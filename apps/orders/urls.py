from django.urls import path

from .views import OrderCreateView, OrderDetailView

urlpatterns = [
    path("", OrderCreateView.as_view()),
    path("<int:pk>", OrderDetailView.as_view()),
]
