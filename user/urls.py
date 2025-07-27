from django.urls import path
from user.views import login_page, register_page


app_name = 'user'

urlpatterns = [
    path('login', login_page, name='login_page'),
    path('register', register_page, name='register_page')
]