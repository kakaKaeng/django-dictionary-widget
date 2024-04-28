from django import forms
from django.contrib import admin

from django_dictionary_widget.widgets import DictionaryEditorWidget
from main.apps.books.models import Book


class BookForm(forms.ModelForm):
    description = forms.JSONField(widget=DictionaryEditorWidget())

    class Meta:
        model = Book
        fields = ['name', 'description']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    form = BookForm
