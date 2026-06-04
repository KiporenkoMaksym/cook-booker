from django import forms
from django.core.exceptions import ValidationError

from classes.models import Ingredient, CookingClass, Chef


class ProfessionalRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter first name"}),
        required=True
    )

    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter last name"}),
        required=True
    )

    years_of_experience = forms.IntegerField(
        label="Years of experience",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter years of experience"}),
        required=True
    )

    class Meta:
        model = Chef
        fields = ["username", "first_name", "last_name", "password", "years_of_experience"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def clean_years_of_experience(self):
        experience_val = self.cleaned_data.get("years_of_experience")

        if experience_val is None:
            raise ValidationError("Please indicate your work experience.")

        experience = int(experience_val)

        if experience < 1:
            raise ValidationError(
                "Registration rejected."
                "Our courses are designed specifically "
                "for chefs with 1 year of experience to improve their skills.")
        return experience


class ChefUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    years_of_experience = forms.IntegerField(
        label="Years of experience",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=True
    )

    class Meta:
        model = Chef
        fields = ["username", "first_name", "last_name", "years_of_experience"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_years_of_experience(self):
        experience_val = self.cleaned_data.get("years_of_experience")
        if experience_val is None:
            raise ValidationError("Please indicate your work experience.")
        if int(experience_val) < 1:
            raise ValidationError("Minimum 1 year of experience required.")
        return experience_val


class CookingClassForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Ingredients"
    )

    class Meta:
        model = CookingClass
        fields = "__all__"


class CookingClassSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label = "",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search by title",
            }
        )
    )


class ChefSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label = "",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search by username",
            }
        )
    )