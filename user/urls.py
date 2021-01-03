from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
