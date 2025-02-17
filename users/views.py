from django.shortcuts import render
from ninja import Router
from .schemas import UserSchema
from .models import User

users_router = Router()


@users_router.get("users/", response=list[UserSchema])
def users(request):
    users = User.objects.all()
    return users


@users_router.post("login/", response=UserSchema)
def login(request, payload: dict):
    return payload


@users_router.post("logout/")
def logout(request):
    return {"message": "Logged out"}


@users_router.post("signup/", response=UserSchema)
def signUp(request, payload: dict):
    return payload



