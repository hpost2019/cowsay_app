from django import forms


class IndexForm(forms.Form):
    text = forms.CharField(max_length=100)
