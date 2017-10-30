from django.conf.urls import url
from django.contrib.auth import views as auth_views
from smart_city_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^editor/$', views.editor, name='editor'),
    url(r'^places/$', views.places, name='places'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', auth_views.login, {'template_name': 'smart_city_app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'smart_city_app/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
]