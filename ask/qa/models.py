from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name='author_set')
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
