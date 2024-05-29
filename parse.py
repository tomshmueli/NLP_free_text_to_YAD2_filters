import spacy_stanza
from spacy.matcher import Matcher

# Load the Hebrew model
nlp = spacy_stanza.load_pipeline("he") # Use the Stanza library for Hebrew NLP.
# stanza is a Python NLP library for many languages.

# Define car types and manufacturers for rule-based matching
CAR_TYPES = ["קרוסאוברים", "משפחתיים", "יוקרה", "ג'יפים", "קטנים", "מיניוואנים",
             "מנהלים", "ספורט", "טנדרים", "מסחריים"]

MANUFACTURERS = [
    "BAWBAW", "EVEASYEVEASY", "KTMKTM", "XPENGXPENG", "ZEEKRZEEKR",
    "אאודי", "אבארט", "אוטוביאנקי", "אולדסמוביל", "אוסטין", "אופל",
    "אורה / Ora", "איווייס", "איווקו", "אינפיניטי", "איסוזו",
    "אל.אי.וי.סי / LEVC", "אל.טי.איי", "אלפא רומיאו", "אלפין / ALPINE",
    "אם. ג'י. / MG", "אסטון מרטין", "אף. אי. דאבליו / FEW", "ב.מ.וו",
    "בי.ווי.די / BYD", "ביואיק", "בנטלי", "ג'י.איי.סי/ GAC", "ג'י.אם.סי / GMC",
    "ג'יאו / Geo", "ג'יאיוואן/ Jiayuan", "ג'יי.איי.סי / JAC", "ג'ילי - Geely",
    "ג'יפ / Jeep", "ג'יפ תע''ר", "ג'נסיס", "גרייט וול", "דאצ'יה", "דודג'",
    "דונגפנג", "די.אס / DS", "דייהו", "דייהטסו", "האמר", "הונגצ'י / HONGQI",
    "הונדה", "הינו  HINO", "ווי / WEY", "וויה / VOYAH", "וולוו", "טאטא",
    "טויוטה", "טסלה", "יגואר", "יונדאי", "לאדה", "לינק&קו / Lynk&Co",
    "לינקולן", "ליפמוטור / leapmotor", "ליצ'י", "למבורגיני", "לנד רובר",
    "לנצ'יה", "לקסוס", "מאזדה", "מאן", "מזראטי", "מיני", "מיצובישי",
    "מקסוס", "מרצדס", "ניאו / NIO", "ניסאן", "ננג'ינג", "סאאב", "סאן ליוינג / Sun Living",
    "סאנגיונג", "סאנשיין", "סובארו", "סוזוקי", "סיאט", "סיטרואן", "סמארט",
    "סנטרו", "סקודה", "סקייוול", "סרס / SERES", "פולסטאר / POLESTAR", "פולקסווגן",
    "פונטיאק", "פורד", "פורשה", "פורתינג / FORTHING", "פיאג'ו", "פיאט", "פיג'ו",
    "פרארי", "צ'רי / Chery", "קאדילק", "קופרה", "קיה", "קרייזלר", "רובר", "רנו",
    "שברולט"
]

# Initialize the matcher
matcher = Matcher(nlp.vocab)

# Add rules for car types

# car_type_patterns = [[{"LOWER": car_type.lower()}] for car_type in CAR_TYPES]
matcher.add("CAR_TYPE", car_type_patterns)

# Add rules for manufacturers
manufacturer_patterns = [[{"LOWER": manufacturer.lower()}] for manufacturer in MANUFACTURERS]
matcher.add("MANUFACTURER", manufacturer_patterns)


# Function to parse text and extract relevant information
def parse_text(input_text):
    doc = nlp(input_text)
    matches = matcher(doc)

    car_types = []
    manufacturers = []
    years = []
    prices = []

    for match_id, start, end in matches:
        span = doc[start:end]
        rule_id = nlp.vocab.strings[match_id]
        if rule_id == "CAR_TYPE":
            car_types.append(span.text)
        elif rule_id == "MANUFACTURER" and len(manufacturers) < 4:
            manufacturers.append(span.text)

    price_from = None
    price_to = None

    for token in doc:
        if token.like_num:
            numeric_value = int(token.text.replace(',', ''))
            if 1900 <= numeric_value <= 2100:
                years.append(token.text)
            else:
                if token.nbor(-1).text == "מ":
                    price_from = numeric_value
                elif token.nbor(-1).text == "עד":
                    price_to = numeric_value
                elif not price_from and not price_to:
                    price_to = numeric_value

    if price_from is None:
        price_from = 0
    if price_to is not None:
        prices = [str(price_from), str(price_to)]

    return car_types, manufacturers, years, prices

