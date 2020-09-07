import face_recognition
import json
import cv2
import uuid
import os
from urllib.request import urlretrieve
urlretrieve(link, "路径"+"文件名")

image_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1599077317159&di=050657edd5117283d9a2530b483d0a1d&imgtype=0&src=http%3A%2F%2Fimg.ewebweb.com%2Fuploads%2F20200218%2F18%2F1582020747-DIEYgQkZWs.jpeg"

image = face_recognition.load_image_file(image_url)
point_list = face_recognition.face_locations(image)
img = cv2.imread(image_url)
i = 1
for point in point_list:
    cropped = img[ point[0]:point[2], point[3]:point[1]] 
    cv2.imwrite("./face_data/" + str(uuid.uuid1()) + ".jpg", cropped)
    break
