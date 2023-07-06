from django import forms
from myapp.models import Cloth

class ClothAddForm(forms.ModelForm):
    class Meta:
        model=Cloth
        fields="__all__"