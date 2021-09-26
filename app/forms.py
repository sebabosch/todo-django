from django import forms
from django.forms import ModelForm

from .models import *


class FolderForm(forms.ModelForm):
    
    class Meta:
        model = Folder
        fields = '__all__'

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['title']
        
