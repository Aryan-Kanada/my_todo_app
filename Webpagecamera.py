import streamlit as st
from PIL import Image, ImageOps

with st.expander("Start Camera"):
    #Start the Camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #Create a pillow Image
    img = Image.open(camera_image)

    # Invert the image
    #inverted_img = ImageOps.invert(img.convert("RGB"))

    #Convert Image into grayscale
    gray_img = img.convert("L")

    #Render the gray scale image in webpage
    st.image(gray_img)