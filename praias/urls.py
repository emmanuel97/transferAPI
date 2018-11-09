from praias import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'praias/', views.ListarPraias.as_view()),
    path(r'praias/<int:pk>/', views.DetalharPraias.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
