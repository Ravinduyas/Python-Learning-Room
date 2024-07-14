import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()
click_threshold = 20  # Distance threshold for detecting click

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
            
            # Get coordinates of the index finger tip and thumb tip
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            
            # Convert normalized coordinates to pixel coordinates
            h, w, _ = image.shape
            finger_x = int(index_finger_tip.x * w)
            finger_y = int(index_finger_tip.y * h)
            thumb_x = int(thumb_tip.x * w)
            thumb_y = int(thumb_tip.y * h)
            
            # Convert coordinates to screen coordinates
            screen_x = int(screen_width / w * finger_x)
            screen_y = int(screen_height / h * finger_y)
            
            # Move the mouse
            pyautogui.moveTo(screen_x, screen_y)
            
            # Calculate the distance between the index finger tip and thumb tip
            distance = math.hypot(thumb_x - finger_x, thumb_y - finger_y)
            
            # Perform a click if the distance is less than the threshold
            if distance < click_threshold:
                pyautogui.click()
                
    # Display the resulting image
    cv2.imshow('Hand Tracking', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
