from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'listings', views.ListingViewSet, basename='listing')
router.register(r'bookings', views.BookingViewSet, basename='booking')

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]