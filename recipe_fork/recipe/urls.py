from django.urls import path

from . import views

app_name = 'recipe'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='recipe'),
    path('new/<int:pk>/', views.NewView.as_view(), name='new'),
    path('new/', views.save_new_recipe, name='new'),
]
