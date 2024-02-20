# admin.py
from django.contrib import admin
from .models import TrainingProgram

class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('training_subject', 'prerequisites', 'training_organization', 'join_date', 'end_of_registration')

admin.site.register(TrainingProgram, TrainingProgramAdmin)
