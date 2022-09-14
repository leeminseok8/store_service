from django.urls import path

from .views import ProductPostView

urlpatterns = [path("", ProductPostView.as_view())]
