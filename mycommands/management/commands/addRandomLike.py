from django.core.management.base import BaseCommand
import random
import string

from questions.models import Question, Answer
from likes.models import LikeToQuestion, LikeToAnswer, LikeToUser
from userprofile.models import UserProfile

class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        all_users = UserProfile.objects.all()
        all_questions = Question.objects.all()
        all_answers = Answer.objects.all()

        for question in all_questions:
            for user in all_users:
                b = random.randint(0, 2)
                if b == 0:
                    likeToQuestion = LikeToQuestion(like_author=user, to_question=question, value=-1)
                    likeToQuestion.save()
                elif b == 2:
                    likeToQuestion = LikeToQuestion(like_author=user, to_question=question, value=1)
                    likeToQuestion.save()


        for answer in all_answers:
            for user in all_users:
                b = random.randint(0, 2)
                if b == 0:
                    likeToAnswer = LikeToAnswer(like_author=user, to_answer=answer, value=-1)
                    likeToAnswer.save()
                elif b == 2:
                    likeToAnswer = LikeToAnswer(like_author=user, to_answer=answer, value=1)
                    likeToAnswer.save()


        for user in all_users:
            for user1 in all_users:
                if user != user1:
                    b = random.randint(0, 2)
                    if b == 0:
                        likeToUser = LikeToUser(like_author=user, to_user=user1, value=-1)
                        likeToUser.save()
                    elif b == 2:
                        likeToUser = LikeToUser(like_author=user, to_user=user1, value=1)
                        likeToUser.save()
