from cv2 import cv2
import face_recognition as fr

# upload images
photo_control = fr.load_image_file('image_b.jpg')
photo_test = fr.load_image_file('image_a.jpg')

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
tolerance = 0.6  # default tolerance 0.6
result = fr.compare_faces([codify_face_A], codify_face_B, tolerance)

# distance measurements
distance = fr.face_distance([codify_face_A], codify_face_B)

# view results
cv2.putText(photo_control,
            f'{result} {distance.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),  # this data can be modified by representing a color depending on the result
            2)

# view images
cv2.imshow('photo_control', photo_control)
cv2.imshow('photo_prueba', photo_test)

# keep program open
cv2.waitKey(0)
