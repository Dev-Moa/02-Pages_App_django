from django.urls import path
from .views import HomePageView,AboutPageView,FooterPageView
urlpatterns = [
    path("footer/", FooterPageView.as_view(), name="footer"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('',HomePageView.as_view(),name='home')
]
