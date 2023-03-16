import streamlit as st
import yaml

from get_information import get_sections, get_places_section
from reader_places import places_reader


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


st.set_page_config(
    page_title="City Explorer",
    page_icon=":world_map:",
    layout="wide",
)

# load the text for the website.
with open('text.yaml', "r") as stream:
    text_website = yaml.safe_load(stream)

# load the yaml data.
all_places = places_reader()

st.title(text_website['title'])

st.markdown(f'<div style="text-align: justify;"><p><i>{text_website["intro"]}<i><p></div>', unsafe_allow_html=True)
st.markdown(f'<div style="text-align: justify;"><p><i>{text_website["contact"]}<i><p></div>', unsafe_allow_html=True)


left, right = st.columns(2)

# print(all_places)

with left:
    import folium

    from streamlit_folium import st_folium

    # center my town
    m = folium.Map(location=[39.1202, 0.4543], zoom_start=1)

    for name, place in all_places.items():
        folium.Marker(place.coordinates, popup=place.name, tooltip=place.name).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)

with right:
    last_clicked = st_data["last_object_clicked_tooltip"]
    if last_clicked is None:
        st.header("Click on the map to show information...")

    if last_clicked:
        location_clicked = all_places[last_clicked]
        data_clicked = (
            location_clicked.data
        )  # get the last click, but if Null, give my town.

        # name of the place
        st.title(location_clicked.name)

        # actual info of the place
        display_information(data_clicked)

        # person who provided the info
        st.markdown(f"*Last updated in {location_clicked.last_updated}*")
        st.markdown(f"*Information kindly provided by {location_clicked.provided_by}*")

st.columns(1)
st.markdown(f'<div style="text-align: justify;"><p><i>{text_website["footer"]}<i><p></div>',
                unsafe_allow_html=True)
