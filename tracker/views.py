from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from dal import autocomplete
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse



def new_listing(request):
    if request.method == 'POST':
        form = NewListingForm(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('all_listings')
    else:
        form = NewListingForm()
    return render(request, 'new_listing_form.html', {'form': form})


def personal_homepage(request):
    pass

def all_listings(request):
    if request.user.is_authenticated:
        listings = JobListing.objects.all()
        # myintersts = My_Jobs.objects.filter(user = request.user)
        # applied_listings_ids = request.user.myapplications_set.all().values_list('listing__id', flat = True)

        return render(request, 'all_listings.html', {'listings': listings})
    else:
        return redirect('login')

def interested(request, listing_id):
    listing = JobListing.objects.get(id = listing_id)
    interest = MyApplications.objects.create(
        listing = listing,
        user = request.user,
    )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def not_interested(request, listing_id):
    job = MyApplications.objects.filter(listing = listing_id)

    job.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def single_listing(request, j_id):
    if request.user.is_authenticated:
        job = JobListing.objects.get(id = j_id)
        print(job)

        return render(request, 'single_listing.html', {'job': job})
    else:
        return redirect('login')


def my_applications_intertested(request):
    if request.user.is_authenticated:
        my_applications = MyApplications.objects.filter(user = request.user, status = 'INTERTESTED')

        return render(request, 'my_applications.html', {'my_applications': my_applications})


def my_applications_applied(request):
    if request.user.is_authenticated:
        my_applications = MyApplications.objects.filter(user = request.user, status = 'APPLIED')

        return render(request, 'my_applications.html', {'my_applications': my_applications})


def my_applications_interview(request):
    if request.user.is_authenticated:
        my_applications = MyApplications.objects.filter(user = request.user, status = 'INTERVIEW')

        return render(request, 'my_applications.html', {'my_applications': my_applications})


def my_applications_accepted(request):
    if request.user.is_authenticated:
        my_applications = MyApplications.objects.filter(user = request.user, status = 'ACCEPTED')

        return render(request, 'my_applications.html', {'my_applications': my_applications})


def my_applications_rejected(request):
    if request.user.is_authenticated:
        my_applications = MyApplications.objects.filter(user = request.user, status = 'REJECTED')

        return render(request, 'my_applications.html', {'my_applications': my_applications})



def my_applications_single(request, application_id):

    application = MyApplications.objects.get(id = application_id)
    application_update = ApplicationUpdateForm(request.POST ,instance = application,)
    updates_form = UpdatesForm
    updates = Updates.objects.filter(application=application)
    if request.method == 'POST' and 'update' in request.POST:
        form = UpdatesForm(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.application = MyApplications.objects.get(id = application_id)
            f.save()
    
    if request.method == 'POST' and 'application' in request.POST:
        if application_update.is_valid():
            print(application_update)
            application_update.save()
        return HttpResponseRedirect(request.path_info)

    return render(request, 'my_applications_single.html', {'application': application, 'updates_form': updates_form, 'application_update': application_update, 'updates':updates})


class DeleteComment(DeleteView):
    model = Updates
    success_url = reverse_lazy('my_applications_single')
    
    def get_success_url(self):
        print(self.kwargs)
        return reverse('my_applications_single', kwargs={'application_id': int(self.object.application.id)})
