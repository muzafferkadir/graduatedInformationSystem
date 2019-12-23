from django.urls import path
from adverts.views import *
urlpatterns = [
    path('advert/add/', AdvertCreate.as_view(), name='add-advert'),
    path('advert/<int:pk>/update', AdvertUpdate.as_view(), name='update-advert'),
    path('advert/<int:pk>/delete/', AdvertDelete.as_view(), name='delete-advert'),
    path('advert/<int:pk>/', AdvertDetail.as_view(), name='detail-advert'),
    path('profile/', AdvertList.as_view(), name='profile'),
]