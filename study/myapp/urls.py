from django.urls import path
from . import views 

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('search_results/', views.search_results, name='search_results'),
    path('three/', views.three, name='three'),
    path('search_subject/', views.search_subject, name='search_subject'),
    path('subject/', views.subject, name='subject'),
    path('four/', views.four_subject, name='four'),
]