from fastapi import FastAPI
from .app import app
#___________________________________________#

#中间件
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

#___________________________________________#

all = FastAPI()


all.include_router(app,prefix="/app")