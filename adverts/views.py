from django.urls import reverse_lazy,reverse,path
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from adverts.models import Advertisement
from django.http import  HttpResponseRedirect

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

    def get(self, request, *args, **kwargs):#sadece kendi objelerini düzenleyebilir
        self.object = self.get_object()
        if self.object.employer.student_no != request.user.student_no:
            return HttpResponseRedirect(reverse('detail-advert', kwargs={'pk': self.object.pk}))
        return super().get(request, *args, **kwargs)       

class AdvertDelete(DeleteView):
    model = Advertisement
    template_name = 'deleteAdvert.html'
    success_url = reverse_lazy('home')
    
    def get(self, request, *args, **kwargs):#sadece kendi objelerini düzenleyebilir
        self.object = self.get_object()
        if self.object.employer.student_no != request.user.student_no:
            return HttpResponseRedirect(reverse('detail-advert', kwargs={'pk': self.object.pk}))
        return super().get(request, *args, **kwargs)  

class AdvertList(ListView):
    model = Advertisement
    paginate_by = 30  # if pagination is desired
    template_name = "profile.html"

    def get_queryset(self):
        return Advertisement.objects.filter(employer=self.request.user)

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