from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="post_image", blank="true")
    author = models.ForeignKey(User, null="true", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    email = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE) 

    def __str__(self):
        return self.author   
