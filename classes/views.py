from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

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

class ChefListView(LoginRequiredMixin, generic.ListView):
    model = Chef
    context_object_name = "chef-list"
    paginate_by = 5


class ChefDetailView(LoginRequiredMixin, generic.DetailView):
    model = Chef
    template_name = "classes/chef_detail.html"


class CuisineListView(LoginRequiredMixin, generic.ListView):
    model = Cuisine
    context_object_name = "cuisine-list"
    paginate_by = 5


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient-list"
    paginate_by = 5


class CookingClassListView(LoginRequiredMixin, generic.ListView):
    model = CookingClass
    queryset = CookingClass.objects.select_related("cuisine", "chef")
    context_object_name = "cooking-class-list"
    paginate_by = 5


class CookingClassDetailView(LoginRequiredMixin, generic.DetailView):
    model = CookingClass
    template_name = "classes/cooking_class_detail.html"
    queryset = CookingClass.objects.select_related("cuisine").prefetch_related("ingredients")
