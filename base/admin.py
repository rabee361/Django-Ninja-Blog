from django.contrib import admin
from .models import Author , Post , User, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
