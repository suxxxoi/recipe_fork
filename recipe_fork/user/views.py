from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Index Site User.")


class DetailView(generic.DetailView):
    model = User
    template_name = 'user/detail.html'
