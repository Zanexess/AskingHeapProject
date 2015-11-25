from django.core.management.base import BaseCommand
import random
import string
from datetime import datetime
import urllib

from questions.models import Question, Answer
from likes.models import LikeToQuestion, LikeToAnswer

class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        all_questions = Question.objects.all()
        all_likes_to_questions = LikeToQuestion.objects.all()

        all_answers = Answer.objects.all()
        all_likes_to_answers = LikeToAnswer.objects.all()

        for question in all_questions:
            counter = 0
            for like in all_likes_to_questions:
                if like.to_question == question:
                    counter = counter + like.value
            question.rate = counter
            question.save()

        for answer in all_answers:
            counter = 0
            for like in all_likes_to_answers:
                if like.to_answer == answer:
                    counter = counter + like.value
            answer.rate = counter
            answer.save()
