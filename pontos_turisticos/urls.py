from pontos_turisticos import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'pontos-turisticos/', views.ListarPontosTuristicos.as_view()),
    path(r'pontos-turisticos/<int:pk>/', views.DetalharPontosTuristicos.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
