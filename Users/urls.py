from django.urls import path, include
from .api import RegisterView, LoginView


urlpatterns = [
    path('api/auth/register', RegisterView.as_view()),
    path('api/auth/login', LoginView.as_view())
]
