from django.contrib import admin
from mediagallery.models import *
from django.contrib.auth.admin import UserAdmin


class MediaClipAdmin(admin.ModelAdmin):
    '''
        Admin View for MediaClip
    '''
    list_display = ('name', 'start_sec', 'end_sec')


class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''
    pass


class MediaClipInline(admin.TabularInline):
    '''
        Tabular Inline View for MediaClip
    '''
    model = MediaClip
    extra = 1


class MediaAdmin(admin.ModelAdmin):
    '''
        Admin View for Media
    '''
    list_display = ('author', 'url', 'category', 'created_by')
    inlines = [MediaClipInline]


admin.site.register(Media, MediaAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MediaClip, MediaClipAdmin)