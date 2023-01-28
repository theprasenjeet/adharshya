import streamlit as st

import cv2

def make_red_invisible(image_path):

    # Read in image

    img = cv2.imread(image_path)

    # Convert to HSV color space

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define range of red color in HSV

    lower_red = np.array([0,50,50])

    upper_red = np.array([10,255,255])

    # Threshold the image to only select red colors

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image

    res = cv2.bitwise_and(img, img, mask=mask)

    return res

st.set_title("Make Red Color Invisible App")

image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if image_file is not None:

    img = make_red_invisible(image_file)

    st.image(img)

