from django.contrib import admin
from . models import university
from.models import college
from . models import course
from . models import branch
from . models import subject
from . models import Student
from . models import teacher


# Register your models here.
admin.site.register(university)
admin.site.register(college)
admin.site.register(course)
admin.site.register(branch)
admin.site.register(subject)
admin.site.register(Student)
admin.site.register(teacher)

