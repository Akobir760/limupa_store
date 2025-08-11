from django.urls import path


app_name = 'user'


from accounts.views import RegisterView, LoginView, ConfirmEmailView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('confirmation/<int:uid>/<str:token>', ConfirmEmailView.as_view(), name='confirmation'),
]