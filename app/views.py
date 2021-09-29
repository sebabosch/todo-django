from django.shortcuts import redirect
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import *
from .forms import *
from .serializers import *

class Index(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'index.html'
	def get(self,request):
		return Response({'form':FolderForm()})

class FolderView(APIView):
	#renderer_classes = [TemplateHTMLRenderer]
	template_name = 'lists/folder.html'
	serializer_class = FolderSerializer
	def get(self,request):
		#Get Folder list
		queryset = Folder.objects.all()
		serializer_class = FolderSerializer(queryset, many=True)
		return Response({'result':'ok','func':'listFolder','data':{'target':'Folders','obj':serializer_class.data}})#, 'form': form})
		#return Response({"obj":obj, 'form': form})
	def post(self,request,*args, **kwargs):
		
		serializer = FolderSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'result':'ok','func':'add','data':{'target':'Folders','obj':[serializer.validated_data]}})#, 'form': form})
		return Response({'result':'not_ok',})#, 'form': form})
		# True
		
		#return Response({"message": "Hello, world!"})
		

class ItemView(APIView):
	#renderer_classes = [TemplateHTMLRenderer]
	template_name = 'lists/items.html'
	
	def get(self,request,folder, **kwargs):
		#Get tasks in folder "folder"
		queryset = Item.objects.filter(folder=folder)
		form = ItemForm()
		serializer_class = ItemSerializer(queryset, many=True)
		#return Response({"obj":obj, 'form': form,'folder':folder})
		return Response({'result':'ok','func':'listItem','data':{'obj':serializer_class.data,'target':folder}})#, 'form': form})
	def delete(self,request,folder):
		Folder.objects.get(title=folder).delete()
		#return Response({"message": "Hello, world!"})
		return Response({'result':'ok','func':'rm','data':{'target':"F{}".format(folder)}})
	
	def post(self,request,folder, **kwargs):
		serializer = ItemSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()
			return Response({'result':'ok','func':'add','data':{'target':'Items','obj':[serializer.validated_data]}})#, 'form': form})
		return Response({'result':'not_ok',})#, 'form': form})
		# True

	
class ItemEdit(APIView):
	#renderer_classes = [TemplateHTMLRenderer]
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
		return Response({'result':'ok','func':'itemPatch','data':{'ok':obj.ok,'target':pk}})
		
