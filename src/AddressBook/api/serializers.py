from rest_framework import serializers
from AddressBook.models import Contact

class ContactSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Contact
		fields = ('id', 'user', 'full_name', 'address', 'phone_number', 'email', 'zip_code')