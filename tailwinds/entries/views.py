from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import EntryCreationForm
from .models import Entry

# Create your views here.
class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'entries/new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
