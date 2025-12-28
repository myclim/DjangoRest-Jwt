from django.urls import path
from user.views import *


app_name = 'user'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('remove/', UserRemoveView.as_view(), name='remove'),
]
