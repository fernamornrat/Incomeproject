from django.contrib import admin
from .models import Transection

class TransectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'amount', 'note', 'category', 'income')
    list_display_links = ('id', 'date')

admin.site.register(Transection, TransectionAdmin)  