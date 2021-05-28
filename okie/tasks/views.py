from django.shortcuts import render
from .models import *
from django import forms
from django.contrib.auth.hashers import  make_password , check_password


count = 5
start = 0


class user_form(forms.ModelForm):
    class Meta:
        model = TUser
        fields = ['username' , 'password']
        labels = {
            'username': 'Username',
            'password': 'Password'
        }

class user_logform(forms.ModelForm):
    class Meta:
        model = TUser
        fields = ['username' , 'password']
        labels = {
            'username': 'Username',
            'password': 'Password'
        }

class task_form(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['task_title' , 'task_description' , 'task_pic']
        labels = {
            'task_title': 'Task Name',
            'task_description': 'Description',
            'task_pic':'Any Image'
        }


# Create your views here.
def index(request):
    return render(request, "tasks/layout.html" , {
        "user1" : request.session.get("username")
    })


def signin(request):
    if request.method == 'POST':
        form_u = user_form(request.POST , request.FILES)
        if form_u.is_valid():
            TUser = form_u.save(commit=False)
            TUser.password = make_password(TUser.password)
            TUser.save()
            return index(request)
        else:
            return render(request, "tasks/signin.html", {
                "signinform": form_u,
                "notvaild":True,
                "user1": request.session.get("username")
            })
    return render(request,"tasks/signin.html" , {
        "signinform" : user_form(),
        "user1": request.session.get("username")
    })

def login(request):
    if request.method == 'POST':
        form_log = user_logform(request.POST )
        if form_log.is_valid():
            pass
        else:
            t  = request.POST.get('username')
            p  = request.POST.get('password')
            us = TUser.objects.get(username=t)
            if check_password(p, us.password):
                request.session['username'] = us.uid
                return index(request)



    return render(request, "tasks/login.html" , {
        "loginform" : user_logform(),
        "user1": request.session.get("username")

    })

def logout(request):
    request.session['username'] = None
    return index(request)

def task_creation(request):
    if request.method == 'POST':
        form_t = task_form(request.POST , request.FILES)
        if form_t.is_valid():
            tm = form_t.save(commit=False)
            tm.uid = TUser.objects.get(uid = request.session.get('username') )
            tm.save()

        else:
            print(form_t.errors)
            return render(request, "tasks/creation.html", {
                "task_creat": form_t,
                "user1": request.session.get("username")
            })


    return  render(request,"tasks/creation.html",{
        "task_creat":task_form(),
        "user1": request.session.get("username")
    })

def task_display(request):
    all_task = tasks.objects.all()
    if len(all_task) < count:
        dis = [all_task[i] for i in range(start, len(all_task))]
    else:
        dis = [all_task[i] for i in range(start,count)]

    return  render(request,"tasks/display.html",{
        "all_task": dis,
        "user1": request.session.get("username"),
    })


def increase(request):
    global count, start
    start = count
    count += 5
    return task_display(request)