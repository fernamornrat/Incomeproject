from django.urls import path
from category import views

urlpatterns = [
    path('', views.index, name='category'),
    path('add', views.add_category, name='add_category'),
    path('edit/<int:cat_id>', views.edit_category_form, name='edit_category'),
    path('save', views.edit_category_save, name='save_category'),
    path('delete/<int:cat_id>', views.delete_category, name='delete_category')
]