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

    path('tbb/detail/<int:pk>/', views.TbDetail.as_view(), name='tbb_detail'),
    path('tbb/new/', views.TbCreateView.as_view(), name='tbb_new'),
    path('tbb/<int:pk>/edit/', views.TbUpdateView.as_view(), name='tbb_edit'),
    path('tbb/<int:pk>/delete/', views.TbDeleteView.as_view(), name='tbb_delete'),
    path('indicateur/new/', views.IndicateurCreateView.as_view(), name='indicateur_new'),
    path('indicateur/<int:pk>/', views.IndicateurDetailView.as_view(), name='indicateur_detail'),
    path('listeIndicateurs/', views.listeindicateurview, name='liste_indicateurs'),
    path('indicateur/<int:pk>/edit', views.IndicateurUpdateView.as_view(), name='indicateur_edit'),
    path('indicateur/<int:pk>/delete', views.IndicateurDeleteView.as_view(), name='indicateur_delete'),
    path('listeDonnees/', views.listedonneesview, name ='liste_donnees'),
    path('data/new/', views.DataCreateView.as_view(), name='data_new'),
    path('data/detail/<int:pk>/', views.DataDetailView.as_view(), name='data_detail'),
    path('data/<int:pk>/delete/', views.DataDeleteView.as_view(), name='data_delete'),
    path('data/<int:pk>/update/', views.DataUpdateView.as_view(), name='data_update'),

    #for administration
    path('administration/', views.administrationView, name='administration'),
    ]
