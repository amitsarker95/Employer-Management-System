from django.urls import path, include
from .views import UserSignUpView, UserProfileView


urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
