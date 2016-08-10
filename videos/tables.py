import django_tables2 as tables

from .models import Video

class SimpleTable(tables.Table):
    class Meta:
        model = Video
        sequence = ('title', 'email')
        fields = ('title', 'email', 'approved')
        attrs = {'class': 'table table-bordered'}
