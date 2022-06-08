from django.urls import path

from users.views import UserLogin

app_name = 'user'

urlpatterns = [
    path('login/auth', UserLogin.as_view(), name='UserLogin'),
    path('logout', UserLogin.as_view(), name='UserLogout')
]