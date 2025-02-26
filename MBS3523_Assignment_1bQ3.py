import cv2
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Flip the frame in different orientations
    flip_horizontal = cv2.flip(frame, 1)  # Flip horizontally (1)
    flip_vertical = cv2.flip(frame, 0)    # Flip vertically (0)
    flip_both = cv2.flip(frame, -1)       # Flip both horizontally and vertically (-1)

    # Resize frames to fit in a 2x2 grid
    height, width = frame.shape[:2]
    resized_frame = cv2.resize(frame, (width // 2, height // 2))
    resized_flip_horizontal = cv2.resize(flip_horizontal, (width // 2, height // 2))
    resized_flip_vertical = cv2.resize(flip_vertical, (width // 2, height // 2))
    resized_flip_both = cv2.resize(flip_both, (width // 2, height // 2))

    # Create a blank canvas to hold all four frames
    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    # Place each frame in the correct position on the canvas
    canvas[:height // 2, :width // 2] = resized_frame  # Top-left: Original
    canvas[:height // 2, width // 2:] = resized_flip_horizontal  # Top-right: Flipped horizontally
    canvas[height // 2:, :width // 2] = resized_flip_vertical  # Bottom-left: Flipped vertically
    canvas[height // 2:, width // 2:] = resized_flip_both  # Bottom-right: Flipped both

    # Display the canvas in a single window
    cv2.imshow('Webcam Frames', canvas)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()