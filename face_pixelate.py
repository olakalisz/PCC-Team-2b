import numpy as np
import cv2


def blur_face_video(filename):
    cap = cv2.VideoCapture(filename)
    while True:
        ret, frame = cap.read()

        frame = blur_face_image(frame)

        cv2.imshow('frame', frame)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return


def blur_face_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        blur_roi = frame[y:y + h, x:x + w]
        frame[y:y + h, x:x + w] = pixelate(blur_roi)
    return frame


def pixelate(frame):
    height, width, channels = frame.shape

    frame = cv2.resize(frame, (width // 32, height // 32), interpolation=cv2.INTER_NEAREST)
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_NEAREST)
    return frame


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

blur_face_video(0)

