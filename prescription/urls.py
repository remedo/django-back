from django.urls import path
from . import views
urlpatterns = [
	path('',views.index,name='index'),
	path('pres_view', views.pres_view, name='view'),
	path('new',views.new,name ='new'),
	path('{prescription_id}',views.display,name='display')
]
