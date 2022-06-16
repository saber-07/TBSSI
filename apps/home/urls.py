from django.urls import path
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
    path('data/new/<int:pk>', views.DataCreateView.as_view(), name='data_new'),
    path('data/filiale/new/<int:pk>', views.DataFilialeCreateView.as_view(), name='data_filiale_new'),
    path('data/application/new/<int:pk>', views.DataAppCreateView.as_view(), name='data_app_new'),
    path('data/mesure/new/<int:pk>', views.DataMesureCreateView.as_view(), name='data_mesure_new'),
    path('data/detail/<int:pk>/', views.DataDetailView.as_view(), name='data_detail'),
    path('data/<int:pk>/delete/', views.DataDeleteView.as_view(), name='data_delete'),
    path('data/filiale/<int:pk>/delete/', views.DataFilialeDeleteView.as_view(), name='data_filiale_delete'),
    path('data/application/<int:pk>/delete/', views.DataAppDeleteView.as_view(), name='data_app_delete'),
    path('data/mesure/<int:pk>/delete/', views.DataMesureDeleteView.as_view(), name='data_mesure_delete'),
    path('data/<int:pk>/update/', views.DataUpdateView.as_view(), name='data_update'),
    path('data/filiale/<int:pk>/update/', views.DataFilialeUpdateView.as_view(), name='data_filiale_update'),
    path('data/application/<int:pk>/update/', views.DataAppUpdateView.as_view(), name='data_app_update'),
    path('data/mesure/<int:pk>/update/', views.DataMesureUpdateView.as_view(), name='data_mesure_update'),
    path('validation/indicateur/directeurlist/', views.ValidationIndicateurDirecteurListView.as_view(), name='validation_indicateur_directeur'),
    path('validation/indicateur/directeur/<int:pk>/', views.ValidationIndicateurDirecteurDetailView.as_view(), name='indicateur_detail'),
    path('validation/indicateur/chefdeplist/', views.ValidationIndicateurChefDepListView.as_view(), name='validation_indicateur_chefdep'),
    path('validation/indicateur/chefdep/<int:pk>/', views.ValidationIndicateurChefDepDetailView.as_view(), name='indicateur_detail'),

    #for graphe
    path('administration/graphe/new/', views.GrapheCreateView.as_view(), name='graphe_new'),
    path('administration/graphe/list', views.GrapheListView.as_view(), name='graphelist'),
    path('administration/graphe/delete/<int:pk>/', views.GrapheDeleteView.as_view(), name='graphe_delete'),
    path('administration/graphe/detail/<int:pk>/', views.GrapheDetailView.as_view(), name='graphe_detail'),
   
    #for interpretation
    path('interpretation/new/<int:pk>', views.InterpretationCreateView.as_view(), name='interpretation_new'),
    
    path('interpretation/detail/<int:pk>/', views.InterpretationDetailView.as_view(), name='interpretation_detail'),

    path('interpretation/<int:pk>/edit', views.InterpretationUpdateView.as_view(), name='interpretation_edit'),

    path('validation/interpretation/directeurlist/', views.ValidationInterpretationDirecteurListView.as_view(), name='validation_interpretation_directeur'),
    path('validation/interpretation/directeur/<int:pk>/', views.ValidationInterpretationDirecteurDetailView.as_view(), name='interpretation_detail'),
    path('validation/interpretation/chefdeplist/', views.ValidationInterpretationChefDepListView.as_view(), name='validation_interpretation_chefdep'),
    path('validation/interpretation/chefdep/<int:pk>/', views.ValidationInterpretationChefDepDetailView.as_view(), name='interpretation_detail'),

    #for administration
    path('administration/', views.administrationView, name='administration'),

    #for validation
    path('valider_indicateur/<int:pk>', views.valider_ind, name='valider-indicateur'), 
    path('valider_indicateur_bis/<int:pk>', views.valider_ind_Bis, name='valider-indicateur-bis'),
    

    path('valider_interpretation/<int:pk>', views.valider_inter, name='valider-inter'), 
    path('valider_interpretation_bis/<int:pk>', views.valider_inter_Bis, name='valider-inter-bis'),
    
    
    path('valider_rapport/<int:pk>', views.valider_rapport, name='valider-rapport'), 

    path('refus-indicateur/<int:pk>', views.refus_indicateur, name='refus-indicateur'),

    path('refus-inter/<int:pk>', views.refus_inter, name='refus-inter'),

    
    path('refus-indicateur/<int:pk>', views.refus_indicateur, name='refus-indicateur'),
    ]