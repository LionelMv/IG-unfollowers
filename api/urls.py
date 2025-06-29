from django.urls import path
from .views import CheckFollowersView


urlpatterns = [
    path('check/', CheckFollowersView.as_view(), name='check-followers'),
]
