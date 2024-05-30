from mapping import CAR_TYPES_MAPPING, MANUFACTURERS_MAPPING


def construct_url(car_types, manufacturers, years, prices):
    base_url = "https://www.yad2.co.il/vehicles/cars?"
    filters = []

    if car_types:
        car_type_ids = [CAR_TYPES_MAPPING[car_type] for car_type in car_types]
        filters.append(f"carFamilyType={','.join(map(str, car_type_ids))}")

    if manufacturers:
        manufacturer_ids = [MANUFACTURERS_MAPPING[manufacturer] for manufacturer in manufacturers]
        filters.append(f"manufacturer={','.join(map(str, manufacturer_ids))}")

    if years:
        years.sort()
        filters.append(f"year={years[0]}-{years[-1]}")

    if prices:
        prices.sort(key=int)
        filters.append(f"price={prices[0]}-{prices[-1]}")

    return base_url + "&".join(filters)
