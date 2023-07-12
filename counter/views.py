from django.shortcuts import render,redirect
import requests
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#zMPQ5pknAt3m6uVmng8BmA==QuMkn1I8pe9mVIOa

@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url+query,headers = {'X-Api-Key': 'zMPQ5pknAt3m6uVmng8BmA==QuMkn1I8pe9mVIOa'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops there was an error"
            print(e)
        return render(request,'home.html',{'api':api})
    else:
        return render(request,'home.html',{'query':'Enter a valid query'})
  
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login/')

        user = User.objects.get(username=username)
        
        if not user.check_password(password):
            messages.error(request, 'Invalid password')
            return redirect('/login/')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')
            

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')




def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= User.objects.filter(username = username)
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('/register/')
        user = User.objects.create(
             first_name = first_name,
             last_name = last_name,
             username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')
        return redirect('/register/')

    return render(request,'register.html')