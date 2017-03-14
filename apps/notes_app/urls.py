from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginUsers ,name='loginUsers'),
    url(r'^register/$', views.registerUsers ,name='registerUsers'),
    url(r'^userNotes/$',views.userNotes, name='userNotes'),
    url(r'^new/$', views.newNote, name='new'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^showNotesOnly/$', views.showNotesOnly, name='showNotesOnly')
]
