def construct_url(car_types, manufacturers, years, prices):
    base_url = "https://www.yad2.co.il/vehicles/cars"
    params = []

    if car_types:
        car_type_param = f"&carFamilyType={','.join(car_types)}"
        params.append(car_type_param)

    if manufacturers:
        manufacturer_param = f"&manufacturer={','.join(manufacturers)}"
        params.append(manufacturer_param)

    if years:
        year_param = f"&year={years[0]}-{years[1]}"
        params.append(year_param)

    if prices:
        price_param = f"&price={prices[0]}-{prices[1]}"
        params.append(price_param)

    return base_url + "?" + "&".join(params)


if __name__ == "__main__":
    car_types = ["2"]
    manufacturers = ["2", "102", "290"]
    years = []
    prices = ["-1", "200000"]
    url = construct_url(car_types, manufacturers, years, prices)
    print(url)
