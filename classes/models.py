from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


class Chef(AbstractUser):
    years_of_experience = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "chef"
        verbose_name_plural = "chefs"

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}".strip()


class Cuisine(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    is_allergen = models.BooleanField(default=False)

    class Meta:
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"
        ordering = ["name"]

    def __str__(self):
        suffix = " (Allergen)" if self.is_allergen else ""
        return f"{self.name}{suffix}"


class CookingClass(models.Model):
    title = models.CharField(max_length=255, unique=True)
    preparation_time = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name="cooking_classes")
    ingredients = models.ManyToManyField(Ingredient, related_name="cooking_classes")
    chefs = models.ManyToManyField(Chef, related_name="cooking_classes")
    students = models.ManyToManyField(Chef, related_name="joined_classes", blank=True)

    class Meta:
        verbose_name_plural = "cooking classes"
        ordering = ["title"]

    def __str__(self):
        return self.title
