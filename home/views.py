from django.shortcuts import render



def index(request):
    return render(request,'index.html',{})

def contact(request):
    return render(request,'contact.html',{})


def about(request):
    return render(request,'about.html',{})

def projects(request):
    return render(request,'projects.html',{})

def services(request):
    return render(request,'services.html',{})

def gallery(request):
    return render(request,'gallery.html',{})