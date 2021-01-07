from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

       #Check if password is match
        if password == password2:
            #Checking user name
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username " + username + " is already taken.")
                return redirect('accounts:register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email " + email + " is already taken.")
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    #Log in after register
                    user.save()
                    messages.success(request, "Account created successfully.")
                    return redirect('accounts:login')          
        else:
            messages.error(request, "Passwords do not match")
            return redirect('accounts:register')

    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
      #LogIn User.objects.
        username = request.POST['username']
        password = request.POST['password']
    
      #Check user and password is in database
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('pages:index')
        else:
            messages.error(request, "Username or password was incorrect.")
            return redirect('accounts:dashboard')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
     if request.method == 'POST':
        auth.logout(request)
        return redirect('pages:index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
