from django.urls import path
from . import views

app_name = 'app_example'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/<int:num_page>/', views.dynamic_mapping_view, name='topic-numbers'),
    path('topics/<str:topic>/', views.dynamic_view, name='topic-page'),
    path('sum/<int:num_1>/<int:num_2>', views.sum, name='sum'),
    path('template/', views.template_example, name='template'),
    path('transactions/', views.all_transactions, name='transactions'),
    path('links/', views.links, name='links'),
]
