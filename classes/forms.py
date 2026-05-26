from django import forms

from classes.models import Ingredient, CookingClass


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