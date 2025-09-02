from django.urls import path
from .views import MessageEditView, MessageListCreateView, MessageDeleteView

urlpatterns = [
    path('', MessageListCreateView.as_view(), name='message-list-create'),
    path('<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
    path('<int:pk>/put/', MessageEditView.as_view(), name='message-edit')
]