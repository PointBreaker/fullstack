from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    # RetrieveUpdateDestroyAPIView 支持 GET、PUT、PATCH、DELETE 方法
    # GET: 获取单个留言详情
    # PUT/PATCH: 更新留言
    # DELETE: 删除留言
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    