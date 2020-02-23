from django.contrib import admin
from .models import Victim, Plaintiff, AggressionType, Testimony


admin.site.register(Victim)
admin.site.register(Plaintiff)
admin.site.register(AggressionType)
admin.site.register(Testimony)

