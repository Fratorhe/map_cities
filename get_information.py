from pathlib import Path


def get_sections(data):
    return data.keys()


def get_places_section(data, section):
    return data[section]


def get_cities():
    files = Path("places").glob("*.yaml")
    return [file.stem for file in files]


if __name__ == "__main__":
    cities = get_cities()
    print(cities)
