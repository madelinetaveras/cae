import streamlit as st


def inject_styles():
    """
    Inyecta estilos visuales globales.
    """

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #FAF7F2;
        }

        h1, h2, h3 {
            color: #1E2761;
        }

        p, label, div {
            color: #1A1A1A;
        }

        div.stButton > button {
            background-color: #F96167;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1rem;
            font-weight: 600;
        }

        div.stButton > button:hover {
            background-color: #e04d53;
            color: white;
        }

        [data-testid="stSidebar"] {
            background-color: white;
        }

        .block-container {
            padding-top: 2rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
