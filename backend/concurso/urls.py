from django.urls import path
from .views import InscripcionView

urlpatterns = [
    path('inscripcion/', InscripcionView.as_view(), name='inscripcion'),
]