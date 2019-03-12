from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cat_type')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'cat_type')
    
admin.site.register(Category, CategoryAdmin)