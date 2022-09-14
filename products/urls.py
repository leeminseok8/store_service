from django.urls import path

from .views import ProductPostView, ProductDetailView

urlpatterns = [
    path("", ProductPostView.as_view()),
    path("<int:pk>", ProductDetailView.as_view()),
]
