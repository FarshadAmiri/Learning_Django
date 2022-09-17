from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    # path('profile/<str:username>', profile_view, name='profile'),
    path('Profile/change?password', change_password_view.as_view(), name='change_password'),
    path('profile/Update/<str:pk>', update_profile_view.as_view(), name='edit_info'),
    path('Profile/delete?account?', delete_account_view, name='delete_account'),
]