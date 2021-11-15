#
from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
   path(
        'entradas/', 
        views.EntryListView.as_view(),
        name='entry-lista',
    ),
    path(
        'entradas/<slug>/', 
        views.EntryDetailView.as_view(),
        name='entry-detail',
    ),
    path(
        'nueva-entrada', 
        views.NewEntry.as_view(),
        name='new-entry',
    ),
]