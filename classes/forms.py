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
