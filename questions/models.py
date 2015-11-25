# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag
from userprofile.models import UserProfile


class Question(models.Model):
    class Meta:
        db_table = "question"

    title = models.CharField(max_length=200)
    text = models.TextField(max_length=100000)
    rate = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag, related_name="tags_question")
    author = models.ForeignKey(UserProfile, related_name="author_question", null=True)

    def __unicode__(self):
        return self.title



class Answer(models.Model):
    class Meta:
        db_table = "answer"

    text = models.TextField(max_length=100000, default='')
    right = models.BooleanField(default=False)
    rate = models.IntegerField(default=0)

    answers_question = models.ForeignKey(Question, related_name="answers_questions")
    author = models.ForeignKey(UserProfile, related_name="author_answer", null=True)

    def __unicode__(self):
        return self.text[:15]