from django.urls import path
from trombil3.views import index, detail
from . import views
urlpatterns = [
   path('',index,name='home'),
   path('cv/', views.detail, name='detail'),
   path('cv/<int:personne_id>/', views.afficher_cv, name='afficher_cv'),
]

