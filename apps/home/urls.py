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
    path('indicateur/<int:pk>/', views.TbDetailView.as_view(), name='indicateur_detail'),
    path('indicateur/new/', views.TbCreateView.as_view(), name='indicateur_new'),
    path('indicateur/<int:pk>/edit/', views.TbUpdateView.as_view(), name='indicateur_edit'),
    path('indicateur/<int:pk>/delete/', views.TbDeleteView.as_view(), name='indicateur_delete'),
    path('listeIndicateurs/', views.ListeIndicateurView, name='liste_indicateurs'),
    path('listeDonnees/', views.ListeDonneesView, name ='liste_donnees'),
    ]
