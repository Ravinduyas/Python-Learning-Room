import cv2
import mediapipe as mp
import pyautogui
import math
from collections import deque

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()
click_threshold = 30  # Distance threshold for detecting click
smooth_factor = 5  # Number of previous points to consider for smoothing

# Deques to store the recent points for smoothing
x_points = deque(maxlen=smooth_factor)
y_points = deque(maxlen=smooth_factor)

def get_smooth_coordinates(x_points, y_points):
    avg_x = sum(x_points) / len(x_points)
    avg_y = sum(y_points) / len(y_points)
    return avg_x, avg_y

while True:
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    
    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image and detect hands
    result = hands.process(rgb_image)
    
    # If hands are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks on image
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get coordinates of the index finger tip and middle finger tip
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            
            # Convert normalized coordinates to pixel coordinates
            h, w, _ = image.shape
            index_x = int(index_finger_tip.x * w)
            index_y = int(index_finger_tip.y * h)
            middle_x = int(middle_finger_tip.x * w)
            middle_y = int(middle_finger_tip.y * h)
            
            # Calculate the midpoint between index and middle fingers
            mid_x = (index_x + middle_x) // 2
            mid_y = (index_y + middle_y) // 2
            
            # Add the current midpoint to the deques
            x_points.append(mid_x)
            y_points.append(mid_y)
            
            # Get the smoothed coordinates
            smooth_x, smooth_y = get_smooth_coordinates(x_points, y_points)
            
            # Convert coordinates to screen coordinates
            screen_x = int(screen_width / w * smooth_x)
            screen_y = int(screen_height / h * smooth_y)
            
            # Move the mouse
            pyautogui.moveTo(screen_x, screen_y)
            
            # Calculate the distance between the index finger tip and middle finger tip
            distance = math.hypot(middle_x - index_x, middle_y - index_y)
            
            # Perform a click if the distance is less than the threshold
            if distance < click_threshold:
                pyautogui.click()
                
    # Display the resulting image
    cv2.imshow('Hand Tracking', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
