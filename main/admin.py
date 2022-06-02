from django.contrib import admin
from.models import *

# Register your models here.

admin.site.register(Jobs)
admin.site.register(Employee1)

# for Base
admin.site.register(BaseJob)
admin.site.register(BaseEmployee)


