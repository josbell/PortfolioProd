"""portfolio_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.portfolio.urls', namespace='portfolio')),
    url(r'^login_reg/', include('apps.login_reg_app.urls', namespace='login_reg')),
    url(r'^book_review/', include('apps.book_review.urls', namespace='book_review')),
    url(r'^ninja_gold/', include('apps.ninja_gold_app.urls', namespace='ninja_gold')),
    url(r'^notes_app/', include('apps.notes_app.urls', namespace='notes_app')),
    url(r'^dance_courses/', include('apps.dance_courses.urls', namespace='dance_courses'))
]
