from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Log)
admin.site.register(Guardian)
admin.site.register(Student)
