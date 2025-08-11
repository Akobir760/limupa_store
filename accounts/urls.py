from django.urls import path

from accounts.views import RegisterView, LoginView, ConfirmEmailView, LogoutView

app_name = "accounts"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirmation/<int:uid>/<str:token>', ConfirmEmailView.as_view(), name='confirmation'),
]