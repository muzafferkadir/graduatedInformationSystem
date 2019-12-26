from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from adverts.models import Advertisement
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class MainList(ListView):
    model = Advertisement
    paginate_by = 30  # if pagination is desired
    template_name = "home.html"
    queryset = Advertisement.objects.all().order_by('-id')