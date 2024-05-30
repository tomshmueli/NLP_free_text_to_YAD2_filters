from parse import parse_text
from url_constructor import construct_url
from googletrans import Translator


def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='he', dest='en')
    return translation.text


def main():
    user_input = input("Enter your search query: ")
    translated_text = translate_to_english(user_input)
    car_types, manufacturers, years, prices = parse_text(translated_text)
    url = construct_url(car_types, manufacturers, years, prices)
    print("Constructed URL:", url)


if __name__ == "__main__":
    main()
