from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'price_per_night', 'max_guests', 'bedrooms', 'bathrooms',
            'property_type', 'amenities', 'is_available', 'host',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), 
        source='listing',
        write_only=True
    )
    
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_id', 'guest', 'check_in', 'check_out',
            'total_price', 'guests_count', 'status', 'special_requests',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'guest', 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(),
        source='booking',
        write_only=True
    )
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(),
        source='listing',
        write_only=True
    )
    
    class Meta:
        model = Review
        fields = [
            'id', 'booking', 'booking_id', 'guest', 'listing', 'listing_id',
            'rating', 'comment', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'guest', 'booking', 'listing', 'created_at', 'updated_at']