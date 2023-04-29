from django.contrib import admin
from users_office.models import *


admin.site.register(User)
admin.site.register(Office)
admin.site.register(User_office)