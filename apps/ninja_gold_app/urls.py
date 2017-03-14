from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process_money/(?P<locn>\w+)$', views.process, name="process")
]