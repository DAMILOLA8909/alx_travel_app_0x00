from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_overview(request):
    """
    API Overview
    """
    api_urls = {
        'Admin Interface': '/admin/',
        'Swagger Documentation': '/swagger/',
        'ReDoc Documentation': '/redoc/',
        'Listings API': '/api/listings/',
    }
    return Response(api_urls)