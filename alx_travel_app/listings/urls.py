from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    # We'll add actual endpoints later
    path('', views.api_overview, name='api-overview'),
]
