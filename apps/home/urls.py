# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

    path('indicateur/list/<int:pk>/', views.TbListView.as_view(), name='indicateur_list'),
    path('tbb/new/', views.TbCreateView.as_view(), name='tbb_new'),
    path('tbb/<int:pk>/edit/', views.TbUpdateView.as_view(), name='tbb_edit'),
    path('tbb/<int:pk>/delete/', views.TbDeleteView.as_view(), name='tbb_delete'),
    path('indicateur/<int:pk>/', views.IndicateurDetailView.as_view(), name='indicateur_detail'),
    path('indicateur/new/', views.IndicateurCreateView.as_view(), name='indicateur_new'),
]
