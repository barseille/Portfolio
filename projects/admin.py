from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'technologies', 'code_link', 'live_link']
    search_fields = ['title', 'technologies']
