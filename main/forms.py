from django import forms

class GetCountry(forms.Form):
    iso3 = forms.CharField(label = "ISO3 Code: ", max_length=3)