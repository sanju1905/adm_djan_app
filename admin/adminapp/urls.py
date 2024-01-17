# urls.py

from django.urls import path
from .views import Create_User,get_all_users,update_user_status,Update_User


urlpatterns = [
    # ... other patterns
    path('create_user/', Create_User, name='create_user'),
    path('get_all_users/', get_all_users, name='get_all_users'),
    path('update/<int:user_id>/', Update_User, name='update'),
 
    path('update_user_status/<int:user_id>/', update_user_status, name='update_user_status'),
]
