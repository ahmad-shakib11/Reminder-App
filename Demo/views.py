from django.shortcuts import render, HttpResponse, redirect
from Demo.forms import Registration

# Create your views here.
def HomePage(request):
    return render(request, 'Home.html')


def CreateNewReminder(request):
    return render(request, 'Create New Reminder.html')


def Title(request):
    return render(request, 'Title.html')


def Date(request):
    return render(request, 'Date.html')


def Time(request):
    return render(request, 'Time.html')


def Markasdone(request):
    return render(request, 'Mark as done.html')


def Settings(request):
    return render(request, 'Settings.html')

def register(request):

    if(request.method=='POST'):
        form = Registration(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('home')


    form = Registration()

    context ={
        'register_form': form,
    }
    return render(request,'register.html', context)
