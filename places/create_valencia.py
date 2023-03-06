from create_yaml_file import YAML_file_parser

if __name__ == "__main__":
    place = "Valencia"
    coordinates = [39.4699, 0.3763]
    creator = "Fran"
    year = 2023
    restaurants = {
        "La riua": "paella",
        "Martin rico ultramarinos": "tapas",
        "Bar biosca": "tapas",
        "Saona": "Fusion",
        "La pascuala": "Brunch, around 10am",
        "Casa Carmela": "Lunch, rice",
        "100 Montaditos": "fast food, but good. On wednesday",
    }
    monuments = {
        "Lonja de la seda": "Old trade market",
        "Ciudad de las artes": "Museums, visit outside",
    }

    pubs = {}

    food = {
        "Paella": "with chicken and rabbit",
        "Arroz a banda": "rice with seafood",
        "Fideua": "similar to above but with pasta",
        "Arroz negro": "black rice with seafood",
        "Arroz al horno": "rice with meat cooked in the oven",
        "Buñuelos de calabaza": "pumpkin dough fried, street food",
    }
    drinks = {
        "Agua de Valencia": "cocktail with orange juice",
        "Horchata con fartons": "similar to almond milk",
        "Carajillo quemado de ron": "coffee with burned rum, my favorite",
        "Zumo de naranja": "fresh orange juice with best oranges",
        "Crema catalana": "shot, creamy sweet drink.Usually to drink after dinner",
        "Cazalla": "shot, strong alcohol similar to sambuca",
    }

    data = {
        "restaurants": restaurants,
        "food": food,
        "drinks": drinks,
        "monuments": monuments,
        # 'pubs': pubs
    }

    create_city = YAML_file_parser(coordinates, place, creator, year, data)
    create_city.to_YAML()
