from django.conf.urls import url
from views import ServiceCreateView, ServiceUpdateView, ServiceDeleteView, ServiceRetriveView


urlpatterns = [
    url(r'^create/$', ServiceCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', ServiceUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)$', ServiceDeleteView.as_view(), name='delete'),
    url(r'^search/$', ServiceRetriveView.as_view(), name='search'),
]
