from django.contrib import admin

# Register your models here.
from registration.models import CompanyUser

admin.site.register(CompanyUser)
