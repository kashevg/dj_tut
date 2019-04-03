from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='polls_index_url'),
    path('poll/<str:id>/', details, name='poll_details_url')
]
