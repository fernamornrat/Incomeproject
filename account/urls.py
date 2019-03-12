from django.urls import path
from account import views
from wallet.views import add_wallet
from transection.views import add_transection

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/wallet/', add_wallet, name='add_wallet'),
    path('dashboard/transection/', add_transection, name='add_transection'),
]
