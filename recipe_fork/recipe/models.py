from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200, default='Title')
    recipe_text = models.TextField()
    description = models.TextField(default='')

    def __str__(self):
        return self.recipe_text


class IngredientList(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_list_title = models.CharField(max_length=100, default='Zutaten')

    def __str__(self):
        return self.ingredient_list_title


class Ingredient(models.Model):
    ingredientList = models.ForeignKey(IngredientList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    amount = models.FloatField(default=0)
    unit = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name
