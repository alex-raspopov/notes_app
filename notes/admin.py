from django.contrib import admin

# Register your models here.

from .models import Notes, Category

# admin.site.register(Notes)
admin.site.register(Category)


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'reminder', 'id')
    list_filter = ('category', 'user', 'reminder')

    fieldsets = (
        (None, {
            'fields': ('id', 'title', 'text')
        }),
        ('Availability', {
            'fields': ('category', 'user', 'reminder')
        }),
    )
