from django.contrib import admin
from django.urls import path, include, re_path
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version='v1',
        description="""
        ALX Travel App API Documentation
        
        This API provides endpoints for managing property listings and bookings.
        
        ## Authentication
        - Listings: Read operations are public, write operations require authentication
        - Bookings: All operations require authentication
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@alxtravel.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def api_root(request):
    """API root endpoint showing available endpoints."""
    return JsonResponse({
        'message': 'ALX Travel App API',
        'endpoints': {
            'listings': '/api/listings/',
            'bookings': '/api/bookings/',
            'admin': '/admin/',
            'swagger': '/swagger/',
            'redoc': '/redoc/',
        },
        'documentation': 'Visit /swagger/ for interactive API documentation'
    })

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', include('listings.urls')),
    
    # Swagger documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', 
            schema_view.without_ui(cache_timeout=0), 
            name='schema-json'),
    path('swagger/', 
         schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),
    path('redoc/', 
         schema_view.with_ui('redoc', cache_timeout=0), 
         name='schema-redoc'),
    
    # Root
    path('', api_root, name='api-root'),
]