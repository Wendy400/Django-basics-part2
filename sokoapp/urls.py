from django.urls import path
from sokoapp import views

urlpatterns = [
    
    path('error/', views.error, name='error'),
    path('details/', views.details, name='details'),
    path('blog/', views.blog, name='blog'),
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
]