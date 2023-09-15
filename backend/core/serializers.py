from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer):
    #all three fields are required to avoid a 404
	name = CharField(source="title", required=True)
	message = CharField(source="description", required=True)
	email = EmailField(required=True)
	
	class Meta:
		model = models.Contact
		fields = (
			'name',
			'email',
			'message'
		)