from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from adverts.models import Advertisement

class AdvertCreate(CreateView):
    model = Advertisement
    fields = ['title','description']
    template_name = 'createAdvert.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):#eğer form doğruysa
        form.instance.employer = self.request.user #şuanki kullanıcıyı renter olarak kaydet
        return super().form_valid(form)

class AdvertUpdate(UpdateView):
    model = Advertisement
    fields = ['title','description']
    template_name = 'updateAdvert.html'
    success_url = reverse_lazy('home')

class AdvertDelete(DeleteView):
    model = Advertisement
    template_name = 'deleteAdvert.html'
    success_url = reverse_lazy('home')

class AdvertList(ListView):
    model = Advertisement
    paginate_by = 3  # if pagination is desired
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class AdvertDetail(DetailView):
    model = Advertisement
    template_name = "detailAdvert.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context