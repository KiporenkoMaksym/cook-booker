from django.shortcuts import render

from classes.models import Chef, Ingredient, Cuisine, CookingClass


def index(request):

    num_chefs = Chef.objects.count()
    num_cuisines = Cuisine.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_cooking_classes = CookingClass.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_chefs": num_chefs,
        "num_cuisines": num_cuisines,
        "num_ingredients": num_ingredients,
        "num_cooking_classes": num_cooking_classes,
        "num_visits": num_visits + 1,
    }

    return render (request, "classes/index.html", context)
