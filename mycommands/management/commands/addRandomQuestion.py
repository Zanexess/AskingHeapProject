from django.core.management.base import BaseCommand
import random
import string
from datetime import datetime
import urllib

from questions.models import Question, Answer
from tags.models import Tag
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib import auth

class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        i = 0
        k = 0
        n = int(args[0])
        allusers = UserProfile.objects.all()
        tags = Tag.objects.all()
        while i < n:
            titleNumber = random.randint(0, 50)
            textNumber = random.randint(0, 300)
            rate = random.randint(-100, 100)
            number = random.randint(0, 10)

            numberOfTags = random.randint(0, 5)
            tagsList = []
            for q in range(0, numberOfTags):
                randomTag = random.randint(0, len(tags)-1)
                tagsList.insert(q, tags[randomTag])

            title = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase +
                                          string.digits + string.whitespace)
                            for x in range(titleNumber))
            token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase +
                                          string.digits + string.whitespace)
                            for x in range(textNumber))
            i = i+1

            randomUserId = random.randint(0, len(allusers)-1)
            user = allusers[randomUserId]

            q = Question(title=title, text=token, rate=rate, author=user)
            q.save()
            q.tags.add(*tagsList)


            for j in range(0, number):
                randomUserId = random.randint(0, len(allusers) - 1)
                userComment = allusers[randomUserId]
                rateComment = random.randint(-100, 100)
                textComment = random.randint(0, 300)
                text = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase +
                                             string.digits + string.whitespace)
                            for x in range(textComment))
                k = k + 1
                a = Answer(k, text=text, rate=rateComment, answers_question=q, author=userComment)
                a.save()