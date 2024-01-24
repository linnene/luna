from fastapi import APIRouter, Depends, Body,UploadFile,File
from tortoise.contrib.pydantic.creator import pydantic_model_creator
import os

from ....models.invitation import invi_img

target_folder = ''


invitation = APIRouter(tags=["帖子相关"])

#图片写入——————————————————————————————————————————————————————————————————————————————

FileModelPydantic = pydantic_model_creator(invi_img)

@invitation.post("/put_img")
async def put_invi_img(file: UploadFile = File(... ,media_type="image/png")):

    file_path = os.path.join(target_folder, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    file_model = await invi_img.create(filename=file.filename, filepath=file_path)

    return await FileModelPydantic.from_tortoise_orm(file_model)

#——————————————————————————————————————————————————————————————————————————————————————






#測試用
@invitation.get("/")
async def invitation_text(yua:int):
    return{"yua":yua}
