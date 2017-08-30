from django.conf.urls import url

from smart_city_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]