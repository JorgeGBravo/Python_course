from cv2 import cv2
import face_recognition as fr


def encode(image):
    return fr.face_encodings(image)


def translate_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def put_text_image(photo_rgb):
    tolerance = 0.6  # default tolerance 0.6
    result = fr.compare_faces([codify_face_A], codify_face_B, tolerance)

    # distance measurements
    distance = fr.face_distance([codify_face_A], codify_face_B)
    cv2.putText(photo_rgb,
                f'{result} {distance.round(2)}',
                (50, 50),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                2)