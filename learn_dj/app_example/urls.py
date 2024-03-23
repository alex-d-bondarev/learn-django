from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<topic>/', views.dynamic_view),
    path('<int:num_1>/<int:num_2>', views.sum),
]
