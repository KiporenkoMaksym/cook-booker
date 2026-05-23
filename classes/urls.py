from django.urls import path

from classes.views import (
    index,
    ChefListView,
    CuisineListView,
    IngredientListView,
    CookingClassListView,
    ChefDetailView,
    CookingClassDetailView,
    CuisineDetailView,
    ChefCreateView,
    ChefUpdateView,
    ChefDeleteView,
    CuisineCreateView,
    CuisineUpdateView,
    CuisineDeleteView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("chefs/", ChefListView.as_view(), name="chef-list"),
    path("chefs/create/", ChefCreateView.as_view(), name="chef-create"),
    path("chefs/<int:pk>/update/", ChefUpdateView.as_view(), name="chef-update"),
    path("chefs/<int:pk>/delete/", ChefDeleteView.as_view(), name="chef-delete"),
    path("chefs/<int:pk>/", ChefDetailView.as_view(), name="chef-detail"),
    path("cuisines/", CuisineListView.as_view(), name="cuisine-list"),
    path("cuisines/<int:pk>/", CuisineDetailView.as_view(), name="cuisine-detail"),
    path("cuisines/create/", CuisineCreateView.as_view(), name="cuisine-create"),
    path("cuisines/<int:pk>/update/", CuisineUpdateView.as_view(), name="cuisine-update"),
    path("cuisines/<int:pk>/delete/", CuisineDeleteView.as_view(), name="cuisine-delete"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete", IngredientDeleteView.as_view(), name="ingredient-delete"),
    path("cooking_classes", CookingClassListView.as_view(), name="cooking-classes-list"),
    path("cooking_classes/<int:pk>/", CookingClassDetailView.as_view(), name="cooking-classes-detail")
]

app_name = "classes"
