import streamlit as st
from utils.utils import sepia
from PIL import Image
import numpy as np

image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg", "webp", "bmp"])

if image_file:
    st.image(image_file)
    image = Image.open(image_file)
    img_array = np.array(image)[:,:,:3]

    st.image(sepia(img_array))