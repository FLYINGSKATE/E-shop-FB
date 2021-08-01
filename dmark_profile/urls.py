
from django.contrib import admin
from django.urls import path
from .views import index,service, Career,about,Contact_us,private_policy

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('', index,name= 'homepage'),
    path('service', service,name = 'service'),
    path('career', Career.as_view(),name ='career'),
    path('about',about, name = 'about'),
    path('contact_us',Contact_us.as_view(), name = 'contact_us'),
    path('private_policy',private_policy, name = 'private_policy'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
