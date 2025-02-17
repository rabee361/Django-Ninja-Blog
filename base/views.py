from django.shortcuts import render
from .models import Post , Author, Comment
from ninja import Router    
from ninja.security import HttpBearer
from .schemas import PostSchema, CommentSchema
from ninja.pagination import paginate
from ninja.security import django_auth

router = Router()   



class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "123":
            return token


def login(request, payload: dict, auth: AuthBearer):
    return payload


@router.get("posts/", response=list[PostSchema], auth=django_auth)
@paginate
def posts(request):
    posts = Post.objects.all()
    return posts


@router.get("posts/{id}", response=PostSchema)
def post(request, id: int):
    post = Post.objects.get(id=id)
    return post 


@router.post("posts/add", response=PostSchema)
def addPost(request, payload: PostSchema):
    post = Post.objects.create(**payload.dict())
    return post


@router.delete("posts/{id}/delete")
def removePost(request, id: int):
    post = Post.objects.get(id=id)
    post.delete()
    return {"message": "Post deleted"}


@router.get("posts/{id}/comments", response=list[CommentSchema])
def postComments(request, id: int):
    comments = Comment.objects.filter(post_id=id)
    return comments


@router.post("comments/add", response=CommentSchema)
def addComment(request, comment: CommentSchema):
    comment = Comment.objects.create(**comment.dict())
    return comment


@router.delete("posts/{id}/delete")
def deletePost(request, id: int):
    post = Post.objects.get(id=id)
    post.delete()
    return {"message": "Post deleted"}


@router.delete("comments/{id}/delete")
def deleteComment(request, id: int):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return {"message": "Comment deleted"}

# @api.get('/posts/{id}')
# def post(request):
#     return api.test(request)
