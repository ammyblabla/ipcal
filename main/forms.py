from django import forms
from django.forms import ModelForm,TextInput,FileInput
import main.ipcal

subnet_list = ((32, '255.255.255.255/32'), (31, '255.255.255.254/31'), (30, '255.255.255.252/30'), (29, '255.255.255.248/29'), (28, '255.255.255.240/28'), (27, '255.255.255.224/27'), (26, '255.255.255.192/26'), (25, '255.255.255.128/25'), (24, '255.255.255.0/24'), (23, '255.255.254.0/23'), (22, '255.255.252.0/22'), (21, '255.255.248.0/21'), (20, '255.255.240.0/20'), (19, '255.255.224.0/19'), (18, '255.255.192.0/18'), (17, '255.255.128.0/17'), (16, '255.255.0.0/16'), (15, '255.254.0.0/15'), (14, '255.252.0.0/14'), (13, '255.248.0.0/13'), (12, '255.240.0.0/12'), (11, '255.224.0.0/11'), (10, '255.192.0.0/10'), (9, '255.128.0.0/9'), (8, '255.0.0.0/8'), (7, '254.0.0.0/7'), (6, '252.0.0.0/6'), (5, '248.0.0.0/5'), (4, '240.0.0.0/4'), (3, '224.0.0.0/3'), (2, '192.0.0.0/2'), (1, '128.0.0.0/1'),)
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

    prefix = forms.ChoiceField(
        label = 'Prefix',
        widget = forms.Select(
            attrs = {
                'name': 'prefix',
                # 'class': "dropdown-menu",
                # 'aria-labelledby': "dropdownMenuButton",
            }
        ) ,
        choices = subnet_list,
    )
        # todays_date= forms.IntegerField(label="What is today's date?", widget=forms.Select(choices=INTEGER_CHOICES))
