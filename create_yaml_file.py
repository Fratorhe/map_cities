from dataclasses import dataclass

import yaml


@dataclass
class YAML_file_parser:
    coordinates: list
    place: str
    creator: str
    year: str | int
    data: dict

    def __post_init__(self):

        # we need to re-arrange the data to fit the format of the yaml files.
        data_1 = {}
        for (
            section,
            entries,
        ) in (
            self.data.items()
        ):  # eg. section: 'resturants', entries: {'La riua': 'paella', 'Martin rico ultramarinos': 'tapas'}
            data_1[section] = []
            for place, comment in entries.items():
                data_1[section].append({"name": place, "comment": comment})

        self.data = data_1
        del data_1

    def to_YAML(self):
        to_store = {
            "name": self.place,
            "provided_by": self.creator,
            "last_updated": self.year,
            "data": self.data,
            "coordinates": self.coordinates,
        }

        with open(f'{self.place.lower()}.yaml', 'w') as file:
            yaml.dump(to_store, file)

        print('YAML file saved.')