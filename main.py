import streamlit as st

from get_information import display_information
from reader_places import places_reader
from telegram_bot import set_telegram_bot

st.set_page_config(
    page_title="streamlit-folium documentation",
    page_icon=":world_map:️",
    layout="wide",
)

# load the yaml data.
all_places = places_reader()

"# Map with travel advices"

left, right = st.columns(2)

bot = set_telegram_bot(st.secrets["TOKEN"])
bot.infinity_polling()

# print(all_places)

with left:
    import folium

    from streamlit_folium import st_folium

    # center on Liberty Bell, add marker
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
