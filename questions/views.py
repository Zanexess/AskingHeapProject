from django.core.context_processors import csrf
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import auth
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from questions.forms import CommentForm, AskQuestion

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from questions.models import Question, Answer
from tags.models import Tag
from likes.models import LikeToQuestion, LikeToAnswer

# Create your views here.

class AskView(TemplateView):
    template_name = "ask.html"

class QuestionView(TemplateView):
    template_name = "question.html"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('date')[:5]

def question(request, question_id):
    q = Question.objects.all()[int(question_id)]

    aq = Answer.objects.all()



    j = 0
    for i in range(0, aq.count()):
        if (aq[i].answers_question.id == (int(question_id) + 1)):
            j=j+1



    tag1 = "bbb"
    tag2 = "ccc"
    return render(request, 'question_render.html', {
            'maintitle': q.title,
            'maintext': q.text,
            'mainlikes': q.rate,
            'mainauthor': q.author,
            'tag1': tag1,
            'tag2': tag2,
            'question_id': question_id,
        })


def questionsBest(request, objects_num=5):
    queryset = Question.objects.all().order_by('-rate')[:objects_num]
    context = {
        "queryset": queryset,
    }
    return render(request, 'best.html', context)

def questionsLast(request, objects_num=5):
    queryset = Question.objects.all().order_by('-date')[:objects_num]
    context = {
        "queryset": queryset,
    }
    return render(request, 'last.html', context)

def questionsTag(request):
    tag = request.GET.get('tag')
    queryset = Question.objects.all().filter(tags__tag=tag)
    context = {
        "queryset": queryset,
    }
    return render(request, 'tags.html', context)

def questionsFeed(request):
    queryset = Question.objects.all().order_by('-date')[:10]
    context = {
        "queryset": queryset,
    }
    return render(request, 'feed.html', context)

def questionsGet(request, question_id):
    queryset = Question.objects.all().filter(id=question_id)
    comment_form = CommentForm
    context = {
        "queryset": queryset,
        "form" : comment_form,
    }
    return render(request, 'question_render.html', context)






def ask(request):
    ask_form = AskQuestion(request.POST or None)
    args = {}
    args['form'] = ask_form
    if request.POST and ask_form.is_valid():
        question = Question(text=ask_form.cleaned_data['text'], title=ask_form.cleaned_data['title'])
        tags = ask_form.cleaned_data['tags']

        g = Tag.objects.all()
        getTag = tags.split(', ')

        for tag in getTag:
            counter = 0
            for l in g:
                if l.tag == tag:
                    counter += 1
            if counter == 0:
                t = Tag(tag=tag)
                t.save()


        user = auth.get_user(request)
        question.author = user

        question.save()
        a = g.filter(tag__in=getTag)
        question.tags.add(*a)
        return redirect('questionGet', question_id=question.id)

    else:
        return render(request, 'ask.html', args)




def comment(request, id):
    comment_form = CommentForm(request.POST or None)
    args = {}
    args['form'] = comment_form

    if request.POST and comment_form.is_valid():
        user = auth.get_user(request)
        a = Question.objects.all().filter(id=id)

        answer = Answer(text=comment_form.cleaned_data['text'])
        answer.author = user
        answer.answers_question=a[0]
        answer.save()

        # sending mail
        str = "User " + user.username + " answer your question " + a[0].title + "\n" + \
                  "Text: " + answer.text
        send_mail('New Comment!', str, 'askingheapproject@gmail.com', [a[0].author.email], fail_silently=False)

        # return redirect('questionGet' + '#text', question_id=a[0].id)
        return redirect('/question/get/%s#text' % id)
    else:
        return redirect('/question/get/%s#text' % id)
    return render(request, 'question_render.html', args)


def likeQuestion(request, id):
    args = {}
    args.update(csrf(request))
    if request.POST:
        if 'like' in request.POST:
            q = Question.objects.get(id=id)
            user = auth.get_user(request)
            if q.author != user:
                f = LikeToQuestion.objects.all().filter(like_author=user).filter(to_question=q)
                if not f.exists():
                    l = LikeToQuestion(like_author=user, to_question=q, value=1)
                    l.save()
                    q.rate += 1
                    q.save()
                else:
                    args['danger'] = "You already like or dislike it"
            else:
                args['danger'] = "You cannot like yourself"
        elif 'dislike' in request.POST:
            q = Question.objects.get(id=id)
            user = auth.get_user(request)
            if q.author != user:
                f = LikeToQuestion.objects.all().filter(like_author=user).filter(to_question=q)
                if not f.exists():
                    l = LikeToQuestion(like_author=user, to_question=q, value=-1)
                    l.save()
                    q.rate -= 1
                    q.save()
                else:
                    args['danger'] = "You already dislike or like it"
            else:
                args['danger'] = "You cannot dislike yourself"
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))

def likeAnswer(request, id):
    args = {}
    args.update(csrf(request))
    if request.POST:
        if 'like' in request.POST:
            a = Answer.objects.get(id=id)
            user = auth.get_user(request)
            if a.author != user:
                f = LikeToAnswer.objects.all().filter(like_author=user).filter(to_answer=a)
                if not f.exists():
                    l = LikeToAnswer(like_author=user, to_answer=a, value=1)
                    l.save()
                    a.rate += 1
                    a.save()
                else:
                    args['danger'] = "You already like or dislike it"
            else:
                args['danger'] = "You cannot like yourself"
        elif 'dislike' in request.POST:
            a = Answer.objects.get(id=id)
            user = auth.get_user(request)
            if a.author != user:
                f = LikeToAnswer.objects.all().filter(like_author=user).filter(to_answer=a)
                if not f.exists():
                    l = LikeToAnswer(like_author=user, to_answer=a, value=-1)
                    l.save()
                    a.rate -= 1
                    a.save()
                else:
                    args['danger'] = "You already like or dislike it"
            else:
                args['danger'] = "You cannot like yourself"
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


def rightAnswer(request, id):
    args = {}
    args.update(csrf(request))
    if request.POST:
        a = Answer.objects.get(id=id)
        q = a.answers_question
        l = q.answers_questions.all()
        user = auth.get_user(request)

        if user == q.author:
            for answer in l:
                if answer.right == True:
                    answer.right = False
                    answer.save()

            a.right = True
            a.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            args['danger'] = "You are not author of the question"
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))



# def ask(request):
#     args = {}
#     args.update(csrf(request))
#     if request.POST:
#         title = request.POST.get('title', '')
#         text = request.POST.get('text', '')
#         tags = request.POST.get('tags', '')
#
#         if tags == "":
#             args['danger'] = "At least 1 tag required"
#             return render(request, 'ask.html', args)
#
#         g = Tag.objects.all()
#         getTag = tags.split(', ')
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
#
#         if len(getTag) > 3:
#             args['danger'] = "3 tags max"
#             return render(request, 'ask.html', args)
#
#
#         user = auth.get_user(request)
#         if (title != "") and (text != ""):
#             q = Question(title=title, text=text, author=user)
#             q.save()
#             a = g.filter(tag__in=getTag)
#             q.tags.add(*a)
#
#             return redirect("/")
#         else:
#             args['danger'] = "Required fields are empty"
#             return render(request, 'ask.html', args)
#     else:
#         return render(request, 'ask.html', args)
