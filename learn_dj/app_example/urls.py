from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num_page>/', views.dynamic_mapping_view),
    path('<str:topic>/', views.dynamic_view),
    path('<int:num_1>/<int:num_2>', views.sum),
]
