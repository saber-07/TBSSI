from django.urls import  path
from .views import UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('user/new/', UserCreateView.as_view(), name='user_new'),
    path('user/edit/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]