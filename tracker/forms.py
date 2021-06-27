from django import forms
from .models import *
from dal import autocomplete

class NewListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ('job_title','company','description','website')
      
class UpdatesForm(forms.ModelForm):
    class Meta:
        model = Updates
        fields = ('text',)



class ApplicationUpdateForm(forms.ModelForm):
    class Meta:
      model = MyApplications
      fields = ('status',)
      use_required_attribute = False
    