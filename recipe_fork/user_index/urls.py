from django.urls import path

from . import views

app_name = 'user_index'
urlpatterns = [
    path('', views.UserIndexView.as_view(), name='index'),
]
