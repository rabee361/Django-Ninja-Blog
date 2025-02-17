from ninja import Schema
from .models import User

class UserSchema(Schema):
    class Meta:
        model = User
        fields = ["id", "username", "email"]    


class LoginSchema(Schema):
    username: str
    password: str

