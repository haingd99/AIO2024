import numpy as np
from zutils import process_image, annotate_image
import streamlit as st
from PIL import Image


def main():
    st. title ("Object Detection for Images ")
    file = st. file_uploader ("Upload Image ", type = ["jpg ","png ","jpeg "])
    if file is not None :   
        st. image (file , caption = " Uploaded Image ")
        conf_score = []
        image = Image . open ( file )
        image = np. array ( image )
        detections = process_image ( image )
        processed_image, conf_score = annotate_image (image , detections )
        st. image ( processed_image , caption = " Processed Image ")
        st.write(conf_score)

if __name__ == "__main__":
    main() 

