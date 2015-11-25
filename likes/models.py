# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from questions.models import Question, Answer
from userprofile.models import UserProfile

class LikeToQuestion(models.Model):
    class Meta:
        db_table = "likeToQuestion"

    like_author = models.ForeignKey(UserProfile, related_name="author_like_to_question")
    to_question = models.ForeignKey(Question, related_name="like_question")
    value = models.IntegerField(default=0)


class LikeToAnswer(models.Model):
    class Meta:
        db_table = "likeToAnswer"

    like_author = models.ForeignKey(UserProfile, related_name="author_like_to_answer")
    to_answer = models.ForeignKey(Answer, related_name="like_answer")
    value = models.IntegerField(default=0)

class LikeToUser(models.Model):
    class Meta:
        db_table = "likeToUser"

    like_author = models.ForeignKey(UserProfile, related_name="author_like_to_user")
    to_user = models.ForeignKey(UserProfile, related_name="like_user")
    value = models.IntegerField(default=0)
