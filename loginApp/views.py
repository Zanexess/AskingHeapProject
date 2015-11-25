from django.shortcuts import render_to_response,redirect,render
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
            else:
                args['login_error'] = "User not active"
        else:
            args['login_error'] = "User not found"
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    args = {}
    args.update(csrf(request))
    #args['form'] = UserCreationForm
    args['form'] = MyRegistrationForm
    print request.POST
    if request.POST:
        newuser_form = MyRegistrationForm(request.POST)
        if newuser_form.is_valid():
            user = newuser_form.save(commit=True)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'registration.html', {'form': args['form']})