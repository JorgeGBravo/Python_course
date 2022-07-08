from cv2 import cv2
import face_recognition as fr

# upload images
photo_control = fr.load_image_file('image_b.jpg')
photo_test = fr.load_image_file('image_c.png')

# translate photo to rgb
photo_control = cv2.cvtColor(photo_control, cv2.COLOR_BGR2RGB)
photo_test = cv2.cvtColor(photo_test, cv2.COLOR_BGR2RGB)

# find face-control
site_face_A = fr.face_locations(photo_control)[0]
codify_face_A = fr.face_encodings(photo_control)[0]

# find face-control
site_face_B = fr.face_locations(photo_test)[0]
codify_face_B = fr.face_encodings(photo_test)[0]

# see rectangles
cv2.rectangle(photo_control,
              (site_face_A[3], site_face_A[0]),
              (site_face_A[1], site_face_A[2]),
              (0, 255, 0),
              2)
cv2.rectangle(photo_test,
              (site_face_B[3], site_face_B[0]),
              (site_face_B[1], site_face_B[2]),
              (0, 255, 0),
              2)

# face comparison
result = fr.compare_faces([codify_face_A], codify_face_B)
print(result)

# view images
cv2.imshow('photo_control', photo_control)
cv2.imshow('photo_prueba', photo_test)

# keep program open
cv2.waitKey(0)
