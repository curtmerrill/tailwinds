from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import CustomUserCreationForm
from entries.models import Entry


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class DashboardView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')

    model = Entry
    paginate_by = 50
    context_object_name = 'entry_list'
    template_name = 'pilots/dashboard.html'

    def get_queryset(self):
        return Entry.objects.filter(author=self.request.user)
