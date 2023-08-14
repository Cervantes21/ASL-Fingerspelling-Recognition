import os
import cv2
import uuid
import time

# Specify the path for captured images
IMAGES_PATH = './Tensorflow/workspace/images/collectedImages'
os.makedirs(IMAGES_PATH, exist_ok=True)

# List of labels
labels = [
    'Hello',
    'Thanks',
    'Yes',
    'No',
    'ILoveYou'
]

# Number of images to capture per label
n_img = 20

# Function to capture an image
def capture_image(label):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        imagename = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('Frame', frame)
        cap.release()
    else:
        print("Error: Unable to capture image from the camera.")

# Capture images for each label
for label in labels:
    label_folder = os.path.join(IMAGES_PATH, label)
    os.makedirs(label_folder, exist_ok=True)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(n_img):
        print(f"Capturing image {imgnum+1}/{n_img}")
        capture_image(label)
        time.sleep(2)

# Wait for the user to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

