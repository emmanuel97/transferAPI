from artigos import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'artigos/', views.ListarArtigos.as_view()),
    path(r'artigos/<int:pk>/', views.DetalharArtigos.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
