import spacy
from spacy.matcher import Matcher
from googletrans import Translator
import spacy_stanza
from mappings import CAR_TYPES_MAPPING, MANUFACTURERS_MAPPING

# Load the Hebrew model (optional, if needed for initial processing)
nlp_he = spacy_stanza.load_pipeline("he")

# Load the English model
nlp_en = spacy.load("en_core_web_sm")

# Initialize the translator
translator = Translator()

# Define car types and manufacturers for rule-based matching in English
CAR_TYPES_EN = ["crossover", "family", "luxury", "jeep", "small", "minivan",
                "executive", "sport", "pickup", "commercial"]

MANUFACTURERS_EN = [
    "audi", "abarth", "autobianchi", "oldsmobile", "austin", "opel",
    "ora", "aiways", "iveco", "infiniti", "isuzu", "levc", "ltai",
    "alfa romeo", "alpine", "mg", "aston martin", "few", "bmw", "byd",
    "buick", "bentley", "gac", "gmc", "geo", "jiayuan", "jac", "geely",
    "jeep", "genesis", "great wall", "dacia", "dodge", "dongfeng", "ds",
    "daewoo", "daihatsu", "hummer", "hongqi", "honda", "hino", "wey",
    "voyah", "volvo", "tata", "toyota", "tesla", "jaguar", "hyundai",
    "lada", "lynk & co", "lincoln", "leapmotor", "lixi", "lamborghini",
    "land rover", "lancia", "lexus", "mazda", "man", "maserati", "mini",
    "mitsubishi", "maxus", "mercedes", "nio", "nissan", "nanjing", "saab",
    "sun living", "ssangyong", "sunshine", "subaru", "suzuki", "seat",
    "citroen", "smart", "centro", "skoda", "skywell", "seres", "polestar",
    "volkswagen", "pontiac", "ford", "porsche", "forthing", "piaggio",
    "fiat", "peugeot", "ferrari", "chery", "cadillac", "cupra", "kia",
    "chrysler", "rover", "renault", "chevrolet"
]

# Initialize the matcher
matcher = Matcher(nlp_en.vocab)

# Add rules for car types
car_type_patterns = [[{"LOWER": car_type.lower()}] for car_type in CAR_TYPES_EN]
matcher.add("CAR_TYPE", car_type_patterns)

# Add rules for manufacturers
manufacturer_patterns = [[{"LOWER": manufacturer.lower()}] for manufacturer in MANUFACTURERS_EN]
matcher.add("MANUFACTURER", manufacturer_patterns)


# Function to parse text and extract relevant information
def parse_text(input_text):
    # Translate the input text to English
    translated_text = translator.translate(input_text, src='he', dest='en').text
    doc = nlp_en(translated_text)
    matches = matcher(doc)

    car_types = []
    manufacturers = []
    years = []
    prices = []

    for match_id, start, end in matches:
        span = doc[start:end]
        rule_id = nlp_en.vocab.strings[match_id]
        if rule_id == "CAR_TYPE":
            car_types.append(CAR_TYPES_MAPPING[span.text.lower()])
        elif rule_id == "MANUFACTURER" and len(manufacturers) < 4:
            manufacturers.append(MANUFACTURERS_MAPPING[span.text.lower()])

    price_from = None
    price_to = None

    for token in doc:
        if token.like_num:
            numeric_value = int(token.text.replace(',', ''))
            if 1900 <= numeric_value <= 2100:
                years.append(token.text)
            else:
                if token.nbor(-1).text == "from":
                    price_from = numeric_value
                elif token.nbor(-1).text == "to":
                    price_to = numeric_value
                elif not price_from and not price_to:
                    price_to = numeric_value

    if price_from is None:
        price_from = 0
    if price_to is not None:
        prices = [str(price_from), str(price_to)]

    return car_types, manufacturers, years, prices


if __name__ == "__main__":
    input_text = "מחפש רכבים משפחתיים עד 200000 שקל"
    car_types, manufacturers, years, prices = parse_text(input_text)
    print("Car Types:", car_types)
    print("Manufacturers:", manufacturers)
    print("Years:", years)
    print("Prices:", prices)
