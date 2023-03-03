import glob
from typing import List, Optional

import yaml
from pydantic import BaseModel as pydanticBaseModel
from pydantic import validator, Extra
from streamlit import cache_resource


class BaseModel(pydanticBaseModel):
    class Config:
        extra = Extra.forbid


class InfoSpot:
    name: str
    comment: str


class InfoPlace(BaseModel):
    '''
    Data structure of a spots in a place.
    If we want to allow for more sections in the yaml files, they have to be included here.
    We could use dynamic model creation in pydantic, but then the internal layers would be more difficult to handle.
    '''
    restaurants: Optional[List]
    monuments: Optional[List]


class Place(BaseModel):
    '''
    Data structure of a place.
    '''

    name: str
    last_updated: str
    coordinates: List[float] = []
    data: Optional[InfoPlace]
    provided_by: Optional[str]

    @validator('coordinates', allow_reuse=True)
    @classmethod
    def check_coordinates_place(cls, value):
        if len(value) == 2:
            return value
        raise ValueError('Coordinates needs to have size 2')


# @cache_resource # allows to keep yaml data in memory
def places_reader():
    """
    Reader of all the yaml files.
    """
    files = glob.glob('places/*.yaml')

    all_places = {}

    for file in files:
        with open(file, 'r') as stream:
            data_loaded = yaml.safe_load(stream)

        place = Place(**data_loaded)
        all_places[place.name] = place

    return all_places


if __name__ == "__main__":
    # Read YAML file
    with open("places/carcaixent.yaml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)

    print(data_loaded)
    carcaixent = Place(**data_loaded)
    print(carcaixent)
