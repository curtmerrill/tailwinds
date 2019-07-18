from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.CreateEntryView.as_view(), name='new_entry'),
]
