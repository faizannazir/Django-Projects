import django_filters
from django_filters import DateFilter
from django import forms
from .models import Attendance

class AttendanceFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date",lookup_expr="gte",widget=forms.DateTimeInput(attrs={
            'type': 'date',
            'id' : 'start-date',
        }))
    end_date = DateFilter(field_name="date",lookup_expr="lte",widget=forms.DateTimeInput(attrs={
            'type': 'date',
            'id' : 'end-date',
        }))
    class Meta:
        model = Attendance
        fields = ['start_date','end_date']


class AdminAttendanceFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date",lookup_expr="gte",widget=forms.DateTimeInput(attrs={
            'type': 'date',
            'id' : 'start-date',
        }))
    end_date = DateFilter(field_name="date",lookup_expr="lte",widget=forms.DateTimeInput(attrs={
            'type': 'date',
            'id' : 'end-date',
        }))
    class Meta:
        model = Attendance
        fields = ['employee','start_date','end_date']
        

