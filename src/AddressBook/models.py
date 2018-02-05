from django.db import models

# Create your models here.

from django.core.validators import RegexValidator, validate_email
from django.contrib.auth.models import User

class Contact(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=100)
	address = models.CharField(max_length=1000)

    # phone = models.IntegerField()
	phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '9999999999'. Exactly 10 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=False)# validators should be a list

	# email_validator = EmailValidator(message=None, code=None, whitelist=None)
	#email_validator = EmailValidator()
	email = models.EmailField(validators=[validate_email])

    # zipcode = models.DecimalField(max_digits=6, decimal_places=0)
	zip_regex = RegexValidator(regex=r'^\d{6}$', message="Zip code must be entered in the format: '666666'. Exactly 6 digits allowed.")
	zip_code = models.CharField(validators=[zip_regex], max_length=6, blank=False)# validators should be a list

	def __str__(self):
		return self.full_name