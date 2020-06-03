from django.shortcuts import render

def home(request):
    import requests
    import json
    api_request = requests.get('https://api.github.com/users?since=13')
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api':api})

def user(request):
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get('https://api.github.com/users/'+user)
        username = json.loads(user_request.content)
        return render(request,'user.html',{'user':user,"username":username})
    else:
        notfound = '請在搜索框中用關鍵詞搜索'
        return render(request,'user.html',{'notfound':notfound})