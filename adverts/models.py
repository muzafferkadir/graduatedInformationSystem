from django.db import models
from users.models import UserTable
class Advertisement(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=2000, blank=False)
    employer = models.ForeignKey(UserTable,on_delete=models.CASCADE)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail-advert', args=[str(self.id)])
    #company
    #position