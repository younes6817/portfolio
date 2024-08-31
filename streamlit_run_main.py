import streamlit as st
from PIL import Image


st.subheader("Color to Grayscale Converter")
st.write("upload image")
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
 camera_image = st.camera_input("Camera")

if camera_image:
   img = Image.open(camera_image)
   gray_camera_img = img.convert('L')
   st.image(gray_camera_img)
elif uploaded_image:
   img_up = Image.open(uploaded_image)
   gray_up = img_up.convert('L')
   st.image(gray_up)
