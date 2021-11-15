from django.db.models.base import Model
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.views.generic.edit import FormView
from .forms import EntryForm
from .models import Entry, Category


class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        return context

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria", '')
        # consulta de busqueda
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado

class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"

class NewEntry(CreateView):
    template_name = "entrada/newentry.html"
    form_class = EntryForm
    success_url = reverse_lazy('entrada_app:entry-lista')