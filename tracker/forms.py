from django import forms
from .models import *
from dal import autocomplete

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', )
        labels = {
            'name': 'Company',
        }
    

class NewListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ('job_title','description','website','location')
       
      
class UpdatesForm(forms.ModelForm):
    class Meta:
        model = Updates
        fields = ('text',)



class ApplicationUpdateForm(forms.ModelForm):
    class Meta:
      model = MyApplications
      fields = ('status',)
      use_required_attribute = False
    