from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing property listings.
    
    Provides full CRUD operations for property listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """Set the host to the current user when creating a listing."""
        serializer.save(host=self.request.user)
    
    @action(detail=True, methods=['get'])
    def bookings(self, request, pk=None):
        """Get all bookings for a specific listing."""
        listing = self.get_object()
        bookings = Booking.objects.filter(listing=listing)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing property bookings.
    
    Provides full CRUD operations for property bookings.
    Users can only view and manage their own bookings.
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Return only bookings for the authenticated user."""
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()
            
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(guest=self.request.user)
    
    def perform_create(self, serializer):
        """Set the guest to the current user when creating a booking."""
        serializer.save(guest=self.request.user)