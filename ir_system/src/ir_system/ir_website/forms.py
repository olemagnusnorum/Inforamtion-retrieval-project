from django import forms

class searchPoemForm(forms.Form):
    query = forms.CharField(label="", max_length=200)
