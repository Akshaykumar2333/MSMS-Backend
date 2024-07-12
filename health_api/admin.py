from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Description)
admin.site.register(models.Diet)
admin.site.register(models.Medication)
admin.site.register(models.Precaution)
admin.site.register(models.SymptomDescription)
admin.site.register(models.Workout)
