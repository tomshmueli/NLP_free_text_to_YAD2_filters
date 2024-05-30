import spacy
from mapping import CAR_TYPES_EN, MANUFACTURERS_EN

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def parse_text(text):
    doc = nlp(text)
    car_types, manufacturers, years, prices = [], [], [], []

    for ent in doc.ents:
        if ent.label_ == "DATE" and len(ent.text) == 4 and ent.text.isdigit():
            years.append(ent.text)
        elif ent.label_ == "MONEY":
            prices.append(ent.text.replace(',', ''))

    for token in doc:
        if token.lemma_.lower() in CAR_TYPES_EN:
            car_types.append(token.lemma_.lower())
        elif token.lemma_.lower() in MANUFACTURERS_EN:
            manufacturers.append(token.lemma_.lower())

    # Convert price strings to integers for further processing
    prices = [int(price) for price in prices if price.isdigit()]

    return car_types, manufacturers, years, prices
