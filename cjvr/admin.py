from django.contrib import admin
from .models import Victim, Plaintiff, AgresssionType, Testimony


admin.site.register(Victim)
admin.site.register(Plaintiff)
admin.site.register(AgresssionType)
admin.site.register(Testimony)

