from django import forms

from schedules.models import Window


class StreamForm(forms.Form):
    stream_url = forms.URLField()
    windows = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Windows to Stream to', choices=[(w.id, w) for w in Window.objects.all()])
