#generic

from rest_framework import generics
from AddressBook.models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions


class CreateContactApiView(generics.CreateAPIView):

	def get_queryset(self):
		return Contact.objects.all()

	serializer_class = ContactSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)