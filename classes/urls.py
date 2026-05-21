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
)

urlpatterns = [
    path("", index, name="index"),
    path("chefs/", ChefListView.as_view(), name="chef-list"),
    path("chefs/create/", ChefCreateView.as_view(), name="chef-create"),
    path("chefs/<int:pk>/", ChefDetailView.as_view(), name="chef-detail"),
    path("cuisines/", CuisineListView.as_view(), name="cuisine-list"),
    path("cuisines/<int:pk>/", CuisineDetailView.as_view(), name="cuisine-detail"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("cooking_classes", CookingClassListView.as_view(), name="cooking-classes-list"),
    path("cooking_classes/<int:pk>/", CookingClassDetailView.as_view(), name="cooking-classes-detail")
]

app_name = "classes"
