from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from classes.models import (Chef,
                            Cuisine,
                            Ingredient,
                            CookingClass
)

User = get_user_model()

class LoginLogoutViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test12345"
        )

    def test_login_required(self):
        response = self.client.get(
            reverse("classes:chef-list")
        )

        self.assertNotEqual(response.status_code, 200)

    def test_logged_in_user_access(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("classes:chef-list"))

        self.assertEqual(response.status_code, 200)


class HomePageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test12345"
        )

    def test_index_view(self):
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("classes:index")
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn("num_chefs", response.context)
        self.assertIn("num_cuisines", response.context)
        self.assertIn("num_ingredients", response.context)
        self.assertIn("num_cooking_classes", response.context)


class StudentAssignmentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test12345"
        )

        self.client.force_login(self.user)

    def test_assign_student_to_class(self):
        cuisine = Cuisine.objects.create(name="Italian")

        cooking_class = CookingClass.objects.create(
            title="Pizza",
            preparation_time=20,
            price=10,
            cuisine=cuisine
        )

        self.client.post(
            reverse(
                "classes:cooking-classes-toggle-assign",
                args=[cooking_class.id]
            )
        )

        cooking_class.refresh_from_db()

        self.assertIn(
            self.user,
            cooking_class.students.all()
        )

    def test_unassign_student_from_class(self):
        cuisine = Cuisine.objects.create(name="Italian")

        cooking_class = CookingClass.objects.create(
            title="Pizza",
            preparation_time=20,
            price=10,
            cuisine=cuisine
        )

        cooking_class.students.add(self.user)

        self.client.post(
            reverse(
                "classes:cooking-classes-toggle-assign",
                args=[cooking_class.id]
            )
        )

        cooking_class.refresh_from_db()

        self.assertNotIn(
            self.user,
            cooking_class.students.all()
        )


class ChefViewTest(TestCase):
    def setUp(self):
        self.user = Chef.objects.create_user(
            username="test",
            password="test12345"
        )

        self.client.force_login(self.user)

    def test_chef_list_view(self):
        response = self.client.get(
            reverse("classes:chef-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "classes/chef_list.html"
        )

    def test_login_required_for_chef_list(self):
        self.client.logout()

        response = self.client.get(
            reverse("classes:chef-list")
        )

        self.assertEqual(response.status_code, 302)

    def test_chef_detail_view(self):
        chef = Chef.objects.create_user(
            username="john",
            password="12345"
        )

        self.client.login(
            username="test",
            password="test12345"
        )

        response = self.client.get(
            reverse("classes:chef-detail", args=[chef.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["chef"], chef)

    def test_search_chef(self):
        Chef.objects.create_user(
            username="john",
            password="12345"
        )

        Chef.objects.create_user(
            username="max",
            password="12345"
        )

        self.client.login(
            username="test",
            password="test12345"
        )

        response = self.client.get(
            reverse("classes:chef-list"),
            {"username": "john"}
        )

        self.assertContains(response, "john")
        self.assertEqual(
            len(response.context["chef_list"]),
            1
        )


class CuisineViewTests(TestCase):
    def setUp(self):
        self.user = Chef.objects.create_user(
            username="test",
            password="test12345"
        )
        self.client.force_login(self.user)

    def test_cuisine_list_view(self):
        response = self.client.get(
            reverse("classes:cuisine-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "classes/cuisine_list.html"
        )

    def test_login_required_for_cuisine_list(self):
        self.client.logout()

        response = self.client.get(
            reverse("classes:cuisine-list")
        )

        self.assertEqual(response.status_code, 302)

    def test_cuisine_detail_view(self):
        cuisine = Cuisine.objects.create(name="Italian")

        response = self.client.get(
            reverse("classes:cuisine-detail", args=[cuisine.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["cuisine"], cuisine)
        self.assertContains(response, cuisine.name)

    def test_search_cuisine(self):
        Cuisine.objects.create(name="Italian")
        Cuisine.objects.create(name="French")

        self.client.login(
            username="test",
            password="test12345"
        )

        response = self.client.get(
            reverse("classes:cuisine-list"),
            {"cuisine": "Italian"}
        )

        self.assertContains(response, "Italian")
        self.assertNotContains(response, "French")


class IngredientViewTests(TestCase):
    def setUp(self):
        self.user = Chef.objects.create_user(
            username="test",
            password="test12345"
        )
        self.client.force_login(self.user)

    def test_ingredient_list_view(self):
        response = self.client.get(
            reverse("classes:ingredient-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "classes/ingredient_list.html"
        )

    def test_login_required_for_ingredient_list(self):
        self.client.logout()

        response = self.client.get(
            reverse("classes:ingredient-list")
        )

        self.assertEqual(response.status_code, 302)


class CookingClassViewTests(TestCase):
    def setUp(self):
        self.user = Chef.objects.create_user(
            username="test",
            password="test12345"
        )
        self.client.force_login(self.user)

    def test_cooking_class_list_view(self):
        response = self.client.get(
            reverse("classes:cooking-classes-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "classes/cookingclass_list.html"
        )

    def test_login_required_for_cooking_class_list(self):
        self.client.logout()

        response = self.client.get(
            reverse("classes:cooking-classes-list")
        )

        self.assertEqual(response.status_code, 302)

    def test_cooking_class_detail_view(self):
        cuisine = Cuisine.objects.create(name="Italian")

        cooking_class = CookingClass.objects.create(
            title="Pasta Master",
            preparation_time=25,
            price=12.00,
            cuisine=cuisine
        )

        response = self.client.get(
            reverse(
                "classes:cooking-classes-detail",
                args=[cooking_class.id]
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["cooking_class"],
            cooking_class
        )
        self.assertContains(response, cooking_class.title)

    def test_search_cooking_class(self):
        cuisine = Cuisine.objects.create(name="Italian")

        CookingClass.objects.create(
            title="Pizza",
            preparation_time=20,
            price=10,
            cuisine=cuisine
        )

        CookingClass.objects.create(
            title="Pasta",
            preparation_time=25,
            price=12,
            cuisine=cuisine
        )

        self.client.login(
            username="test",
            password="test12345"
        )

        response = self.client.get(
            reverse("classes:cooking-classes-list"),
            {"title": "Pizza"}
        )

        self.assertContains(response, "Pizza")
        self.assertNotContains(response, "Pasta")
