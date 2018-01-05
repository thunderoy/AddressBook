from django import forms
from .models import Contact

class RegistrationLoginForm(forms.Form):
	username = forms.CharField(required=True, label='Username')
	password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput())

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = [
		    "full_name",
		    "address",
		    "phone_number",
		    "email",
		    "zip_code",
		]