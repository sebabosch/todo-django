from django.urls import path
from . import views

urlpatterns = [
	path('', views.Index.as_view(),name='index'),
	#path('e/<str:primary_key>/', views.upd, name='upd'),
	path('folder/',views.FolderView.as_view(),name='folders'),
	path('folder/<str:folder>/',views.ItemView.as_view(),name='items'),
	path('task/<int:pk>/',views.ItemEdit.as_view(),name='task'),
]
