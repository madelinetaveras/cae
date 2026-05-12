import streamlit as st

from data.database import initialize_database
from ui._brand import inject_styles
from ui.home_page import render_home_page

st.set_page_config(
    page_title="QueHacerSD",
    layout="wide"
)

try:

    initialize_database()

except Exception as error:

    st.error(
        f"No pudimos inicializar la base de datos: {error}"
    )

inject_styles()

render_home_page()
