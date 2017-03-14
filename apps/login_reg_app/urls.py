from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^addUser$', views.addUser,name="addUser"),
    url(r'^login$',views.login, name="login"),
]
