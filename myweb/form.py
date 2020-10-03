from django.forms import ModelForm
from django import forms

from .models import Fruit,Farm

class addFarm(ModelForm):
    class Meta:
        model = Farm
        fields = ['Farm_Name']


class addFruit(ModelForm):
    class Meta:
        model = Fruit
        fields = ['Fruit_Name','Price','Season','FarmName']


searchchoices = (
        (1 , 'ชื่อผลไม้'),
        (2 , 'ราคา'),
        (3 , 'ฤดู'),
        (4 , 'ชื่อฟาร์ม'),
    )

class SearchForm(forms.Form):
    

    SearchBy = forms.ChoiceField(choices=searchchoices)
    keyword = forms.CharField(max_length=100)
