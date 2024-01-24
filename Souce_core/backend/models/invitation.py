from typing import Optional, Iterable

from tortoise import models, BaseDBAsyncClient
from tortoise import fields



class invitation(models.Model):
    author = fields.ForeignKeyField("User.User",related_name="your_invitation")
    #记录发帖时间
    release_time = fields.DatetimeField(auto_now_add=True)





class invi_img(models.Model):
    id = fields.IntField(pk=True)
    filename = fields.CharField(max_length=255)
    filepath = fields.CharField(max_length=255)

    class Meta:
        table = 'files'
