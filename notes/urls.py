from django.urls import path
from django.views.generic import ListView

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # as function
    # path('index/', ListView.as_view(), name='index'),  # as Class
    path('category_<int:category_id>/', views.notes_in_category, name='notes_in_category'),
    path('note_<int:note_id>/', views.view_note, name='view_note'),
    path('note/', views.note_add, name='note_add'),
    path('category/', views.category_add, name='category_add'),
    path('category_<int:category_id>/u/', views.category_update, name='category_update'),
    path('category_<int:category_id>/d/', views.category_delete, name='category_delete'),
    path('note_<int:note_id>/u/', views.note_update, name='note_update'),
    path('note_<int:note_id>/d/', views.note_delete, name='note_delete'),
]
