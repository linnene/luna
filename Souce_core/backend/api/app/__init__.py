from fastapi import APIRouter
from .endpoints.user import user 
from .endpoints.invitation import invitation
 

app = APIRouter(tags=["初始化输入接口"])


app.include_router(user,prefix= "/user")
app.include_router(invitation,prefix= "/invitation")
# app.include_router(login,prefix= "/login")

