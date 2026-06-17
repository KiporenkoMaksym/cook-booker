from django.test import TestCase

from classes.models import (Chef,
                            Ingredient,
                            Cuisine,
                            CookingClass
)


class ChefModelTest(TestCase):
    def test_chef_str(self):
        chef = Chef.objects.create_user(
            username="bond",
            first_name="James",
            last_name="Bond",
            password="12345"
        )

        self.assertEqual(str(chef), "bond James Bond")


class CuisineModelTest(TestCase):
    def test_cuisine_str(self):
        cuisine = Cuisine.objects.create(name="Italian")

        self.assertEqual(str(cuisine), "Italian")


class IngredientModelTest(TestCase):
    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(
            name="Tomato",
            is_allergen=False
        )

        self.assertEqual(str(ingredient), "Tomato")


class CookingClassModelTest(TestCase):
    def test_cooking_class_str(self):
        cuisine = Cuisine.objects.create(name="Italian")

        cooking_class = CookingClass.objects.create(
            title="Pasta",
            preparation_time=25,
            price=12.00,
            cuisine=cuisine
        )

        self.assertEqual(str(cooking_class), "Pasta")
