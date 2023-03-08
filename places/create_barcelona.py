from create_yaml_file import YAML_file_parser

if __name__ == "__main__":
    place = "Barcelona"
    coordinates = [41.3874, 2.1686]
    creator = "Ernest"
    year = 2023
    restaurants = {
        "100 Montaditos": "fast food, but good. On wednesday",
        "El bosc de les fades": "coffee place",
        "Federal Cafe Gotic": "brunch",
        "Mi burrito y yo": "cheap and good",
        "Flax & Kale Passage": " ",
        "Brew Wild BCN": " ",
        "Puertecillo Born": "Fish",
        "Mercat Boqueria": "oysters, fried fish, jamón, empanadillas",
    }
    monuments = {}

    city_skyline = {
        "Museu Nacional d’Art de Catalunya": " ",
        "Hotel W": "You can get a drink on the last floor. Expensive, but great views. Dressing code. ",
        "Castell de Montjuic": " ",
    }
    food = {"calçots": "grilled green onion"}
    drinks = {
        "Crema catalana": "shot, creamy sweet drink.Usually to drink after dinner",
    }

    data = {
        "restaurants": restaurants,
        "food": food,
        "drinks": drinks,
        "monuments": monuments,
        "city skyline": city_skyline,
    }

    create_city = YAML_file_parser(coordinates, place, creator, year, data)
    create_city.to_YAML()
