from django.test import TestCase
from classes.models import Chef, Ingredient, Cuisine
from classes.forms import (
    ProfessionalRegistrationForm,
    ChefUpdateForm,
    CookingClassForm,
    CookingClassSearchForm,
    ChefSearchForm,
    CuisineSearchForm
)


class TestProfessionalRegistrationForm(TestCase):

    def test_form_is_valid_with_good_data(self):
        form_data = {
            "username": "chef_ramsay",
            "first_name": "Gordon",
            "last_name": "Ramsay",
            "password": "secretpassword123",
            "years_of_experience": 5
        }
        form = ProfessionalRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_if_experience_less_than_one(self):
        form_data = {
            "username": "chef_novice",
            "first_name": "John",
            "last_name": "Doe",
            "password": "secretpassword123",
            "years_of_experience": 0
        }
        form = ProfessionalRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)
        self.assertEqual(
            form.errors["years_of_experience"][0],
            "Registration rejected."
            "Our courses are designed specifically for chefs with "
            "1 year of experience to improve their skills."
        )

    def test_required_fields(self):
        form = ProfessionalRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors)
        self.assertIn("last_name", form.errors)
        self.assertIn("years_of_experience", form.errors)


class TestChefUpdateForm(TestCase):

    def test_form_is_valid(self):
        form_data = {
            "username": "chef_updated",
            "first_name": "James",
            "last_name": "Oliver",
            "years_of_experience": 2
        }
        form = ChefUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_experience(self):
        form_data = {
            "username": "chef_updated",
            "first_name": "James",
            "last_name": "Oliver",
            "years_of_experience": 0
        }
        form = ChefUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["years_of_experience"][0],
                         "Minimum 1 year of experience required.")


class TestCookingClassForm(TestCase):

    def setUp(self):
        self.chef1 = Chef.objects.create(
            username="chef1",
            first_name="A",
            last_name="B",
            years_of_experience=3
        )
        self.chef2 = Chef.objects.create(
            username="chef2",
            first_name="C",
            last_name="D",
            years_of_experience=4
        )
        self.ingredient = Ingredient.objects.create(name="Tomato")
        self.cuisine_obj = Cuisine.objects.create(name="Italian")

    def test_form_is_valid_with_relations(self):
        form_data = {
            "title": "Italian Pasta Masterclass",
            "preparation_time": 60,
            "price": 45.50,
            "cuisine": self.cuisine_obj.pk,
            "ingredients": [self.ingredient.pk],
            "chefs": [self.chef1.pk],
            "students": [self.chef2.pk],
        }
        form = CookingClassForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_required_relations(self):
        form_data = {
            "title": "Italian Pasta Masterclass",
            "ingredients": [],
            "chefs": [],
        }
        form = CookingClassForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("ingredients", form.errors)
        self.assertIn("chefs", form.errors)


class TestSearchForms(TestCase):

    def test_cooking_class_search_form_valid(self):
        form = CookingClassSearchForm(data={"title": "Pasta"})
        self.assertTrue(form.is_valid())
        empty_form = CookingClassSearchForm(data={})
        self.assertTrue(empty_form.is_valid())

    def test_chef_search_form_valid(self):
        form = ChefSearchForm(data={"username": "ramsay"})
        self.assertTrue(form.is_valid())

    def test_cuisine_search_form_valid(self):
        form = CuisineSearchForm(data={"cuisine": "French"})
        self.assertTrue(form.is_valid())
