from django import crispy_forms
from .models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        field = ('name', 'age', 'sex', 'memo')
        widgets = {
            'name' : forms.TextInput(attrs = {'placeholder': '例：山田　太郎'}),
            'age' : forms.NumberInput(attrs = {'min' : 1}),
            'sex' : forms.RadioSelect(),
            'memo' : forms.Textarea(attrs = {'rows' : 4}),
        }