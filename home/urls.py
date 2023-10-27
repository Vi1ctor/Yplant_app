from django.urls import path
from home.views import index, classify, results, classifyForm, filterForm, filter, removeItem
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('classify', classify, name='classify'),
    path('results/<int:objeto_id>/', results, name='results'),
    path('classifyForm', classifyForm, name='classifyForm'),
    path('filterForm', filterForm, name='filterForm'),
    path("filter", filter , name='filter'),
    path('remover/<int:objeto_id>/', removeItem, name='removeItem'),
]