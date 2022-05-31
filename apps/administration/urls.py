from django.urls import  path
from apps.administration import views

urlpatterns = [
    path('administration/user/new/', views.UserCreateView.as_view(), name='user_new'),
    path('administration/user/list', views.UserListView.as_view(), name='user_list'),
    path('administration/user/edit/<int:pk>/', views.UserUpdateView.as_view(), name='user_edit'),
    path('administration/user/delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('administration/user/detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('administration/filiale/new/', views.FilialeCreateView.as_view(), name='filiale_new'),
    path('administration/filiale/list', views.FilialeListView.as_view(), name='filiale_list'),
    path('administration/filiale/edit/<int:pk>/', views.FilialeUpdateView.as_view(), name='filiale_edit'),
    path('administration/filiale/delete/<int:pk>/', views.FilialeDeleteView.as_view(), name='filiale_delete'),
    path('administration/filiale/detail/<int:pk>/', views.FilialeDetailView.as_view(), name='filiale_detail'),
    path('administration/direction/new/', views.DirectionCreateView.as_view(), name='direction_new'),
    path('administration/direction/list', views.DirectionListView.as_view(), name='direction_list'),
    path('administration/direction/edit/<int:pk>/', views.DirectionUpdateView.as_view(), name='direction_edit'),
    path('administration/direction/delete/<int:pk>/', views.UserDeleteView.as_view(), name='direction_delete'),
    path('administration/direction/detail/<int:pk>/', views.DirectionDetailView.as_view(), name='direction_detail'),
    path('administration/departement/new/', views.DepartementCreateView.as_view(), name='departement_new'),
    path('administration/departement/list', views.DepartementListView.as_view(), name='departement_list'),
    path('administration/departement/edit/<int:pk>/', views.DepartementUpdateView.as_view(), name='departement_edit'),
    path('administration/departement/delete/<int:pk>/', views.DepartementDeleteView.as_view(), name='departement_delete'),
    path('administration/departement/detail/<int:pk>/', views.DepartementDetailView.as_view(), name='departement_detail'),
]