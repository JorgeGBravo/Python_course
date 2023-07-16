from cv2 import cv2
import face_recognition as fr
from face import Face
from PIL import Image
import numpy as np
from functions import *
from pathlib import Path


photo_Juan_a = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_a.jpg"
photo_Juan_b = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_b.jpg"

# Face('Juan', 'Perez', photo_Juan_a)
# Face('Juan', 'Perez', photo_Juan_b)
# Face('Simon', 'González', photo_Simon)

photo_Simon = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_c.jpg"

list = Face.list_users()

for user in list:
    photo = fr.load_image_file(user[3])
    photo_rgb = translate_to_rgb(photo)
    photo_encode = encode(photo_rgb)

    name = f'{user[1]} {user[2]}'
    cv2.imshow(name, photo_rgb)

cv2.waitKey(0)
