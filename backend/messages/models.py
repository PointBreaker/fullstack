from django.db import models

class Message(models.Model):
    content = models.TextField(verbose_name="留言内容")
    author = models.CharField(max_length=100, verbose_name="作者")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    class Meta:
        verbose_name = "留言"
        verbose_name_plural = "留言"
        ordering = ['-created_at']  # 按创建时间倒序
    
    def __str__(self):
        return f"{self.author}: {self.content[:20]}"