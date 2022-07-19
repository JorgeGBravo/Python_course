from cv2 import cv2
import face_recognition as fr
from face import Face
from PIL import Image
import numpy as np
from pathlib import Path


def encode(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    return fr.face_encodings(image_rgb)


photo_Juan_a = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_a.jpg"
photo_Juan_b = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_b.jpg"

# Face('Juan', 'Perez', photo_Juan_a)
# Face('Juan', 'Perez', photo_Juan_b)
# Face('Simon', 'González', photo_Simon)

photo_Simon = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_c.jpg"

list = Face.list_users()

for user in list:
    name = f'{user[1]} {user[2]}'
    image = np.array(Image.open(user[3]))
    photo = encode(image)
