from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

from classes.models import Chef, Ingredient, Cuisine, CookingClass

@login_required
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
    context_object_name = "chef_list"
    paginate_by = 5


class ChefDetailView(LoginRequiredMixin, generic.DetailView):
    model = Chef
    template_name = "classes/chef_detail.html"


class ChefCreateView(LoginRequiredMixin, generic.CreateView):
    model = Chef
    fields = "__all__"
    success_url = reverse_lazy("classes:chef-list")


class ChefUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Chef
    fields = "__all__"
    success_url = reverse_lazy("classes:chef-list")


class ChefDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Chef
    success_url = reverse_lazy("classes:chef-list")


class CuisineListView(LoginRequiredMixin, generic.ListView):
    model = Cuisine
    context_object_name = "cuisine_list"
    paginate_by = 5


class CuisineDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cuisine
    template_name = "classes/cuisine_detail.html"


class CuisineCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cuisine
    fields = "__all__"
    success_url = reverse_lazy("classes:cuisine-list")


class CuisineUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cuisine
    fields = "__all__"
    success_url = reverse_lazy("classes:cuisine-list")


class CuisineDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cuisine
    success_url = reverse_lazy("classes:cuisine-list")

class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    paginate_by = 10


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("classes:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("classes:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("classes:ingredient-list")


class CookingClassListView(LoginRequiredMixin, generic.ListView):
    model = CookingClass
    queryset = CookingClass.objects.select_related("cuisine")
    context_object_name = "cooking_class"
    paginate_by = 5


class CookingClassDetailView(LoginRequiredMixin, generic.DetailView):
    model = CookingClass
    template_name = "classes/cooking_class_detail.html"
    context_object_name = "cooking_class"
    queryset = CookingClass.objects.select_related("cuisine").prefetch_related("ingredients")
