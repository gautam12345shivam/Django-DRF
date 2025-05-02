from django.urls import path
from .views import RegisterView, LoginView, LogoutView
from .views import UserDetailView, UserDeleteView, UserUpdateView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('delete/<int:user_id>/', UserDeleteView.as_view(), name='delete-user'),
    path('update/<int:user_id>/', UserUpdateView.as_view(), name='update-user'),
    
]
