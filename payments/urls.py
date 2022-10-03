from django.urls import path

from .views import PaymentCreateView, PaymentDeleteView

urlpatterns = [
    path("", PaymentCreateView.as_view()),
    path("<int:pk>", PaymentDeleteView.as_view()),
]
