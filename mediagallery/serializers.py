from rest_framework import serializers
from .models import *

class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields = (
			'id',
			'url',
			'author',
			'media_type',
			'created_at',
			'country',
			'city'
		)