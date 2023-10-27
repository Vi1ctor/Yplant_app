from django.urls import path
from classify.views import classify

urlpatterns = [
    path('', classify, name='index'),
    # Adicione outros padrões de URL conforme necessário
]