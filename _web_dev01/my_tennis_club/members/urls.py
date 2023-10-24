#   path('about/', views.about, name='about'),
#   path('services/', views.services, name='services'),
#   path('past_projects/', views.past_projects, name='past_projects'),
#   path('careers/', views.careers, name='careers'),
#   path('sustainability/', views.sustainability, name='sustainability'),
#   path('contact_us/', views.contact_us, name='contact_us'),s
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]