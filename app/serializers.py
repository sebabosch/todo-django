from rest_framework import serializers
from .models import *

class FolderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Folder
		fields = ['title']
        
class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ['id','ok','title']
	
	def validate_data(self,data):
		return data
	
	def to_representation(self, instance):
		return {
			'id': instance.id,
			'title': instance.title,
				'ok': "checked" if instance.ok else "" 
		}
