from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/update/', views.task_update, name='task_update'),
    path('api/tasks/', views.api_task_list, name='api_task_list'),
]

# from django.urls import path
# from django.contrib.auth import views as auth_views
# from .views import custom_login, custom_logout  # if you're using custom views

# urlpatterns = [
#     # Login and logout views
#     path('login/', auth_views.LoginView.as_view(), name='login'),  # or use custom_login
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # or use custom_logout
# ]
