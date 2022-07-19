from cv2 import cv2
import face_recognition as fr


def encode(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    return fr.face_encodings(image_rgb)
