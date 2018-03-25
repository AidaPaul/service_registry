from django.conf.urls import url
from views import ServiceCreateView, ServiceUpdateView, ServiceDeleteView, ServiceRetriveView


urlpatterns = [
    url(r'^create/$', ServiceCreateView.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', ServiceUpdateView.as_view()),
    url(r'^delete/$', ServiceDeleteView.as_view()),
    url(r'^search/$', ServiceRetriveView.as_view()),
]
