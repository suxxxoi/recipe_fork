from django.shortcuts import render
from django.views import generic

from django.contrib.auth.models import User


class UserIndexView(generic.ListView):
    template_name = 'user_index/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(username='admin')
