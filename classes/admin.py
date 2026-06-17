from django.contrib import admin
from classes.models import Chef, Ingredient, Cuisine, CookingClass

admin.site.register(Chef)
admin.site.register(Cuisine)
admin.site.register(Ingredient)
admin.site.register(CookingClass)
