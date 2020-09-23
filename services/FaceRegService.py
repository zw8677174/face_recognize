import face_recognition
import cv2
from model.FaceRegModel import ImageUrl

class FacePointService:

    @staticmethod
    def save(image_url):
        # Log.debug(image_url)
        ImageUrl.create()
        pass
        # image = face_recognition.load_image_file(image_url)
        # point_list = face_recognition.face_locations(image)
        # img = cv2.imread(image_url)
        # for point in point_list:
        #     cropped = img[point[0]:point[2], point[3]:point[1]]
        #     cv2.imwrite("./out.jpg", cropped)
        #     break

    def _save_face_points(self, points, pic_url):
        pass


class SimilarFaceService:
    def get_one(self):
        pass
