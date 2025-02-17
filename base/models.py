from django.db import models
from users.models import User


class Author(User):
    bio = models.TextField()
    followers = models.ManyToManyField(User , related_name='following')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


