from django.core.management.base import BaseCommand
import random
import string

from tags.models import Tag

class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        #i = 0
        #n = int(args[0])

        allTags = ['java', 'c++', 'incapsulation', 'programming', 'python',
                   'django', 'web', 'tags', 'questions', 'users', 'heap', 'ask']
        allTags.
        #for tagname in allTags:
        for i in range(len(allTags)):
            t = Tag(tag=allTags[i])
            t.save()


        #while i < n:
            #token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            #                for x in range(10))
            #i = i+1
            #t = Tag(tag=token)
            #t.save()
