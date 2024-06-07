import cv2
import numpy as np
import pyautogui
import time

# Set the screen size (width and height)
screen_size = pyautogui.size()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, screen_size)

while True:
    try:
        # Take a screenshot using pyautogui
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert the frame from RGB to BGR (pyautogui takes screenshots in RGB format)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the output file
        out.write(frame)

        # Display the frame
        cv2.imshow("Screen Recording", frame)

        # Exit the recording when 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
            break

        # Add a small delay to prevent high CPU usage
        time.sleep(0.05)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Release the VideoWriter and close all OpenCV windows
out.release()
cv2.destroyAllWindows()
