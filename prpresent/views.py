from django.shortcuts import render

def home(request):
    import requests
    import json
    api_request = requests.get('https://api.github.com/users?since=1598676')
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api':api})