from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'technologies', 'github_link', 'technical_skills', 'soft_skills', 'image']
    search_fields = ['title', 'technologies']
