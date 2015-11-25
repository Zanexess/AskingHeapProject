from django.core.management.base import BaseCommand
import random
import string

from userprofile.models import UserProfile
from django.contrib.auth.models import User
from userprofile.models import UserProfile

class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        i = 0
        n = int(args[0])
        while i < n:
            userNumber = random.randint(1, 20)
            token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                            for x in range(userNumber))
            email = token + "@" + "mail.ru"
            i = i+1
            rate = random.randint(-100, 100)
            user = UserProfile.objects.create_user(token, email, token, token, token, rate, '1111')
            user.save()
