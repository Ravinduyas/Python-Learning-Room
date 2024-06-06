import cv2
import numpy as np
import pyautogui

# Set the screen size (width and height)
screen_size = pyautogui.size()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_size))

while True:
    # Take a screenshot using pyautogui
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert the frame from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the output file
    out.write(frame)

    # Exit the recording when 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the VideoWriter and close all OpenCV windows
out.release()
cv2.destroyAllWindows()
