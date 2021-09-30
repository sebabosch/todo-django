from rest_framework import serializers
from .models import *
from django.db import models

class FolderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Folder
		fields = ['title']

class ItemManager(models.Manager):
	def get_by_natural_key(self, folder):
		return self.get(folder=folder)


class ItemSerializer(serializers.ModelSerializer):
	objects = ItemManager()
	class Meta:
		model = Item
		fields = ['id','ok','title','folder']
	
	def validate_data(self,data):
		#data.folder_id = "VV"
		#data.id = Item.objects.order_by('-id').first().order
		#data.id = data.id  + 1 if data.id else 0
		return data
	
	def to_representation(self, instance):
		return {
			'id': instance.id,
			'title': instance.title,
			'ok': "checked" if instance.ok else "",
		}
