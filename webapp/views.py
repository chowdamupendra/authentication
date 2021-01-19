from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')
@login_required
def customer(request):
    return render(request, 'myapp/customer.html')
def logout(request):
    return render(request,'registration/logout.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'MyApp/registration.html', {'form': form})

