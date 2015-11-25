from django import forms
from django.views.generic.edit import CreateView
from django.contrib import admin
from models import Question
from django.contrib import auth
from django.core.urlresolvers import reverse
from questions.models import Question, Answer
from tags.models import Tag
from django.forms import ModelForm
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import forms, CharField, Textarea



# def validate_tags(value):
#         if value == "":
#             raise forms.ValidationError('At least 1 tag required')
#
#         g = Tag.objects.all()
#         getTag = value.split(', ')
#
#         if len(getTag) > 0:
#             for tag in getTag:
#                 counter = 0
#                 for l in g:
#                     if l.tag == tag:
#                         counter += 1
#                 if counter == 0:
#                     t = Tag(tag=tag)
#                     t.save()
#                     pass
#                 return getTag
#
#         if len(getTag) > 3:
#             raise forms.ValidationError('3 tags max')
#
#
# class QuestionForm(forms.ModelForm):
#     tags = forms.CharField(validators=[validate_tags])
#
#     class Meta:
#         model = Question
#         fields = 'title', 'text', 'tags'
#
#
# class AskQuestion(CreateView):
#     model = Question
#     form_class = QuestionForm
#     template_name = 'ask.html'
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super(AskQuestion, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse('home')


# class CommentForm(ModelForm):
#     class Meta:
#         model = Answer
#         fields = ['text']


class CommentForm(forms.Form):
    text = CharField(widget=Textarea)

    def clean_text(self):
        if len(self.cleaned_data['text']) < 1:
            raise ValidationError("Answer is empty!")
        if len(self.cleaned_data['text']) > 99999:
            raise ValidationError("Answer is long, sorry")
        return self.cleaned_data['text']

class AskQuestion(forms.Form):
    title = CharField()
    text = CharField(widget=Textarea)
    tags = CharField()

    def clean_title(self):
        if len(self.cleaned_data['title']) > 200:
            raise ValidationError("Title is long")
        return self.cleaned_data['title']

    def clean_text(self):
        if len(self.cleaned_data['text']) > 99999:
            raise ValidationError("Text is too long")
        return self.cleaned_data['text']

    def clean_tags(self):
        tags_list = self.cleaned_data['tags'].split(", ")
        if len(tags_list) > 3:
            raise ValidationError("Too many tags")
        for tag in tags_list:
            if len(tag) > 49:
                raise ValidationError("Tag should have 50 characters max")
        return self.cleaned_data['tags']