import spacy
from mapping import CAR_TYPES_EN, MANUFACTURERS_EN
from fuzzywuzzy import fuzz, process

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def length_adjusted_ratio(query, choice):
    partial_score = fuzz.partial_ratio(query, choice)
    length_score = min(len(query), len(choice)) / max(len(query), len(choice)) * 100
    return (partial_score + length_score) / 2

def get_closest_match(query, choices, threshold=60):
    # Use fuzzy matching to find the closest match from the list of choices
    match, score = process.extractOne(query, choices, scorer=length_adjusted_ratio)
    # Ensure the matched word is sufficiently similar to the entire word
    return match if score >= threshold else None

def parse_text(text):
    doc = nlp(text)
    car_types, manufacturers, years, prices = [], [], [], []

    for ent in doc.ents:
        if ent.label_ == "DATE":
            # Extract individual years from date entities
            year_tokens = [token.text for token in ent if token.text.isdigit() and len(token.text) == 4]
            years.extend(year_tokens)
        elif ent.label_ == "MONEY":
            prices.append(ent.text.replace(',', ''))
        elif ent.label_ == "CARDINAL":
            # Check if cardinal numbers are likely to be years or prices
            cardinal_numbers = [token.text for token in ent if token.text.isdigit()]
            for number in cardinal_numbers:
                if len(number) == 4:  # Likely to be a year
                    years.append(number)
                else:  # Likely to be a price
                    prices.append(number)

    for token in doc:
        # Skip tokens that are punctuation, non-alphanumeric, or not nouns/proper nouns, or common stopwords
        if token.is_punct or not token.is_alpha or token.pos_ not in {"NOUN", "PROPN"} or token.is_stop:
            continue

        if token.lemma_.lower() in CAR_TYPES_EN:
            car_types.append(token.lemma_.lower())
        else:
            # Apply fuzzy matching for potential manufacturer names
            closest_manufacturer = get_closest_match(token.lemma_.lower(), MANUFACTURERS_EN)
            if closest_manufacturer and len(manufacturers) < 4:
                manufacturers.append(closest_manufacturer)

    # Convert price strings to integers for further processing
    prices = [int(price) for price in prices if price.isdigit()]

    return car_types, manufacturers, years, prices
