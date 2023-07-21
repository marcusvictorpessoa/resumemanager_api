from django.contrib import admin

# Register your models here.
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'phone', 'experience_area', 'resume', 'resume_avaliation', 'note')