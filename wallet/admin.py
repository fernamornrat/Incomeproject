from django.contrib import admin
from .models import Wallet

class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Wallet, WalletAdmin)
