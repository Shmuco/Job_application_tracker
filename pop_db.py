import os
from bs4.builder import HTML
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_application_tracker.settings')
django.setup()


from careerjet_api import CareerjetAPIClient
from tracker.models import JobListing, Company, Location
from datetime import datetime
from django.utils.timezone import make_aware
from  bs4 import BeautifulSoup
import requests
from django.conf import settings

affid = settings.AFFID
cj  =  CareerjetAPIClient("he_IL");



def search_query(page):
    result_json = cj.search({
                          # 'location'    : 'israel',
                          # 'keywords'    : keywords,
                          'affid'       : affid,
                          'user_ip'     : '11.22.33.44',
                          'url'         : 'http://www.example.com/jobsearch?q=python&l=london',
                          'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
                          'page'    : page,
                        
                      
                        });
    job_list = result_json['jobs']
    return job_list


def get_description(url):
  source = requests.get(url).text

  soup = BeautifulSoup(source, 'html.parser')
  description = soup.find('section', class_ = 'content')
  description.find('p', class_ = 'source').decompose()
  clean = (str(description)[25:-10]).strip()
  return clean


index = 0

for i in range(2000):
  jobs = search_query(i)
  print(len(jobs))
  

  for job in jobs:
    try:
      new = JobListing.objects.get(
            website = job['url'])
      index += 1
      print(index)
      continue

    except:
      comp, created = Company.objects.get_or_create(name = job['company'])
      loca, created = Location.objects.get_or_create(name = job['locations'])
      date = job['date']
      date_datetime = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z' )
      description = get_description(job['url'])
      new = JobListing.objects.create(
        website = job['url'],
        job_title = job['title'],
        company = comp,
        location = loca,
        description = description,
        salary = job['salary'],
        created = make_aware(date_datetime),
      )
      index += 1
      print(index)
    
