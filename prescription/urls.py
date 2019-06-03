from django.urls import path
from . import views
urlpatterns = [
	path('',views.index,name='index'),
	path('<prescription_id>/', views.pres_view, name='view'),
	path('new',views.new,name ='new')
]
