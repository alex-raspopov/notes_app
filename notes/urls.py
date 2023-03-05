from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('category_<int:category_id>/', views.notes_in_category, name='notes_in_category'),
    path('note_<int:note_id>/', views.view_note, name='view_note'),
]
