from django.urls import path
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_review/',AddReviewView.as_view(),name='add_review'),
    path('review/',ReviewListView.as_view(),name='review')
]