from django.contrib import admin

# Register your models here.
from .models import Course, Dance_Class, Subscription, Dance_Style, Comment

admin.site.register(Course) 
admin.site.register(Dance_Class) 
admin.site.register(Subscription) 
admin.site.register(Dance_Style) 
admin.site.register(Comment) 