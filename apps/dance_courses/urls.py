from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^showUserCourses$', views.showUserCourses ,name='showUserCourses'),
    url(r'^createusers/$', views.createUsers ,name='createUsers'),
    url(r'^loginUsers/$', views.loginUsers ,name='loginUsers'),
    url(r'^logoutUsers/$', views.logoutUsers ,name='logoutUsers')
 #   url(r'^userNotes/$',views.userNotes, name='userNotes'),
 #   url(r'^new/$', views.newNote, name='new'),
 #   url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
 #   url(r'^showNotesOnly/$', views.showNotesOnly, name='showNotesOnly')
]