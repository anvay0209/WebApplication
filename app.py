import streamlit as st
import requests
from PIL import Image
import io

API_URL = "http://127.0.0.1:8000/upload/"  # Backend URL

st.title("Image Resizer & Twitter Uploader 🚀")

# File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Upload Button
    if st.button("Resize & Upload to Twitter"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            st.success("Image successfully resized and posted to Twitter! 🎉")
        else:
            st.error(f"Error: {response.json().get('detail')}")
