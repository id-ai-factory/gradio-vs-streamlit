import streamlit as st
from utils.utils import sepia
from PIL import Image
import numpy as np
from hashlib import sha256

def hash_image(image) -> bytes:
    """画像をsha256ハッシュ化する"""
    if image is None:
        return None
    m = sha256()
    img = Image.open(image)
    m.update(img.tobytes())
    return m.digest()

tabs = st.tabs(["Upload", "Camera"])

with tabs[0]:
    image_uploader = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg", "webp", "bmp"])
    if image_uploader:
        st.image(image_uploader)
    uploader_hash = hash_image(image_uploader)   

with tabs[1]:
    image_camera = st.camera_input("Camera")
    camera_hash = hash_image(image_camera)


image = None
if image_uploader and image_camera:
    # ハッシュを前回の実行と比べる。
    # 異なることは新しいものがアップロードされた意味となる
    if st.session_state["upload_id"] != uploader_hash:
        image = image_uploader
    elif st.session_state["camera_id"] != camera_hash:
        image = image_camera
    elif "last_image" in st.session_state:
        # 両方あるがどっちも新しくないときは最後に使われたものが残る
        image = st.session_state["last_image"] 
    
    # 選択されたものをセッションに保存する
    st.session_state["last_image"] = image
else:
    # 片方だけだったら、それを使う
    image = image_uploader or image_camera

if image:
    image_bits = Image.open(image)
    img_array = np.array(image_bits)[:,:,:3]

    st.image(sepia(img_array))
        
# セッションにハッシュを保存する
st.session_state["upload_id"] = uploader_hash
st.session_state["camera_id"] = camera_hash