import cv2

import numpy as np

import streamlit as st

# Create a function to apply the color filter

def make_red_invisible(img):

    # Convert the image to the HSV color space

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the red color

    lower_red = np.array([0,100,100])

    upper_red = np.array([10,255,255])

    # Create a mask for the red color

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Apply the mask to the image

    img[mask != 0] = [0, 0, 0]

    return img

def main():

    st.set_page_config(page_title="Remove Red Color", page_icon=":guardsman:", layout="wide")

    st.title("Remove Red Color")

    st.subheader("Select an image and adjust the color filter to make the red color invisible.")

    

    # Add a file uploader widget

    image_path = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if image_path is None:

        st.warning("Please upload an image.")

    else:

        # Read in the image

        img = cv2.imread(str(image_path))

        

        # Create a slider to adjust the color filter

        color_filter = st.slider("Adjust color filter", 0, 10, 0, 1)

        

        # Define the lower and upper bounds of the red color

        lower_red = np.array([0,100,100])

        upper_red = np.array([color_filter,255,255])

        # Create a mask for the red color

        mask = cv2.inRange(img, lower_red, upper_red)

        # Apply the mask to the image

        img[mask != 0] = [0, 0, 0]

        

        # Show the original and filtered images

        st.image(img, width=700)

if __name__ == "__main__":

    main()

