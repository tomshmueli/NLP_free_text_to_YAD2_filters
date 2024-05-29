def construct_url(car_types, manufacturers, years, prices):
    base_url = "https://www.yad2.co.il/vehicles/cars"
    params = []

    if car_types:
        car_type_param = f"&sogRechev={','.join(car_types)}"
        params.append(car_type_param)

    if manufacturers:
        manufacturer_param = f"&manufacturer={','.join(manufacturers)}"
        params.append(manufacturer_param)

    if years:
        year_param = f"&year={years[0]}-{years[1]}"
        params.append(year_param)

    if prices:
        # Remove commas from prices and format correctly
        formatted_prices = [price.replace(',', '') for price in prices]
        price_param = f"&price={formatted_prices[0]}-{formatted_prices[1]}"
        params.append(price_param)

    # Construct the final URL
    return base_url + "?" + "&".join(params).strip("&")