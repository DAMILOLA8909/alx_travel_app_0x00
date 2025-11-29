from django.contrib import admin
from django.urls import path, include, re_path
from django.http import JsonResponse
from rest_framework import permissions

# Conditional import for Swagger
try:
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    SWAGGER_AVAILABLE = True
except ImportError:
    SWAGGER_AVAILABLE = False

if SWAGGER_AVAILABLE:
    schema_view = get_schema_view(
        openapi.Info(
            title="ALX Travel App API",
            default_version='v1',
            description="ALX Travel App API Documentation",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@alxtravel.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

def api_root(request):
    endpoints = {
        'message': 'ALX Travel App API',
        'endpoints': {
            'listings': '/api/listings/',
            'bookings': '/api/bookings/ (requires authentication)',
            'reviews': '/api/reviews/',
            'admin': '/admin/',
        }
    }
    if SWAGGER_AVAILABLE:
        endpoints['endpoints']['swagger'] = '/swagger/'
        endpoints['endpoints']['redoc'] = '/redoc/'
    return JsonResponse(endpoints)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),
    path('', api_root, name='api-root'),
]

if SWAGGER_AVAILABLE:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]