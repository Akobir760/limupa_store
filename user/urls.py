from django.urls import path
from user.views import login_page, register_page, logout_page


app_name = 'user'

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logour/', logout_page, name='logout_page')
]