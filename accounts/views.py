from django.shortcuts import render,redirect
from .forms import user_form
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = user_form()


    return render(request,'signup.html',{'form':form})

@login_required
def home_view(request):
    return render(request,'home.html')  