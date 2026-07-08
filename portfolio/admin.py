from django.contrib import admin
from .models import Contact, Blog, Skill


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin interface for Contact messages."""
    list_display = ('name', 'email', 'subject', 'date_created', 'is_read')
    list_filter = ('date_created', 'is_read')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date_created', 'date_updated')
    list_editable = ('is_read',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
        ('Timestamps', {
            'fields': ('date_created', 'date_updated'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Admin interface for Blog posts."""
    list_display = ('title', 'date_created', 'date_updated', 'is_published')
    list_filter = ('is_published', 'date_created')
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('date_created', 'date_updated')
    
    fieldsets = (
        ('Blog Post Details', {
            'fields': ('title', 'slug', 'description', 'image', 'content')
        }),
        ('Publication', {
            'fields': ('is_published',)
        }),
        ('Timestamps', {
            'fields': ('date_created', 'date_updated'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin interface for Skills."""
    list_display = ('name', 'level', 'category', 'date_updated')
    list_filter = ('category', 'level')
    search_fields = ('name',)
    list_editable = ('level',)
    readonly_fields = ('date_created', 'date_updated')
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'level', 'category', 'icon_class')
        }),
        ('Timestamps', {
            'fields': ('date_created', 'date_updated'),
            'classes': ('collapse',)
        }),
    )