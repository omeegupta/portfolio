from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_editable = ('status',)
admin.site.register(Category, CategoryAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'industry', 'status')
    list_editable = ('status',)
admin.site.register(Project, ProjectAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
admin.site.register(Contact, ContactAdmin)
