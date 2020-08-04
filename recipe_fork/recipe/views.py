from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import generic

# Create your views here.

from .models import Recipe


def index(request):
    return HttpResponse("Index Site.")


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/detail.html'
    # try:
    #     recipe = Recipe.objects.get(pk=recipe_id)
    # except Recipe.DoesNotExist:
    #     raise Http404("Recipe does not exist")
    # return render(recipe, 'recipe/detail.html', {'recipe': recipe})
