from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Seed the database with sample data for ALX Travel App'
    
    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Create sample users
        users_data = [
            {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
            {'username': 'mike_wilson', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Wilson'},
            {'username': 'sarah_jones', 'email': 'sarah@example.com', 'first_name': 'Sarah', 'last_name': 'Jones'},
        ]
        
        users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                user.set_password('password123')
                user.save()
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')
        
        # Sample listings data
        listings_data = [
            {
                'title': 'Cozy Apartment in Downtown',
                'description': 'A beautiful cozy apartment located in the heart of downtown with amazing city views.',
                'address': '123 Main St',
                'city': 'New York',
                'country': 'USA',
                'price_per_night': 120.00,
                'max_guests': 4,
                'bedrooms': 2,
                'bathrooms': 1,
                'property_type': 'apartment',
                'amenities': 'WiFi, Kitchen, Air Conditioning, TV',
                'host': users[0],
            },
            {
                'title': 'Luxury Villa with Pool',
                'description': 'Stunning luxury villa with private pool and garden. Perfect for family vacations.',
                'address': '456 Beach Road',
                'city': 'Miami',
                'country': 'USA',
                'price_per_night': 350.00,
                'max_guests': 8,
                'bedrooms': 4,
                'bathrooms': 3,
                'property_type': 'villa',
                'amenities': 'Pool, WiFi, Kitchen, Air Conditioning, TV, Garden',
                'host': users[1],
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin in the mountains with breathtaking views and hiking trails nearby.',
                'address': '789 Mountain View',
                'city': 'Aspen',
                'country': 'USA',
                'price_per_night': 180.00,
                'max_guests': 6,
                'bedrooms': 3,
                'bathrooms': 2,
                'property_type': 'cabin',
                'amenities': 'Fireplace, WiFi, Kitchen, Hiking Trails',
                'host': users[0],
            },
            {
                'title': 'Modern Studio in City Center',
                'description': 'Modern and stylish studio apartment perfect for solo travelers or couples.',
                'address': '321 Central Ave',
                'city': 'San Francisco',
                'country': 'USA',
                'price_per_night': 95.00,
                'max_guests': 2,
                'bedrooms': 1,
                'bathrooms': 1,
                'property_type': 'studio',
                'amenities': 'WiFi, Kitchenette, Air Conditioning, TV',
                'host': users[2],
            },
            {
                'title': 'Spacious Family House',
                'description': 'Large family house with backyard and play area. Great for family gatherings.',
                'address': '654 Family Lane',
                'city': 'Austin',
                'country': 'USA',
                'price_per_night': 220.00,
                'max_guests': 10,
                'bedrooms': 5,
                'bathrooms': 3,
                'property_type': 'house',
                'amenities': 'Backyard, WiFi, Kitchen, Air Conditioning, TV, Play Area',
                'host': users[3],
            },
        ]
        
        listings = []
        for listing_data in listings_data:
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                city=listing_data['city'],
                defaults=listing_data
            )
            listings.append(listing)
            status = 'Created' if created else 'Exists'
            self.stdout.write(f'{status} listing: {listing.title}')
        
        # Create sample bookings
        booking_statuses = ['pending', 'confirmed', 'completed', 'cancelled']
        
        for i in range(10):
            listing = random.choice(listings)
            guest = random.choice([user for user in users if user != listing.host])
            
            check_in = datetime.now().date() + timedelta(days=random.randint(1, 30))
            check_out = check_in + timedelta(days=random.randint(1, 14))
            
            nights = (check_out - check_in).days
            total_price = listing.price_per_night * nights
            
            booking, created = Booking.objects.get_or_create(
                listing=listing,
                guest=guest,
                check_in=check_in,
                defaults={
                    'check_out': check_out,
                    'total_price': total_price,
                    'guests_count': random.randint(1, min(4, listing.max_guests)),
                    'status': random.choice(booking_statuses),
                    'special_requests': 'Early check-in requested' if random.choice([True, False]) else ''
                }
            )
            if created:
                self.stdout.write(f'Created booking: {guest.username} - {listing.title}')
        
        # Create sample reviews
        completed_bookings = Booking.objects.filter(status='completed')
        
        for booking in completed_bookings[:5]:  # Review first 5 completed bookings
            review, created = Review.objects.get_or_create(
                booking=booking,
                guest=booking.guest,
                defaults={
                    'listing': booking.listing,
                    'rating': random.randint(4, 5),
                    'comment': f'Great stay at {booking.listing.title}! Everything was perfect.'
                }
            )
            if created:
                self.stdout.write(f'Created review for: {booking.listing.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully seeded database with sample data!')
        )