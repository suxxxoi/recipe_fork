from django.contrib import admin

from .models import Recipe, IngredientList, Ingredient

admin.site.register(Recipe)
admin.site.register(IngredientList)
admin.site.register(Ingredient)
