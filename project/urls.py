"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    url(r'^nimda/', include(admin.site.urls)),
    url(r'^home/$', "mmain.views.cereal_list", name='cereal_list'),
    url(r'^$', "mmain.views.cereal_list", name='home'),
    url(r'^cereal_detail/(?P<pk>\d+)/$', "mmain.views.cereal_detail", name="cereal_detail"), 
    url(r'^manufacturer_list/$', "mmain.views.manufacturer_list", name="manufacturer_list"),
    url(r'^manufacturer_detail/(?P<pk>\d+)/$', 'mmain.views.manufacturer_detail', name='manufacturer_detail'),
    url(r'^create_cereal/$', "mmain.views.create_cereal", name='create_cereal'),
    url(r'^update_cereal/(?P<pk>\d+)/$', "mmain.views.update_cereal", name='update_cereal'),
    url(r'^cereal_delete/(?P<pk>\d+)/$', 'mmain.views.cereal_delete', name='cereal_delete'),
    url(r'^signup/$', 'mmain.views.signup', name='signup'),
    url(r'^login/$', 'mmain.views.login_user', name='login_user'),
    url(r'^logout/$', 'mmain.views.logout_user', name='logout_user'),
    url(r'^create_manufacturer/$', 'mmain.views.create_manufacturer', name='create_manufacturer'),
    url(r'^create_manufacturer/(?P<pk>\d+)/$', 'mmain.views.create_manufacturer', name='update_manufacturer'),
    url(r'^manufacturer_delete/(?P<pk>\d+)/$', 'mmain.views.manufacturer_delete', name='manufacturer_delete'),
    url(r'^template_view/', 'mmain.views.template_view', name='template_view_name'),
    url(r'^contact/$', 'mmain.views.contact', name='contact'),
    url(r'^feedback/$', 'mmain.views.feedback', name='feedback')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

