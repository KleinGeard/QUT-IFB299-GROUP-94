from django.conf.urls import url

from smart_city_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
]