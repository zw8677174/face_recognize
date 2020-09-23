from flask import Flask, request
from services import FacePointService
from utils import Response
from model import DBconfig

# init
app = Flask(__name__)
log = app.logger
DBconfig.DatabaseConfig.get_zpc_base().connect()


@app.route('/save_pic')
def save_pic():
    image_url = request.args.get("image_url")
    FacePointService().save(image_url)
    return Response().success(image_url)


app.run(debug=True)
