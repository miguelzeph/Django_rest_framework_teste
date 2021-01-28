from django.urls import path, include

from .views import TaskViewSet, ClientViewSet


from rest_framework import routers
router = routers.DefaultRouter()
# Jeito Automático de fazer as routs
router.register(r'task',TaskViewSet, basename = 'task')
router.register(r'client',ClientViewSet)

urlpatterns = [
    # add routs de modo automático
    path('api/',include(router.urls)),
]
