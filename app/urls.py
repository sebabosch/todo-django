from django.urls import path
from . import views

urlpatterns = [
	path('', views.Index.as_view(),name='index'),
	#path('e/<str:primary_key>/', views.upd, name='upd'),
	path('folders/',views.FolderView.as_view(),name='folders'),
	path('folders/<str:folder>',views.FolderView.as_view(),name='folders'),
	path('tasks/<str:folder>',views.ItemView.as_view(),name='task'),
	path('edit/<int:pk>',views.ItemEdit.as_view(),name='task'),
]
