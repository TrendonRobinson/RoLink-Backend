from django.db import models

# Create your models here.


class UserPost(models.Model):
    post_content = models.CharField(max_length=200)


class Game(models.Model):
    test_text = models.CharField(max_length=200)
