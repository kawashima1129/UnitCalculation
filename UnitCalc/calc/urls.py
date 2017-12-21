from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/results$', views.results, name='results'),
    url(r'^inquire$', views.inquire, name='inquire'),
]
