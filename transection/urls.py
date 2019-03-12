from django.urls import path
from transection import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='transection'),
    path('add', views.add_transection, name='add_transection'),
    path('delete/<int:transection_id>', views.delete_transection, name='delete'),
    path('edit/<int:transection_id>', views.edit_transection_form, name='edit'),
    path('editsave', views.edit_transection_save, name='editsave')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)