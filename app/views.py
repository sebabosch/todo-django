from django.shortcuts import redirect
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import *
from .forms import *

class Index(APIView):
	def get(self,request):
		return redirect('/folders/')

class FolderView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'lists/folder.html'
	
	def get(self,request,*args, **kwargs):
		obj = Folder.objects.all()
		form = FolderForm()
		return Response({"obj":obj, 'form': form})
	
	def post(self,request,*args, **kwargs):
		form = FolderForm(request.POST)
		if form.is_valid():
			form.save() 
		return redirect(request.path)
	def delete(self,request,*args,**kwargs):
		Folder.objects.get(title=kwargs['folder']).delete()
		return HttpResponse()
	
class ItemView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'lists/items.html'
	
	def get(self,request,folder, **kwargs):
		obj = Item.objects.filter(folder=folder)
		form = ItemForm()
		return Response({"obj":obj, 'form': form,'folder':folder})
	
	def post(self,request,folder, **kwargs):
		form = ItemForm(request.POST)
		if form.is_valid():
			obj=form.save(commit=False)
			obj.folder = Folder.objects.get(title=folder)
			obj.save() 
		return redirect(request.path)
	
	def patch(self,request,*args, **kwargs):
		return redirect(request.path)
	
class ItemEdit(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'edit.html'
	
	def get(self,request,pk, **kwargs):
		obj = Item.objects.get(id=pk)
		form = ItemForm(initial={"title":obj.title})
		
		return Response({'obj':obj, 'form': form,'pk':pk,'folder':obj.folder.title})
	def patch(self,request,pk, **kwargs):
		obj = Item.objects.get(id=pk)
		if  request.GET["type"]=='ok':
			obj.toggle_task()
		elif  request.GET["type"]=='title':
			obj.title=str(request.GET["data"])
		obj.save()
		return HttpResponse()
		
