from ninja import Schema
from .models import Author , User , Post , Comment  



class AuthorSchema(Schema):
    class Meta:
        model = Author
        fields = ["id"]


class UserSchema(Schema):
    class Meta:
        model = User
        fields = ["id", "username", "email"]



class PostSchema(Schema):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "author"]


class CommentSchema(Schema):
    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "post"]

