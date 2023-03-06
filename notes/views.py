from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Notes, Category
from .forms import NoteForm, CategoryForm


def hello(request):
    return HttpResponse("Hello from Notes app.")


def index(request):
    categories_list = get_list_or_404(Category.objects.order_by('-title'))
    upcoming_notes = Notes.objects.order_by('reminder')[:5]
    context = {'categories_list': categories_list, 'upcoming_notes': upcoming_notes}
    return render(request, 'notes/view_categories.html', context)


def notes_in_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    notes = category.notes.all()
    return render(request, 'notes/view_notes_in_category.html', {'category': category, 'notes': notes})


def view_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    return render(request, 'notes/view_note.html', {'note': note})


def note_add(request):
    if request.method == 'GET':
        form = NoteForm()
        return render(request, 'notes/note.html', {'form': form})
    else:
        # if this is a POST request we need to process the form data
        # create a form instance and populate it with data from the request:
        form = NoteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            note = Notes(title=form.cleaned_data['title'], text=form.cleaned_data['text'],
                         reminder=form.cleaned_data['reminder'], category=form.cleaned_data['category'])
            note.save()
            # redirect to a new URL:
            return HttpResponse('thanks')


def category_add(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'notes/category.html', {'form': form})
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category(title=form.cleaned_data['title'])
            category.save()
            return HttpResponse('thanks')


def category_update(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request, 'notes/category.html', {'form': form})
    else:
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category.save()
            return HttpResponse('thanks')


def note_update(request, note_id):
    note = Notes.objects.get(id=note_id)
    if request.method == 'GET':
        form = NoteForm(instance=note)
        return render(request, 'notes/note.html', {'form': form})
    else:
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note.save()
            return HttpResponse('thanks')


def note_delete(request, note_id):
    return render(request, 'notes/delete.html')


def category_delete(request, category_id):
    return render(request, 'notes/delete.html')
