import streamlit as st

from lib.api import ThisDayAPIConnection

this_day_api_connection = ThisDayAPIConnection(
    connection_name="this_day_api_connection"
)

input_date = st.date_input(
    "Enter the date you want to look in history for:",
    help="Year is not important, nor is it used.",
)
search_button = st.button("Lookup!")

if search_button:
    data = this_day_api_connection.query(input_date.day, input_date.month)
    st.write(f"Events that happened on {input_date.day}/{input_date.month}")
    for event in data.events:
        st.write(f"{event.year}: {event.description}")
        for wikipedia in event.wikipedia:
            st.write(f"Read more: {wikipedia.wikipedia}")
