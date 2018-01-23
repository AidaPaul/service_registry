from django.conf.urls import url
from service_registry import views

urlpatterns = [
    url(r'^services/$', views.snippet_list),
    url(r'^services/(?P<pk>[0-9]+)/$', views.snippet_detail),
]