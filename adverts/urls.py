from django.urls import path
from adverts.views import AdvertCreate,AdvertUpdate,AdvertDelete
urlpatterns = [
    path('advert/add/', AdvertCreate.as_view(), name='add-advert'),
    path('advert/<int:pk>/', AdvertUpdate.as_view(), name='update-advert'),
    path('advert/<int:pk>/delete/', AdvertDelete.as_view(), name='delete-advert'),
]