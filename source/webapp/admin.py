
from django.contrib import admin
from .models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('pk', 'name', 'email', 'text',
                    'created_at', 'updated_at',)
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


admin.site.register(GuestBook, GuestBookAdmin)



