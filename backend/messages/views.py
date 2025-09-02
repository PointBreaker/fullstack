from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class MessageDeleteView(generics.DestroyAPIView):
    # DestroyAPIView 专门处理DELETE请求
    # 它会根据URL中的ID自动找到对应的留言并删除
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class MessageEditView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer