import spacy
from numerizer import numerizer

from mapping import CAR_TYPES_EN, MANUFACTURERS_EN
from fuzzywuzzy import fuzz, process
from datetime import datetime
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Stop words to prevent irrelevant tokens from being sent to fuzzy matching
STOP_WORDS = {"decade", "price", "year", "month", "me", "NIS", "shekel"}


def handle_prices_range(prices, text):
    upper_bound = ["at most", "up to", "less than", "maximum", "no more than", "under", "below"]
    lower_bound = ["at least", "more than", "minimum", "no less than", "over", "above"]

    if len(prices) == 1:
        context = text.lower()
        # check if the context contains any of the upper bound phrases
        if any(phrase in context for phrase in upper_bound):
            prices = [0, prices[0]]
        # check if the context contains any of the lower bound phrases
        elif any(phrase in context for phrase in lower_bound):
            prices = [prices[0], 1000000]
    return prices


def handle_years_range(years, text):
    current_year = datetime.now().year
    upper_bound = ["until", "to", "before", "by", "up to", "less than", "maximum", "no more than", "under", "below"]
    lower_bound = ["since", "from", "after", "starting from", "at least",
                   "more than", "minimum", "no less than", "above"]
    if len(years) == 1:
        context = text.lower()
        if any(phrase in context for phrase in upper_bound):
            years = [years[0], str(current_year)]
        elif any(phrase in context for phrase in lower_bound):
            years = [min(years), max(years)]

    return years


def length_adjusted_ratio(query, choice):
    partial_score = fuzz.partial_ratio(query, choice)
    length_score = min(len(query), len(choice)) / max(len(query), len(choice)) * 100
    return (partial_score + length_score) / 2


def get_closest_match(query, choices, threshold=80):
    match, score = process.extractOne(query, choices, scorer=length_adjusted_ratio)
    return match if score >= threshold else None


def parse_text(text):
    """
    Extract car types, manufacturers, years, and prices from the input text
    perform it in 2 stages of extraction:
    1. Extract entities using spaCy's named entity recognition
    2. Extract tokens using spaCy's part-of-speech tagging and lemmatization
    function also deals with mistakes that were caused due to wrong translation using fuzzy matching and Regex
    :param text: translated to english sentence from the user
    :return: extracted car types, manufacturers, years, and prices
    """
    doc = nlp(text)
    car_types, manufacturers, years, prices = [], [], [], []
    current_year = datetime.now().year

    # Extract entities using spaCy's named entity recognition
    for ent in doc.ents:
        if ent.label_ == "DATE":
            if "last decade" in ent.text.lower():
                years.append(current_year - 10)
                years.append(current_year)
                continue
            # Extract individual years from date entities
            range_match = re.search(r'(\d{4})\s*-\s*(\d{2,4})', ent.text)
            if range_match:
                start_year = range_match.group(1)
                end_year = range_match.group(2)
                if len(end_year) == 2:
                    end_year = start_year[:2] + end_year
                years.extend([start_year, end_year])
            else:
                year_tokens = [token.text for token in ent if token.text.isdigit() and len(token.text) == 4]
                years.extend(year_tokens)
        elif ent.label_ == "MONEY":
            prices.append(ent.text.replace(',', ''))
        elif ent.label_ == "CARDINAL":
            # Check if cardinal numbers are likely to be years or prices
            cardinal_text = ent.text
            if not cardinal_text.isdigit():
                try:
                    cardinal_text = numerizer.numerize(cardinal_text)
                except ValueError:
                    continue  # If numerize fails, skip this entity

            cardinal_numbers = re.findall(r'\d+', cardinal_text)
            for number in cardinal_numbers:
                if len(number) == 4:  # Likely to be a year
                    years.append(number)
                else:  # Likely to be a price
                    prices.append(number)

    # Extract tokens using spaCy's part-of-speech tagging and lemmatization
    for token in doc:
        # Skip tokens that are punctuation, non-alphanumeric, or not nouns/proper nouns, or common stopwords
        if token.is_punct or not token.is_alpha or token.pos_ \
                not in {"NOUN", "PROPN"} or token.is_stop or token.lemma_.lower() in STOP_WORDS:
            continue

        if token.lemma_.lower() in CAR_TYPES_EN:
            car_types.append(token.lemma_.lower())
        elif token.like_num and token.text.isdigit():
            # check if the token is a price
            if len(token.text) > 4:
                prices.append(token.text)
            else:
                # check if the token is a year
                if 1900 <= int(token.text) <= current_year:
                    years.append(token.text)
        else:
            # Apply fuzzy matching for potential manufacturer names
            closest_manufacturer = get_closest_match(token.lemma_.lower(), MANUFACTURERS_EN)
            if closest_manufacturer and len(manufacturers) < 4:
                manufacturers.append(closest_manufacturer)

    # Convert price strings to integers for further processing
    prices = [int(price) for price in prices if price.isdigit()]

    # Handle price ranges
    prices = handle_prices_range(prices, text)
    # Handle year ranges
    years = handle_years_range(years, text)

    return car_types, manufacturers, years, prices
