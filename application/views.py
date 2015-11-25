# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = "base.html"

class IndexView(TemplateView):
    template_name = "feed.html"
