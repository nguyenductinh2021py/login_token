from django.urls import path, include
from .api import RegisterView, LoginView, UserAPI


urlpatterns = [
    path('api/auth/register', RegisterView.as_view()),
    path('api/auth/login', LoginView.as_view()),
    path('api/auth/user', UserAPI.as_view())
]
