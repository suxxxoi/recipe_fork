from django.urls import include, path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='user'),
    path('<int:user_pk>/r/', include('recipe.urls'), name='recipe'),
]