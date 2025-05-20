from django.urls import path, include
from .views import UserSignUpView, UserProfileView, LoginView, LogOutView


urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
