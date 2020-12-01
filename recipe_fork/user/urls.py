from django.urls import include, path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.IndexView, name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='user'),
    path('<int:pk>/', views.detail, name='user'),
    path('<int:user_pk>/r/', include('recipe.urls'), name='recipe'),
]
