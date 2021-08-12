from django.urls import path
from profiles_api import views

urlpatterns = [
    path('first-view', views.FirstAPIView.as_view()),
    ]
