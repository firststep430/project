from django.contrib import admin
from .models import Users, Ingredients, Recipes

admin.site.register(Users)
admin.site.register(Ingredients)
admin.site.register(Recipes)