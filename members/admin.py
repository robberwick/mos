from django.contrib import admin
from django.contrib.auth.models import User

from mos.members.models import MemberAdmin

admin.site.unregister(User)
admin.site.register(User, MemberAdmin)
