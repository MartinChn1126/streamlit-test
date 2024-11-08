import streamlit as st
import cv2
import time

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

with st.empty():
    start_button = st.button('start sample',key='start')

    if start_button:
        camera = cv2.VideoCapture(0)

        with st.container():
            stop_button = st.button('stop',key='stop')

            with st.empty():
                while not stop_button:
                    ret,image = camera.read()
                    st.image(image,channels='BGR',use_container_width=True)
                    time.sleep(0.02)
                    

        camera.release()
