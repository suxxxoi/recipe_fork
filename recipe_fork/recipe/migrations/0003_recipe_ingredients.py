# Generated by Django 3.0.8 on 2020-08-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=''),
        ),
    ]