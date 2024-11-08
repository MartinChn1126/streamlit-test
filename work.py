import streamlit as st

st.markdown(
    """
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>""", 
    unsafe_allow_html=True
)

def main_page():

    st.text('Working...!')

