from cidades import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'cidades/', views.ListarCidades.as_view()),
    path(r'cidades/<int:pk>/', views.DetalharCidades.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
