import streamlit as st
from common.utils import sepia
from PIL import Image
import numpy as np

tabs = st.tabs(["Upload", "Camera"])

with tabs[0]:
    image_uploader = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg", "webp", "bmp"])

with tabs[1]:
    image_camera = st.camera_input("Camera")


if image_uploader:
    st.image(image_uploader)

image = image_uploader or image_camera
if image:
    image_bits = Image.open(image)
    img_array = np.array(image_bits)[:,:,:3]

    st.image(sepia(img_array))