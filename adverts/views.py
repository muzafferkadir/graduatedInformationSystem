from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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
