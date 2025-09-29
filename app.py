import time  # to simulate a real time data, time loop
import joblib as jb
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import matplotlib.pyplot as plt
import cv2 as cv
import streamlit as st
from tempfile import NamedTemporaryFile
st.set_page_config(
    page_title="Image processing V1.0", 
    page_icon="✅",
    layout="wide",
)
st.header('Perform Basic Image processing on Your Image') 

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
# Convert the uploaded file to a numpy array
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    # Decode the image as OpenCV format
    cv_image = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
    # with st.form("example_form"):
    height  = st.number_input("height",min_value=100, key="height")
    width = st.number_input("width", min_value=100, key="width")
    # submit = st.form_submit_button("Done")
    cv_image=cv.resize(cv_image,(height,width))
    # Display with Streamlit (convert BGR to RGB for correct colors)
    st.subheader("uploaded Image")
    st.image(cv.cvtColor(cv_image, cv.COLOR_BGR2RGB), channels="RGB") 
    st.header('Perform Canny Edge Detection') 
    t1 = st.slider("Threshold1", 50, 200, 100)
    t2 = st.slider("Threshold2", 50, 300, 200)
    edges = cv.Canny(cv_image,t1,t2)
    cv.resize(edges,(height,width))
    edges=cv.resize(edges,(height,width))
    st.image(edges,caption="Canny Image")

    if edges is not None:
        download_format = st.radio(
            "Choose download format:",
            ("PNG", "JPEG"),key="canny_radio" 
        )

        # Select correct extension and MIME type
    if download_format == "PNG":
        ext = ".png"
        mime = "image/png"
    else:
        ext = ".jpg"
        mime = "image/jpeg"

        # Encode to chosen format
    is_success, buffer = cv.imencode(ext, edges)

    if is_success:
        st.download_button(
                label=f"Download as {download_format}",
                data=buffer.tobytes(),
                file_name=f"processed_image{ext}",
                mime=mime
            )
    st.header(' Blur my image using Gaussian Blur')
    ksize = st.slider("Kernel Size", 1, 21, 5, step=2)
    Blur_img = cv.GaussianBlur(cv_image, (ksize, ksize), 0)
    Blur_img=cv.resize(Blur_img,(height,width))
    st.image(cv.cvtColor(Blur_img, cv.COLOR_BGR2RGB),
                caption="Blurred Image")
    if Blur_img is not None:
        download_form = st.radio(
            "Choose download format:",
            ("PNG", "JPEG"),key="Blur_radio" 
        )

        # Select correct extension and MIME type
    if download_form == "PNG":
        ext = ".png"
        mime = "image/png"
    else:
        ext = ".jpg"
        mime = "image/jpeg"

        # Encode to chosen format
    success, buff = cv.imencode(ext, Blur_img)

    if success:
        st.download_button(
                label=f"Download as {download_form}",
                data=buff.tobytes(),
                file_name=f"Blur_img{ext}",
                mime=mime
            )
