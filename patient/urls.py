from django.urls import path
from . import views
urlpatterns = [
	path('change_pass',views.change_pass,name='change_pass'),
	path('dash', views.dashboard, name='dash'),
	path('login',views.login,name ='login'),
	path('logout',views.logout,name='logout'),
	path('prescriptions',views.prescriptions,name='prescriptions'),
]
