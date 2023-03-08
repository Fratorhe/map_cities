import glob
import os
from pathlib import Path

import streamlit as st


def display_information(data):
    # get the sections
    sections = get_sections(data)

    for section in sections:
        places_section = get_places_section(data, section)
        if places_section:
            st.header(section.title())
            s = ""
            for place in places_section:
                s += f'- **{place["name"].title()}**: {place["comment"]} \n'

            st.markdown(s)


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
