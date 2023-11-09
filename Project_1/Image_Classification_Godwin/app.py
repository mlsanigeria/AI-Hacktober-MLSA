# Model Deployment using Streamlit

# import libraries
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.xception import preprocess_input


img_height, img_width = (300, 400)
classes = {0: 'Bungalow', 1: 'High-rise', 2: 'Storey-building'}
model_name = 'xception_v1_11_0.810.h5'
model = load_model(model_name)

# Function to Read and Manupilate Images for display
def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image

# Function to Read and Manupilate Images for model input
def process_image(img):

    im = Image.open(img).resize((img_height, img_width))
    image = np.array(im)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis = 0)
    return image 

# Function for makin predictions
def predict(model, img_data):

    prediction = model.predict(img_data)
    class_index = np.argmax(prediction)
    img_class = classes[class_index]
    return img_class

def main():

    st.title("Image Classification Web App")
    uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png']) # Uploading the File to the Page

    # Checking the Format of the page
    if uploadFile is not None:
        img = load_image(uploadFile)
        st.image(img)
        st.write("Image Uploaded Successfully")

        model_img = process_image(uploadFile)
        img_cls = predict(model, model_img)
        output_text = f"The image building uploaded is a {img_cls}"

        st.success(output_text)
    else:
        st.write("Make sure you image is in JPG/PNG Format.")

if __name__ == "__main__":
    main()