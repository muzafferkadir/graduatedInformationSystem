from django.urls import path
from .views import MessagesListView, MessagesDetailView, MessagesSendView

urlpatterns = [
    path('list/', MessagesListView.as_view(), name='messages_list'),
    path('detail/<int:user_id>/', MessagesDetailView.as_view(), name='messages_detail'),
    path('detail/<int:user_id>/send', MessagesSendView.as_view(), name='messages_send'),
]
