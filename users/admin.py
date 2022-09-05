from django.contrib import admin
from users.models import AccountType, Profile


admin.site.register(AccountType)
admin.site.register(Profile)
