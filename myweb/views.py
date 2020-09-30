from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
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

def ViewPrice(req):
    	return render(req, 'myweb/ViewPrice.html')

def CheckInform(req):
    	return render(req, 'myweb/CheckInform.html')
def LogIn(req):

	return render(req, 'myweb/LogIn.html')





