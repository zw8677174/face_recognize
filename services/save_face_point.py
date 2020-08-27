import face_recognition
import json
import cv2

class save_face_point_sevice:

    def save():
        image_url = "test.jpg"

        image = face_recognition.load_image_file(image_url)
        point_list = face_recognition.face_locations(image)
        img = cv2.imread(image_url)
        i = 1
        for point in point_list:
            cropped = img[ point[0]:point[2], point[3]:point[1]] 
            cv2.imwrite("./out.jpg", cropped)
            break

    def _save_face_points(points, picUrl):
        
