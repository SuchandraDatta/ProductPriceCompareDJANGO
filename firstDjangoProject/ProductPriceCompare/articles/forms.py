from django import forms

class NameForm(forms.Form):
    your_name=forms.CharField(label='Item Name ', max_length=100)
    your_company=forms.CharField(label='Company Name' , max_length=100)
    your_modelNumber=forms.CharField(label='Model number' , max_length=100)