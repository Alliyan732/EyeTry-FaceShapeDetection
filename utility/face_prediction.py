import face_alignment
from skimage import io

import cv2

def isFace(imagePath):
    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType.TWO_D, flip_input=False)
    input = io.imread(imagePath)

    result = fa.get_landmarks(input)

    return result


def isFaceAlt(imagePath):
    img = cv2.imread(imagePath)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )
    return face