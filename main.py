import streamlit as st

from lib.api import ThisDayAPIConnection

st.set_page_config(
    page_title="This Day in History",
    page_icon="📅",
)

this_day_api_connection = ThisDayAPIConnection(
    connection_name="this_day_api_connection"
)

st.image(
    "https://cdn.discordapp.com/attachments/1136666469606903939/1136666611768643646/Streamlit_gradient.svg"
)
st.title("This Day in History")

input_date = st.date_input(
    "Enter the date you want to look in history for:",
    help="Year is not important, nor it is used.",
    format="DD/MM/YYYY",
)
search_button = st.button("Lookup!")

if search_button:
    data = this_day_api_connection.query(input_date.day, input_date.month)
    st.write(f"Events that happened on {input_date.day}/{input_date.month}")
    st.markdown(data.to_markdown())
