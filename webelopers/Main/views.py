from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
from Main.forms import UserRegistrationForm


def home(request):
    return render(request, "home.html",{"user" : request.user})


def sign_up(request):
    return render(request, "signup.html",{"user" : request.user})


def create_user(request):
    print("in create user")
    if request.POST:
        print("post")
        user_temp = User()
        # todo: check unique username
        # todo:check for required fields
        user_temp.username = request.POST.get('username')
        user_temp.password = request.POST.get('password')
        user_temp.email = request.POST.get('email')
        user_temp.first_name = request.POST.get('first_name')
        user_temp.last_name = request.POST.get('last_name')
        user_temp.save()
        login(request, user_temp)  # our change
        return HttpResponseRedirect('/')


def login_(request):
    form = UserRegistrationForm(request.POST)
    error = False
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = True
        forms.ValidationError('نام کاربری یا گذرواژه غلط است')
        error = True

    return render(request, "login.html", {
        "error": error,"form":forms
    })
def login__(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists()):
                User.objects.create_user(username, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('نام کاربری یا گذرواژه غلط است')
        else:
            form = UserRegistrationForm()
        return render(request, 'login.html', {'form': form})
def logout_(request):
    try:
        logout(request)
    except:
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")
def contact_us(request):
    return render(request,'contact_us.html')
def contact_saved(request):
    title = request.POST.get('title')
    text=request.POST.get('text')
    email = request.POST.get('email')
    email = EmailMessage(title, email+'\n'+text, to=['ostaduj@fastmail.com'])
    email.send()
    return render(request,"contactSaved.html")