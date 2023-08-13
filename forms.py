from django import forms
from admissions.models import student

class studentModelForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'


class VendorForm(forms.Form):
    name = forms.CharField()
    adress = forms.CharField()
    contact = forms.CharField()
    item = forms.CharField()