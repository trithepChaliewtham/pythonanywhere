from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import Farm,Fruit,Season
from .form import *



# Create your views here.
banana = "https://www.thailandmedical.news/uploads/editor/files/ANTIVIRALS.jpg"

lemon = "https://share.upmc.com/wp-content/uploads/2014/10/lemon.png"

watermelon = "https://dz.lnwfile.com/jrbazo.jpg"






def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('LogIn')
    else:
        form = UserCreationForm()
    return render(request, 'myweb/register.html', {'form': form})

def index(req):
	return render(req, 'myweb/index.html')

def Contact(req):
    	return render(req, 'myweb/Contact.html')

def CheckInform(req):
    	return render(req, 'myweb/CheckInform.html')
def LogIn(req):
    
	return render(req, 'myweb/LogIn.html')

#---------- database function ----------#

def showFruit(testrequestreq):
    fruit = Fruit.objects.all()
    print(fruit)
    return render(testrequestreq ,'myweb/AllFruit.html' ,{'fruit':fruit})

def addfarm(req):
    if req.method == "POST":
        form = addFarm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = addFarm()
        context = {'form':form}
        return render(req, 'myweb/add.html',context)

def addfruit(req):
    if req.method == "POST":
        form = addFruit(req.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = addFruit()
        context = {'form':form}
        return render(req, 'myweb/add.html',context)


def search(req):
    if req.method == "POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            searchby = form.cleaned_data['SearchBy']
            keyword = form.cleaned_data['keyword']
            if searchby == '1':
                fruits = Fruit.objects.filter(Fruit_Name__contains=keyword)

            elif searchby == '2':
                try:

                    keyword = float(keyword)

                except:

                    form = SearchForm()
                    
                    context = {'form':form}
                    return render(req, 'myweb/SearchFruit.html',context)
                fruits = Fruit.objects.filter(Price=keyword)
                
            elif searchby == '3':

                fruits = Fruit.objects.filter(Season__SeasonName__contains=keyword)

            elif searchby == '4':

                fruits = Fruit.objects.filter(FarmName__Farm_Name__contains=keyword)
            return render(req , "myweb/ShowFruit.html",{"fruits":fruits})
    else:
        form = SearchForm()
        context = {'form':form}
        return render(req, 'myweb/SearchFruit.html',context)