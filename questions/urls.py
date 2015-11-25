"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView

from views import question
from views import questionsBest
from views import questionsLast
from views import questionsTag
from views import questionsFeed
from views import questionsGet
from views import ask
from views import comment
from views import likeQuestion
from views import likeAnswer
from views import rightAnswer

# from questions.forms import AskQuestion

urlpatterns = [
    # url(r'^create/$', AskQuestion.as_view(), name='create'),
    url(r'^create/$', ask, name='create'),
    url(r'^feed/$', questionsFeed, name='feed'),
    url(r'^/get/$', TemplateView.as_view(template_name='question.html'), name='question'),
    url(r'^get/(?P<question_id>[0-9]+)/$', questionsGet, name='questionGet'),
    url(r'^best/(?P<objects_num>[0-9]+)/$', questionsBest, name='best'),
    url(r'^last/(?P<objects_num>[0-9]+)/$', questionsLast, name='last'),
    url(r'^tag/$', questionsTag, name='tag'),
    url(r'^newquestion/$', ask),
    url(r'^newcomment/(?P<id>[0-9]+)$', comment),
    url(r'^like/(?P<id>[0-9]+)$', likeQuestion),
    url(r'^likeA/(?P<id>[0-9]+)$', likeAnswer),
    url(r'^rightA/(?P<id>[0-9]+)$', rightAnswer),
    # url(r'^like/(?P<id>[0-9]+)$', likeQuestion),
]
