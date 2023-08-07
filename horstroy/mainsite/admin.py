from django.contrib import admin

from .models import Service, Image, Project, DesignProject


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title') 
    search_fields = ('title', ) 
    empty_value_display = '-'

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title') 
    search_fields = ('title', ) 
    empty_value_display = '-'

class DesignProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title') 
    search_fields = ('title', ) 
    empty_value_display = '-'

class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name') 
    search_fields = ('name', ) 
    empty_value_display = '-'
    ordering = ('name', )

admin.site.register(DesignProject, DesignProjectAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Image, ImageAdmin)
