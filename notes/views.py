from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Notes, Category


def hello(request):
    return HttpResponse("Hello from Notes app.")


def index(request):
    categories_list = get_list_or_404(Category.objects.order_by('-title'))
    context = {'categories_list': categories_list}
    return render(request, 'notes/view_categories.html', context)


def notes_in_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    notes = category.notes.all()
    return render(request, 'notes/view_notes_in_category.html', {'category': category, 'notes': notes})


def view_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    return render(request, 'notes/view_note.html', {'note': note})
