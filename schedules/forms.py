from django import forms

from .models import Window


class StreamForm(forms.Form):
    stream_url = forms.URLField()
    windows = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Windows to Stream to', choices=[])

    def __init__(self):
        super(StreamForm, self).__init__()
        self.fields['windows']['choices'] = [(w.id, w) for w in Window.objects.all()]
