from dataclasses import dataclass


@dataclass
class YAML_file_parser():
    coordinates: list
    creator: str
    year: str|int
    data: dict

# to be finished...