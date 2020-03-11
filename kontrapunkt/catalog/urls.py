from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('country_list/', views.CountryListView.as_view(), name='country_list'),
    path('country/<int:pk>', views.CountryDetailView.as_view(), name='country_detail'),
    path('country/create/', views.CountryCreate.as_view(), name='country_create'),
    path('country/<int:pk>/update/', views.CountryUpdate.as_view(), name='country_update'),
    path('country/<int:pk>/delete/', views.CountryDelete.as_view(), name='country_delete'),
    
#    path('country_list/', views.CountryListView.as_view(), name='country_list'),
    
    path('composer_list/', views.ComposerListView.as_view(), name='composer_list'),
    path('composer/<int:pk>', views.ComposerDetailView.as_view(), name='composer_detail'),
    path('composer/create/', views.ComposerCreate.as_view(), name='composer_create'),
    path('composer/<int:pk>/update/', views.ComposerUpdate.as_view(), name='composer_update'),
    path('composer/<int:pk>/delete/', views.ComposerDelete.as_view(), name='composer_delete'),
    
    path('composition_list/', views.CompositionListView.as_view(), name='composition_list'),
    path('composition/<int:pk>', views.CompositionDetailView.as_view(), name='composition_detail'),
    path('composition/create/', views.CompositionCreate.as_view(), name='composition_create'),
    path('composition/<int:pk>/update/', views.CompositionUpdate.as_view(), name='composition_update'),
    path('composition/<int:pk>/delete/', views.CompositionDelete.as_view(), name='composition_delete'),
    
]
