import json

from django import forms


class DictionaryEditorWidget(forms.Widget):
    template_name = 'django_dictionary_widget.html'

    # TODO
    #   1. Delete key
    #   2. Load css and js from Media
