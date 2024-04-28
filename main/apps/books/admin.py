from django import forms
from django.contrib import admin

from main.apps.books.models import Book
from main.apps.django_dictionary_widget.widgets import DictionaryEditorWidget


class BookForm(forms.ModelForm):
    description = forms.JSONField(widget=DictionaryEditorWidget())

    class Meta:
        model = Book
        fields = ['name', 'description']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    form = BookForm
