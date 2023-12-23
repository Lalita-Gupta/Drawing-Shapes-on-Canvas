# Importing Packages

import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import streamlit as st 
from streamlit_drawable_canvas import st_canvas

# function to convert hex_color to rgb
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# title
st.title("Simulation for Drawing Shapes on Canvas")

# displaying canvas
color_canvas = st.color_picker("Pick a color for the canvas", value = "#FFFFFF", key= "canvas")
color_canvas = hex_to_rgb(color_canvas)
uploaded_image = np.ones(shape =(1024,1024,3), dtype = np.int16) * 255
uploaded_image[:] = color_canvas
imageLocation = st.empty()
imageLocation.image(uploaded_image, caption = "Original Image")

st.write("Image dimensions:", uploaded_image.shape)

# sidebar
with st.sidebar:

    # choice of shape:
    choice = st.selectbox("Shape", ["Select one", "Line", "Rectangle", "Circle", "Ellipse", "Text"])

    # parameters for shapes (common parameters for all shapes)
    if choice != "Select one":
        color_shape = st.color_picker("Pick a color for the shape", key= "shape")
        color_shape = hex_to_rgb(color_shape)

    if choice == "Line":
        thickness = st.slider("Thickness", 1, 100, value = 4)
        top_left_x = st.number_input("Enter x of the top-left corner", value = 300, step = 1)
        top_left_y = st.number_input("Enter y of the top-left corner", value = 300, step = 1)
        bottom_right_x = st.number_input("Enter x of the bottom-right vertics", value = 700, step = 1)
        bottom_right_y = st.number_input("Enter y of the bottom-right vertics", value = 700, step = 1)

    if choice == "Rectangle":
        filled = st.toggle("Fill the shape")
        if filled == False:
            thickness = st.slider("Thickness", 0, 100, value = 3)
        else:
            thickness = -1
        top_left_x = st.number_input("Enter x of the top-left corner", value = 350, step = 1)
        top_left_y = st.number_input("Enter y of the top-left corner", value = 350, step = 1)
        bottom_right_x = st.number_input("Enter x of the bottom-right vertics", value = 650, step = 1)
        bottom_right_y = st.number_input("Enter y of the bottom-right vertics", value = 650, step = 1)

    if choice == "Circle":
        filled = st.toggle("Fill the shape")
        if filled == False:
            thickness = st.slider("Thickness", 0, 100, value = 3)
        else:
            thickness = -1
        radius = st.slider("Radius", 1, 1000, value = 200)
        centre_x = st.number_input("Enter x of the centre", value = 500, step = 1)
        centre_y = st.number_input("Enter y of the centre", value = 500, step = 1)

    if choice == "Ellipse":
        filled = st.toggle("Fill the shape")
        if filled == False:
            thickness = st.slider("Thickness", 0, 100, value = 3)
        else:
            thickness = -1
        centre_x = st.number_input("Enter x of the centre", value = 500, step = 1)
        centre_y = st.number_input("Enter y of the centre", value = 500, step = 1)
        major_axis = st.number_input("Enter length of major axis", value = 200, step = 1)
        minor_axis = st.number_input("Enter length of minor axis", value = 100, step = 1)
        angle_rotation = st.slider("Angle of Rotation in anti-clockwise direction", 0, 360, value = 0)
        startAngle = st.slider("Start Angle", 0, 360, value = 0)
        endAngle = st.slider("End Angle", 0, 360, value = 360)

    if choice == "Text":
        thickness = st.slider("Thickness", 1, 100, value = 5)
        text = st.text_input("Text you want to put on canvas", value = "Potato")
        bottom_left_x = st.number_input("Enter x of the bottom-left vertics", value = 340, step = 1)
        bottom_left_y = st.number_input("Enter y of the bottom-left vertics", value = 500, step = 1)
        font_type = st.selectbox("Pick one", ["FONT_HERSHEY_SIMPLEX", "FONT_HERSHEY_PLAIN", "FONT_HERSHEY_DUPLE", "FONT_HERSHEY_COMPLEX", "FONT_HERSHEY_TRIPLEX", "FONT_HERSHEY_COMPLEX_SMALL", "FONT_HERSHEY_SCRIPT_SIMPLEX", "FONT_HERSHEY_SCRIPT_COMPLEX"])
        Dict = {"FONT_HERSHEY_SIMPLEX": 0, "FONT_HERSHEY_PLAIN" : 1, "FONT_HERSHEY_DUPLE" : 2, "FONT_HERSHEY_COMPLEX" : 3, "FONT_HERSHEY_TRIPLEX" : 4, "FONT_HERSHEY_COMPLEX_SMALL" : 5, "FONT_HERSHEY_SCRIPT_SIMPLEX" : 6, "FONT_HERSHEY_SCRIPT_COMPLEX " : 7}
        font_type = Dict[font_type]
        font_scale = st.slider("Scale of the text", 0, 30, value = 3)
        lineType = cv2.LINE_AA
        

if choice == "Line":
    if st.button("Generate"):
        output_image = cv2.line(uploaded_image,(top_left_x, top_left_y), (bottom_right_x, bottom_right_y), color_shape, thickness)
        imageLocation.image(output_image, caption = "Result Image")

if choice == "Rectangle":
    if st.button("Generate"):
        output_image = cv2.rectangle(uploaded_image,(top_left_x, top_left_y), (bottom_right_x, bottom_right_y), color_shape, thickness)
        imageLocation.image(output_image, caption = "Result Image")
  
if choice == "Circle":
    if st.button("Generate"):
        output_image = cv2.circle(uploaded_image, (centre_x, centre_y), radius, color_shape, thickness)
        imageLocation.image(output_image, caption = "Result Image")

if choice == "Ellipse":
    if st.button("Generate"):
        output_image = cv2.ellipse(uploaded_image, (centre_x, centre_y), (major_axis,minor_axis), angle_rotation,startAngle, endAngle, color_shape, thickness)
        imageLocation.image(output_image, caption = "Result Image")

if choice == "Text":
    if st.button("Generate"):
        output_image = cv2.putText(uploaded_image, text, (bottom_left_x, bottom_left_y), font_type, font_scale, color_shape, thickness, lineType)
        imageLocation.image(output_image, caption = "Result Image")
