from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Recipe, IngredientList, Ingredient
from django.contrib.auth.models import User


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


def new_recipe(request, user_pk):
    username = User.objects.get(pk=user_pk).username
    context = {'user_pk': user_pk,
               'user_name': username}
    return render(request, 'recipe/new.html', context)


def save_new_recipe(request):
    new_r = Recipe(
        author=User(pk=request.POST['user_pk']),
        title=request.POST['title'],
        recipe_text=request.POST['recipe_text'],
        description=request.POST['description_text'],
        portions=float(request.POST['portions']),
        )
    new_r.save()
    ingredient_list_titles = [name for name in request.POST.keys() if name.startswith('ingredient_list_')]
    print(ingredient_list_titles)
    for i, ingredient_list in enumerate(ingredient_list_titles):
        ingredient_var_names = [i_name for i_name in request.POST.keys() if i_name.startswith('ingredient_name_' + str(i))]
        # check whether the ingredient list is empty
        ingredient_not_empty = False
        for i_name in ingredient_var_names:
            if request.POST[i_name] != '':
                ingredient_not_empty = True
                break
        if ingredient_not_empty:
            # make a new ingredient list
            i_list = IngredientList(ingredient_list_title=request.POST[ingredient_list], recipe=new_r)
            i_list.save()
            for j, i_name in enumerate(ingredient_var_names):
                if request.POST[i_name] != '':
                    ing = Ingredient(
                            ingredientList=i_list,
                            name=request.POST['ingredient_name_' + str(i) + '_' + str(j)],
                            amount=float(request.POST['ingredient_amount_' + str(i) + '_' + str(j)]),
                            unit=request.POST['ingredient_unit_' + str(i) + '_' + str(j)],
                        )
                    print(request.POST[i_name])
                    ing.save()

    return HttpResponseRedirect(reverse('recipe:recipe', args=(new_r.id,)))
