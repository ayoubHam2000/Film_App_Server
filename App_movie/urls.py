from django.urls import path

from .views import (
    TestView
)

app_name = "App_movie"

urlpatterns = [
    path('', TestView.as_view(), name = 'test'),
]