import cv2
import numpy as np
import streamlit as st

st.title(" Real-time Color Detection with OpenCV")

# Sidebar controls
option = st.selectbox("Choose a color to detect:", ("Red", "Green", "Blue", "All"))
start = st.sidebar.button(" Start Camera")
stop = st.sidebar.button(" Stop Camera")

stframe = st.empty()

if start and not stop:
    cap = cv2.VideoCapture(0)

    while cap.isOpened() and not stop:
        ret, frame = cap.read()
        if not ret:
            st.write("Failed to capture video")
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = None

        if option == "Red":
            # Red wraps around HSV, so use two ranges
            lower_red1 = np.array([0, 120, 70])
            upper_red1 = np.array([10, 255, 255])
            lower_red2 = np.array([170, 120, 70])
            upper_red2 = np.array([180, 255, 255])
            mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
            mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
            mask = mask1 | mask2

        elif option == "Green":
            lower_green = np.array([40, 70, 70])
            upper_green = np.array([80, 255, 255])
            mask = cv2.inRange(hsv_frame, lower_green, upper_green)

        elif option == "Blue":
            lower_blue = np.array([94, 80, 2])
            upper_blue = np.array([126, 255, 255])
            mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

        elif option == "All":
            lower = np.array([0, 50, 50])
            upper = np.array([179, 255, 255])
            mask = cv2.inRange(hsv_frame, lower, upper)

        # Clean the mask (remove noise)
        if mask is not None:
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

            result = cv2.bitwise_and(frame, frame, mask=mask)

            # Draw contours and bounding boxes
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > 500:  # ignore tiny detections
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(result, (x, y), (x + w, y + h), (255, 255, 255), 2)
                    cv2.putText(result, f"{option} Detected", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        else:
            result = frame

        # Convert to RGB for Streamlit
        rgb_frame = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        stframe.image(rgb_frame, channels="RGB")

    cap.release()
