from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from user.forms import LoginForm, RegisterForm


def login_page(request):
    form = LoginForm
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            password = cd['password']
            user = authenticate(request=request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('pages:home')
            else:
                return HttpResponse("Email or password is wrong!")
            
    context = {
        'form': form
    }
    return render(request, template_name="htmls/login-register.html", context=context)


def register_page(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request=request, user=user)
            return redirect("pages:home")
        

    context = {
        'form': form
    }

    return render(request=request, template_name='htmls/register.html', context=context)

def logout_page(request):
    logout(request)
    return redirect("pages:home")

