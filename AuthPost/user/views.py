from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from user.forms import SignUpForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

# Create your views here.
#Sign Up
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           user =  form.save()
            
           first_name = user.first_name.title()
           messages.success(request, f'Hii,{first_name} Your account is created SUCCESSFULLY')
           return redirect('home')
        else:
           
            return redirect(user_signup)
    else:
        form = SignUpForm()
        context = {'forms': form}
    return render(request, 'signup.html', context)


class ProfileUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'profile.html'
    success_url = '/dashboard'