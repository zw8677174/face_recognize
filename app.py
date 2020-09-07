from flask import Flask, request

from services import FacePointService
from utils import Response
from model import ZpcDBconfig


# app run
app = Flask(__name__)

# connect database
ZpcDBconfig.database.connect()

# import
@app.route('/save_pic')
def save_pic():
    image_url = request.args.get("image_url")
    FacePointService().save(image_url)
    return Response().success(image_url)

