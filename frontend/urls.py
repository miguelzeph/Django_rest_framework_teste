from django.urls import path

from .views import (
    home_page,
    create_model_task,
    delete_model_task,
    create_model_client,
    delete_model_client,
    )

urlpatterns = [
    path('',home_page, name='home'),
    path('create-task/',create_model_task,name='create_task'),
    path('delete-task/<str:pk>/',delete_model_task,name='delete_task'),
    path('create-client/',create_model_client,name='create_client'),
    path('delete-client/<str:pk>/',delete_model_client,name='delete_client'),

]
