from django import forms
from django.forms import ModelForm,TextInput,FileInput

class InputForm(forms.Form):
    ip = forms.GenericIPAddressField(
        label='IP', 
        max_length=15,
        widget = forms.TextInput(
            attrs = {
                        'class': 'form-control', 
                        'id': 'exampleInputEmail1',
                        'type': 'text',
                        'placeholder': "ex. 158.108.125.125",
                        'name': 'ip'
                    }
        )
    )
    
    prefix = forms.IntegerField(
        label='Prefix', 
        min_value=1, 
        max_value=32,
        widget = forms.TextInput(
            attrs = {
                        'class': 'form-control', 
                        'id': 'exampleInputPassword1',
                        'type': 'text',
                        'placeholder': "1-31",
                        'name': 'prefix'
                    }
        )
    )