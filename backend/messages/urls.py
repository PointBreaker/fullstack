from django.urls import path
from .views import MessageListCreateView, MessageDeleteView

urlpatterns = [
    path('', MessageListCreateView.as_view(), name='message-list-create'),
    path('<int:pk>/', MessageDeleteView.as_view(), name='message-delete')
]