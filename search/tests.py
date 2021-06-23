from django.test import TestCase

# Create your tests here.
import requests
# Create your views here.

response = requests.get("https://apis.indeed.com/oauth/v2/tokens", headers={'client_id':"63b387b4f16fcfae3e50f38273de30e2f41dc612cfe66780e5755658a66089e5
", 'client_secret': 'owF7TUgXboBQ590nTaH7rkFKVMudEO7QzFV9KIvfyjvScrmJrZDQNv9tcvOuHanl'})

print(response)