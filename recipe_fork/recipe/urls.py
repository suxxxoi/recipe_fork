from django.urls import path

from . import views

app_name = 'recipe'
urlpatterns = [
    #path('/u/recipe/', views.DetailView.as_view(), name='detail'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='recipe')
]
