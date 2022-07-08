from cv2 import cv2
import face_recognition as fr

# upload images

photo_control = fr.load_image_file('image_a.jpg')
photo_test = fr.load_image_file('image_b.jpg')


photo_control = cv2.cvtColor(photo_control, cv2.COLOR_BGR2RGB)
photo_test = cv2.cvtColor(photo_test, cv2.COLOR_BGR2RGB)


cv2.imshow('photo_control', photo_control)
cv2.imshow('photo_prueba', photo_test)

cv2.waitKey()