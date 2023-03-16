from pathlib import Path
from typing import List, Optional, Dict

import yaml
from pydantic import BaseModel as pydanticBaseModel
from pydantic import validator, Extra
from streamlit import cache_data


class BaseModel(pydanticBaseModel):
    class Config:
        extra = Extra.forbid


class InfoSpot:
    name: str
    comment: str


class Place(BaseModel):
    """
    Data structure of a place.
    """

    name: str
    last_updated: str
    coordinates: List[float] = []
    data: Optional[Dict]
    provided_by: Optional[str]

    @classmethod
    def check_coordinates_place(cls, value):
        if len(value) == 2:
            return value
        raise ValueError("Coordinates needs to have size 2")


@cache_data  # allows to keep yaml data in memory
def places_reader():
    """
    Reader of all the yaml files.
    """
    path_package = Path(__file__).parent.resolve()

    files = Path(f"{path_package}/places").glob("*.yaml")

    all_places = {}

    for file in files:
        data_loaded = place_reader(file)
        place = Place(**data_loaded)
        all_places[place.name] = place

    return all_places


def place_reader(file):
    with open(file, "r") as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded


if __name__ == "__main__":
    # Read YAML file
    with open("places/carcaixent.yaml", "r") as stream:
        data_loaded = yaml.safe_load(stream)

    print(data_loaded)
    carcaixent = Place(**data_loaded)
    print(carcaixent)
