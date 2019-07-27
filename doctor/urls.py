from django.urls import path
from . import views
urlpatterns = [
	path('change_pass',views.change_pass,name='change_pass'),
	path('dash', views.dashboard, name='dash'),
	path('login',views.login,name ='login'),
	path('logout',views.logout,name='logout'),
	path('prescriptions',views.prescriptions,name='prescriptions'),
	path('search',views.search,name='search'),
	path('slots_setter',views.slots_setter,name='slots_setter'),
	path('get_slots',views.get_slots,name='get_slots'),
	path('add_appointment',views.add_appointment,name='add_appointment')
]
