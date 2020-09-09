from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.template import loader

from django.contrib.auth.models import User


def IndexView(request):
    template = loader.get_template('user/index.html')
    return HttpResponse(template.render({}, request))


class DetailView(generic.DetailView):
    model = User
    template_name = 'user/detail.html'
