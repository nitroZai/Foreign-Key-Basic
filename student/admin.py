from django.contrib import admin
from .models import Student, Subjects, Marks
# Register your models here.

admin.site.register(Student)
admin.site.register(Subjects)
admin.site.register(Marks)