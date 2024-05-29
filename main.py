from parse import parse_text
from url_constructor import construct_url

def generate_search_url(input_text):
    car_types, manufacturers, years, prices = parse_text(input_text)
    search_url = construct_url(car_types, manufacturers, years, prices)
    return search_url

if __name__ == "__main__":
    input_text = input("Enter your search criteria: ")
    search_url = generate_search_url(input_text)
    print("Generated Search URL:", search_url)
