from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/<int:num_page>/', views.dynamic_mapping_view),
    path('topics/<str:topic>/', views.dynamic_view, name='topic-page'),
    path('sum/<int:num_1>/<int:num_2>', views.sum),
    path('template/', views.template_example, name='template')
]
