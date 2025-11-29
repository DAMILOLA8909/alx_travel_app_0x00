from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing property listings.
    
    Provides full CRUD operations for property listings.
    Authenticated users can create listings, everyone can view listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """Automatically set the host to the current user when creating a listing."""
        serializer.save(host=self.request.user)
    
    @swagger_auto_schema(
        operation_description="Retrieve all bookings for a specific listing",
        responses={200: BookingSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def bookings(self, request, pk=None):
        """
        Get all bookings for a specific listing.
        
        Returns a list of all bookings associated with this property listing.
        """
        listing = self.get_object()
        bookings = Booking.objects.filter(listing=listing)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Retrieve all reviews for a specific listing",
        responses={200: ReviewSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """
        Get all reviews for a specific listing.
        
        Returns a list of all reviews associated with this property listing.
        """
        listing = self.get_object()
        reviews = Review.objects.filter(listing=listing)
        serializer = ReviewSerializer(reviews, many=True)
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
        """
        Return only bookings for the authenticated user.
        
        Non-staff users can only see their own bookings.
        Staff users can see all bookings.
        """
        # Fix for Swagger schema generation
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()
            
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(guest=self.request.user)
    
    def perform_create(self, serializer):
        """Automatically set the guest to the current user when creating a booking."""
        serializer.save(guest=self.request.user)

class ReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing property reviews.
    
    Provides full CRUD operations for property reviews.
    Users can only manage their own reviews, but anyone can read reviews.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        """
        Return reviews based on user permissions.
        
        Staff users can see all reviews.
        Regular users can only see their own reviews.
        Anonymous users can see all reviews (read-only).
        """
        # Fix for Swagger schema generation
        if getattr(self, 'swagger_fake_view', False):
            return Review.objects.none()
            
        if self.request.user.is_staff:
            return Review.objects.all()
        elif self.request.user.is_authenticated:
            return Review.objects.filter(guest=self.request.user)
        return Review.objects.all()
    
    def perform_create(self, serializer):
        """Automatically set the guest to the current user when creating a review."""
        serializer.save(guest=self.request.user)