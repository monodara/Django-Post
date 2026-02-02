from django.contrib import admin
from .models import ProjectGroup, Technology, Project, ProjectImage

class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1  # Number of extra forms to display

class ProjectAdmin(admin.ModelAdmin):
    fields = ['group', 'title', 'description', 'github_link', 'technologies']
    inlines = [ProjectImageInline]
    list_display = ('title', 'group')
    list_filter = ('group',)
    filter_horizontal = ('technologies',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectGroup)
admin.site.register(Technology)