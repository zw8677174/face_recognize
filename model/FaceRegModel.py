from peewee import *
from model.DBconfig import DatabaseConfig


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = DatabaseConfig.get_zpc_base()


class FacePics(BaseModel):
    create_at = IntegerField(null=True)
    image_url = CharField(null=True)
    points = CharField(null=True)

    class Meta:
        table_name = 'face_pics'


class FaceReg(BaseModel):
    def_1 = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'face_reg'


class ImageUrl(BaseModel):
    create_at = IntegerField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'image_url'
