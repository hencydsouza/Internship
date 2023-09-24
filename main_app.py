import numpy as np
import streamlit as st
import cv2
from keras.models import load_model
import tensorflow as tf

model = load_model('model-leaf-2.h5')

CLASS_NAMES = ['Apple___healthy','Apple___Black_rot','Apple___Apple_scab']

st.title("Plant Leaf Disease Detection")
st.markdown("Upload an image of the leaf")

image = st.file_uploader("Choose an image...", type="jpg")
submit = st.button('Predict')

if submit:
    if image is not None:
        file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)
        
        resized = cv2.resize(opencv_image, (256,256))
        print(resized.shape)
        
        opencv_image = cv2.resize(opencv_image, (256,256))
        
        opencv_image.shape = (1,256,256,3)
        
        y_pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(y_pred)]
        st.title(str("This is "+result.split('___')[0]+" leaf with "+result.split('___')[1]))