from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Language)
admin.site.register(Role)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Course)
admin.site.register(Degree)
admin.site.register(Institute)

