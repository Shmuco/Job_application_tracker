# from job_application_tracker.tracker.models import JobListing
# from job_application_tracker.tracker.models import Location
from django import forms
from .models import *

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('query','location',)

        

