from django.forms import widgets
from rest_framework import serializers
from tree.models import *

class PictureSeriallizer(serializers.Serializer):
	image = serializers.CharField()
	taken = serializers.DateField()
	taken_confirmed = serializers.BooleanField()
	notes = serializers.CharField()

	def create(self, validated_data):
		"""
		Create and return a new `Snippet` instance, given the validated data.
		"""
		return Picture.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.image = validated_data.get('image', Picture.image)		
		instance.taken = validated_data.get('taken', Picture.taken)
		instance.taken_confirmed = validated_data.get('taken_confirmed', Picture.taken_confirmed)
		instance.notes = validated_data.get('notes', Picture.notes)
		instance.save()
		return instance