import streamlit as st

import cv2

import numpy as np

# Create a function to process the image

def make_red_invisible(img, threshold):

    # Convert image to HSV color space

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define range of red color in HSV

    lower_red = np.array([0, 50, 50])

    upper_red = np.array([10, 255, 255])

    # Threshold the image to get only red colors

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image

    res = cv2.bitwise_and(img, img, mask=mask)

    # Convert the result back to BGR color space

    res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)

    # Convert the result to grayscale

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    # Apply threshold to make the pixels below the threshold transparent

    _, alpha = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Create a 3-channel alpha mask

    b, g, r = cv2.split(res)

    rgba = [b, g, r, alpha]

    img_bgra = cv2.merge(rgba, 4)

    # Return the processed image

    return img_bgra

def main():

    st.set_page_config(page_title="Red color invisible", page_icon=":guardsman:", layout="wide")

    # Select an image file

    image_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if not image_file:

        st.error("Please upload an image file")

        return

    # Read in image

    img = cv2.imread(image_file)

    # Create a slider for the threshold

    threshold = st.slider("Threshold", 0, 255, 128)

    # Process the image

    img_processed = make_red_invisible(img, threshold)

    # Show the original and processed images

    st.image(img, caption="Original Image", use_column_width=True)

    st.image(img_processed, caption="Red color invisible", use_column_width=True)

if __name__ == "__main__":

    main()

