import spacy
from mapping import CAR_TYPES_EN, MANUFACTURERS_EN
from fuzzywuzzy import fuzz, process
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def length_adjusted_ratio(query, choice):
    partial_score = fuzz.partial_ratio(query, choice)
    length_score = min(len(query), len(choice)) / max(len(query), len(choice)) * 100
    return (partial_score + length_score) / 2

def get_closest_match(query, choices, threshold=80):
    match, score = process.extractOne(query, choices, scorer=length_adjusted_ratio)
    return match if score >= threshold else None

def parse_text(text):
    doc = nlp(text)
    car_types, manufacturers, years, prices = [], [], [], []

    for ent in doc.ents:
        if ent.label_ == "DATE":
            year_tokens = []
            # Check for ranges in the text of the entity
            range_match = re.search(r'(\d{4})\s*-\s*(\d{2,4})', ent.text)
            if range_match:
                start_year = range_match.group(1)
                end_year = range_match.group(2)
                if len(end_year) == 2:  # Handle two-digit year ranges
                    end_year = start_year[:2] + end_year
                year_tokens.extend([start_year, end_year])
            else:
                year_tokens = [token.text for token in ent if token.text.isdigit() and len(token.text) == 4]
            years.extend(year_tokens)
        elif ent.label_ == "MONEY":
            prices.append(ent.text.replace(',', ''))
        elif ent.label_ == "CARDINAL":
            cardinal_numbers = [token.text for token in ent if token.text.isdigit()]
            for number in cardinal_numbers:
                if len(number) == 4:  # Likely to be a year
                    years.append(number)
                else:  # Likely to be a price
                    prices.append(number)

    for token in doc:
        if token.is_punct or not token.is_alpha or token.pos_ not in {"NOUN", "PROPN"} or token.is_stop:
            continue

        if token.lemma_.lower() in CAR_TYPES_EN:
            car_types.append(token.lemma_.lower())
        else:
            closest_manufacturer = get_closest_match(token.lemma_.lower(), MANUFACTURERS_EN)
            if closest_manufacturer and len(manufacturers) < 4:
                manufacturers.append(closest_manufacturer)

    prices = [int(price) for price in prices if price.isdigit()]

    return car_types, manufacturers, years, prices
