from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^new/$', views.new, name='new'),
    url(r'^add/$', views.add, name='add'),
    url(r'^destroy/(?P<review_id>\d+)$', views.destroy, name='destroy'),
    url(r'^show/(?P<book_id>\d+)$', views.show, name='show')

]	


