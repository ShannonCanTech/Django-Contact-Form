from django import forms
from django.forms import TextInput,EmailInput

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Jane Doe', 'class':'form-control'}), max_length=100, required=True)
    from_email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'placeholder': 'janedoe@example.com', 'class':'form-control'}), required=True)
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter message here...', 'class':'form-control'}), required=True)
