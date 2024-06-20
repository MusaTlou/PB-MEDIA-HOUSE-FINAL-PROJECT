import requests
from django.shortcuts import render

def home(request):
  # USING APIS => Example 1
  response = requests.get('https://zenquotes.io/api/random')
  data = response.json()[0]
  quote = data['q']
  author = data['a']

  # Example 2
  reponse2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = reponse2.json()
  result2 = data2["message"]



  return render(request, 'templates/index.html', {'quote': quote, 'author': author, 'result2': result2})