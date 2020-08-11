from django.urls import path

from . import views

app_name = 'recipe'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='recipe'),
    path('new/', views.new_recipe, name='new'),
    path('save_new/', views.save_new_recipe, name='save_new'),
]
