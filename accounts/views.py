from django.shortcuts import render

# Create your views here.
import threading

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from accounts.forms import RegisterForm, LoginForm
from accounts.utils import send_email_confirmation


class RegisterView(FormView):
    template_name = 'htmls/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        email_thread = threading.Thread(target=send_email_confirmation, args=(user, self.request,))
        email_thread.start()

        messages.success(self.request, "Please, confirm your email and login")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something getting wrong")
        return super().form_invalid(form)


class LoginView(FormView):
    template_name = 'htmls/login-register.html'
    form_class = LoginForm
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        login(request=self.request, user=form.cleaned_data["user"])
        messages.success(self.request, "Please, confirm your email and login")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Username or password is invalid")
        return super().form_invalid(form)


class ConfirmEmailView(View):
    @staticmethod
    def get(request, uid, token):
        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            messages.error(request, "User not found")
            return redirect('users:login')

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your email address is verified!")
            return redirect(reverse_lazy('accounts:login'))
        else:

            messages.error(request, "Link is not correct")
            return redirect(reverse_lazy('accounts:register'))


class LogoutView(View):
    @staticmethod
    def post(request):
        logout(request)
        return redirect('pages:home')


