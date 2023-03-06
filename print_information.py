import streamlit as st

# from reader_places import InfoPlace


def display_information(data):

    for section, places_section in data.items():
        st.header(section.title())
        s = ""
        for place in places_section:
            s += f'- **{place["name"].title()}**: {place["comment"]} \n'

        st.markdown(s)
