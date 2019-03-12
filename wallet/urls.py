from django.urls import path
from wallet import views

urlpatterns = [
    path('', views.index, name='wallet'),
    path('add', views.add_wallet, name='add_wallet'),
    path('edit', views.edit_wallet, name='edit_wallet'),
]