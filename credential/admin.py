from django.contrib import admin
from credential.models import Project
from credential.models import Employee
from credential.models import Vault
from credential.models import Component
from credential.models import Item
from credential.models import UserAccess


admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Vault)
admin.site.register(Component)
admin.site.register(Item)
admin.site.register(UserAccess)
