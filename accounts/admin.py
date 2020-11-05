from django.contrib import admin
from accounts.models import User, Level

admin.site.register([User, Level])