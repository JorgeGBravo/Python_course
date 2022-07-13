from cv2 import cv2
import face_recognition as fr
from face import Face
from pathlib import Path

photo_Juan_a = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_a.jpg"
photo_Juan_b = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_b.jpg"
photo_Simon = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_c.jpg"

#Face('Juan', 'Perez', photo_Juan_a)
#Face('Juan', 'Perez', photo_Juan_b)
#Face('Simon', 'González', photo_Simon)

list = Face.list_photos()

for user in list:
    print(Path(user[0]))
