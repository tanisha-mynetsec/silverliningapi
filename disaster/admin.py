from django.contrib import admin
from disaster import models

# Register your models here.

admin.site.register(models.Riot)
admin.site.register(models.Earthquake)
admin.site.register(models.CyberCrime)
admin.site.register(models.Tsunami)
admin.site.register(models.Flood)
admin.site.register(models.Terrorism)
admin.site.register(models.Severe_Pollution)
admin.site.register(models.Fire)
admin.site.register(models.NuclearWar)