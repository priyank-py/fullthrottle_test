from django.urls import path
from .views import CountryAutocomplete

urlpatterns = [
    path(
        '',
        CountryAutocomplete.as_view(),
        name='country-autocomplete',
    ),
]