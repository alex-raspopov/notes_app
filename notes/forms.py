from django import forms
from .models import Notes, Category


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        widgets = {'title': forms.Textarea(attrs={'cols': "20", "rows": "1"})}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {'title': forms.Textarea(attrs={'cols': "20", "rows": "1"})}
