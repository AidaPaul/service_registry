from django.conf.urls import url
from views import ServiceCreateView, ServiceUpdateView, ServiceDeleteView, ServiceRetriveView


urlpatterns = [
    url(r'^create/$', ServiceCreateView.as_view()),
    url(r'^update/$', ServiceUpdateView.as_view()),
    url(r'^delete/$', ServiceDeleteView.as_view()),
    url(r'^find/$', ServiceRetriveView.as_view()),
]
