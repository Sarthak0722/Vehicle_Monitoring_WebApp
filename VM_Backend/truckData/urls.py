from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TruckViewSet

# Create a DefaultRouter instance for automatic URL routing
router = DefaultRouter()

# Register the TruckViewSet with the router under the 'trucks' path
router.register(r'trucks', TruckViewSet)

urlpatterns = [
    # Include all URLs generated by the DefaultRouter
    # This will include routes for CRUD operations on the 'trucks' endpoint
    path('', include(router.urls)),
]
