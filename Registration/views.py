from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from .forms import CreateUserForm, LoginForm

# Create your views here.

# @login_required
def home(request):
    return render(request, 'Registration/Homepage.html')


def loginRenderpage(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            fetchedUsername = request.POST.get('username')
            fetchedPassword = request.POST.get('password')
            user = authenticate(request, username=fetchedUsername, password=fetchedPassword)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'loginformkey': form}
    return render(request, 'Registration/loginpage.html', context)


def signupRenderPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to login after successful signup
    context = {"registerformkey": form}
    return render(request, "Registration/signupPage.html", context)

def logoutRenderPage(request):
    auth.logout(request)  # Log out the user
    return redirect('signin')  # Redirect to login page after logout

@login_required(login_url="signin")  # Require login for accessing the dashboard
def dashBoardRenderPage(request):
    return render(request, 'Registration/Dashboard.html', {})
