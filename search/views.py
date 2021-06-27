from django.http import response
from django.shortcuts import render, redirect
from .forms import *
from tracker.models import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def new_search(request):
    
    form = SearchForm(request.GET)
    if request.GET:
        if form.is_valid:
            f = form.save(commit=False)
            f.user = request.user
            # f.save()

            srch_words = f.query.split(' ')
            query = Q(job_title__icontains=srch_words[0]) | Q(description__icontains=srch_words[0])
            for word in srch_words[1:]:
                query |=  Q(job_title__icontains=word) | Q(description__icontains=word)
            listings = JobListing.objects.filter(query)
            
            paginator = Paginator(listings, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        


            
            # query_location = JobListing.objects.filter(location = f.location)
            # restults = query_location.filter(job_title__contains = f.query)|query_location.filter(description = f.query)
            # print(restults)
            print(page_obj)
            print(listings)


            return render(request, 'search_results.html', {'page_obj': page_obj, 'form': form})
    else:
        form = SearchForm()
    return render(request, 'new_search.html', {'form': form})
    


def search(qs, srch_str='hello world'):
    srch_words = srch_str.split(' ')
    query = Q(title__icontains=srch_words[0]) | Q(description__icontains=srch_words[0])
    for word in srch_words[1:]:
        query |=  Q(title__icontains=word) | Q(description__icontains=word)
    qs.filter(query)