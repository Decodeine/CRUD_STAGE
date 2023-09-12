from django.urls import path
from .views import PersonCreateView, PersonRetrieveUpdateDeleteView

urlpatterns = [
    path('', PersonCreateView.as_view(), name='person-list-create'),
    path('<str:pk_or_name>/', PersonRetrieveUpdateDeleteView.as_view(), name='person-detail'),
]
