from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Video
        fields = ['uploader_name', 'email', 'phone', 'address', 'city', 'state',
                  'zipcode', 'title', 'description',
                  'category', 'file']
