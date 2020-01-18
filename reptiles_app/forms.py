from django import forms
from .models import Reptile

#depends on a model = 2 eme type dependant de bdd
class ReptileModelForm(forms.ModelForm):
    class Meta:
        model=Reptile
        fields = ("nom","nomEspece","ordre","age","poids","user")

    