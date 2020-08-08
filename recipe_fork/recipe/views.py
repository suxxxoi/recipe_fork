from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

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

class NewView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/new.html'

def save_new_recipe(request):
    print(request)
    new_r = Recipe(
        title=request.POST['title'],
        recipe_text=request.POST['recipe_text']
        )
    new_r.save()
    return HttpResponseRedirect(reverse('recipe:new', args = (new_r.id,)))
