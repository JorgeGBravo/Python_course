import sqlite3

from cv2 import cv2
import face_recognition as fr
from face import Face
from pathlib import Path

photo = "C:/Users/jdgbr/PycharmProjects/pythonCourse/Dia 14/project/photos/image_a.jpg"

juan = Face('Juan', 'Gonzalez', photo)

print(juan.name)



