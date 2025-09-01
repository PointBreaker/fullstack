# Vue.js + Element UI + Django REST Framework 入门教程

## 📋 教程概述

本教程将指导你从零开始创建一个简单的"用户留言板"系统，这是一个最基础但完整的前后端分离项目。通过这个项目，你将学会：

- Django REST Framework 如何创建API
- Vue.js 如何调用后端API
- 前后端如何协作完成一个完整功能

## 🎯 项目目标

创建一个简单的留言板，用户可以：
1. 查看所有留言（GET请求）
2. 添加新留言（POST请求）

这个功能虽然简单，但涵盖了前后端交互的核心流程。

## 🚀 第一阶段：环境准备

### 1.1 创建项目目录
```bash
mkdir message-board
cd message-board
```

### 1.2 后端环境准备
```bash
mkdir backend
cd backend
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或 venv\Scripts\activate  # Windows
```

### 1.3 安装后端依赖
```bash
pip install django
pip install djangorestframework
pip install django-cors-headers
pip freeze > requirements.txt
```

**作用说明：**
- `django`: Web框架核心
- `djangorestframework`: 提供REST API功能
- `django-cors-headers`: 解决前后端跨域问题

### 1.4 创建Django项目
```bash
django-admin startproject config .
python manage.py startapp messages
```

**预期效果：** 你会看到创建了`config`目录和`messages`目录

## 🔧 第二阶段：配置Django后端

### 2.1 修改Django配置文件

**文件位置：** `backend/config/settings.py`

**需要修改的内容：**
1. 在`INSTALLED_APPS`中添加：
   ```python
   'rest_framework',
   'corsheaders',
   'messages',
   ```

2. 在`MIDDLEWARE`最顶部添加：
   ```python
   'corsheaders.middleware.CorsMiddleware',
   ```

3. 在文件末尾添加：
   ```python
   # CORS设置
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:8080",
   ]
   
   # REST Framework配置
   REST_FRAMEWORK = {
       'DEFAULT_PERMISSION_CLASSES': [
           'rest_framework.permissions.AllowAny',
       ]
   }
   ```

**作用说明：**
- CORS配置允许前端（8080端口）访问后端（8000端口）
- REST Framework配置暂时允许所有人访问API（简化学习）

### 2.2 创建数据模型

**文件位置：** `backend/messages/models.py`

**需要添加的内容：**
```python
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
```

**作用说明：**
- 定义了留言的数据结构：内容、作者、创建时间
- `ordering`让最新留言显示在前面

### 2.3 创建API序列化器

**文件位置：** `backend/messages/serializers.py`（新建文件）

**需要添加的内容：**
```python
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'author', 'created_at']
        read_only_fields = ['id', 'created_at']
```

**作用说明：**
- 序列化器负责将Python对象转换为JSON格式
- 定义了哪些字段可以被API访问

### 2.4 创建API视图

**文件位置：** `backend/messages/views.py`

**需要替换的内容：**
```python
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
```

**作用说明：**
- `ListCreateAPIView`自动提供GET（获取列表）和POST（创建）功能
- 这是Django REST Framework的便捷类，减少代码量

### 2.5 配置URL路由

**文件位置：** `backend/messages/urls.py`（新建文件）

**需要添加的内容：**
```python
from django.urls import path
from .views import MessageListCreateView

urlpatterns = [
    path('', MessageListCreateView.as_view(), name='message-list-create'),
]
```

**文件位置：** `backend/config/urls.py`

**需要修改的内容：**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/messages/', include('messages.urls')),
]
```

**作用说明：**
- 配置API访问路径：`/api/messages/`
- 将messages应用的URL包含到主项目中

### 2.6 运行数据库迁移

**执行命令：**
```bash
python manage.py makemigrations
python manage.py migrate
```

**预期效果：**
- 看到"Create model Message"的迁移信息
- 数据库中创建了messages_message表

### 2.7 启动后端服务

**执行命令：**
```bash
python manage.py runserver
```

**预期效果：**
- 服务运行在 http://127.0.0.1:8000
- 访问 http://127.0.0.1:8000/api/messages/ 应该看到空的JSON列表：`[]`

## 🎨 第三阶段：创建Vue.js前端

### 3.1 创建前端项目

**在新终端中执行：**
```bash
cd .. # 回到message-board目录
npx @vue/cli create frontend
```

**选择配置：**
- Manually select features
- 选择：Babel, Router, CSS Pre-processors
- Vue version: 2.x
- Use history mode: Yes
- CSS pre-processor: Sass/SCSS

### 3.2 安装前端依赖

```bash
cd frontend
npm install element-ui
npm install axios
```

**作用说明：**
- `element-ui`: 提供美观的UI组件
- `axios`: 用于发送HTTP请求到后端API

### 3.3 配置Element UI和axios

**文件位置：** `frontend/src/main.js`

**需要修改的内容：**
```javascript
import Vue from 'vue'
import App from './App.vue'
import router from './router'

// 引入Element UI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

// 引入axios
import axios from 'axios'

Vue.use(ElementUI)

// 配置axios
axios.defaults.baseURL = 'http://127.0.0.1:8000/api'
Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

**作用说明：**
- 全局注册Element UI组件
- 配置axios的基础URL，简化API调用

## 🔧 第四阶段：创建留言板页面

### 4.1 创建留言板组件

**文件位置：** `frontend/src/views/MessageBoard.vue`（新建文件）

**需要添加的内容：**
```vue
<template>
  <div class="message-board">
    <el-container>
      <el-header>
        <h1>简单留言板</h1>
      </el-header>
      
      <el-main>
        <!-- 添加留言表单 -->
        <el-card class="add-message-card">
          <div slot="header">
            <span>添加新留言</span>
          </div>
          
          <el-form :model="newMessage" ref="messageForm">
            <el-form-item label="作者" required>
              <el-input v-model="newMessage.author" placeholder="请输入你的名字"></el-input>
            </el-form-item>
            
            <el-form-item label="留言内容" required>
              <el-input 
                type="textarea" 
                v-model="newMessage.content" 
                placeholder="请输入留言内容"
                :rows="3"
              ></el-input>
            </el-form-item>
            
            <el-form-item>
              <el-button type="primary" @click="addMessage" :loading="submitting">
                提交留言
              </el-button>
            </el-form-item>
          </el-form>
        </el-card>
        
        <!-- 留言列表 -->
        <el-card class="messages-list">
          <div slot="header">
            <span>所有留言 ({{ messages.length }}条)</span>
            <el-button style="float: right;" @click="loadMessages" :loading="loading">
              刷新
            </el-button>
          </div>
          
          <div v-if="loading" style="text-align: center;">
            <el-icon class="el-icon-loading"></el-icon> 加载中...
          </div>
          
          <div v-else-if="messages.length === 0" style="text-align: center; color: #999;">
            暂无留言，快来添加第一条吧！
          </div>
          
          <div v-else>
            <el-card v-for="message in messages" :key="message.id" class="message-item">
              <div class="message-content">{{ message.content }}</div>
              <div class="message-meta">
                <span class="author">— {{ message.author }}</span>
                <span class="time">{{ formatTime(message.created_at) }}</span>
              </div>
            </el-card>
          </div>
        </el-card>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'MessageBoard',
  data() {
    return {
      messages: [],
      loading: false,
      submitting: false,
      newMessage: {
        author: '',
        content: ''
      }
    }
  },
  
  mounted() {
    this.loadMessages()
  },
  
  methods: {
    // 加载所有留言
    async loadMessages() {
      this.loading = true
      try {
        const response = await this.$http.get('/messages/')
        this.messages = response.data
        console.log('加载留言成功:', response.data)
      } catch (error) {
        console.error('加载留言失败:', error)
        this.$message.error('加载留言失败，请检查网络连接')
      } finally {
        this.loading = false
      }
    },
    
    // 添加新留言
    async addMessage() {
      if (!this.newMessage.author || !this.newMessage.content) {
        this.$message.warning('请填写作者和留言内容')
        return
      }
      
      this.submitting = true
      try {
        const response = await this.$http.post('/messages/', this.newMessage)
        console.log('添加留言成功:', response.data)
        this.$message.success('留言添加成功！')
        
        // 清空表单
        this.newMessage = { author: '', content: '' }
        
        // 重新加载留言列表
        this.loadMessages()
      } catch (error) {
        console.error('添加留言失败:', error)
        this.$message.error('添加留言失败，请重试')
      } finally {
        this.submitting = false
      }
    },
    
    // 格式化时间
    formatTime(timeString) {
      const date = new Date(timeString)
      return date.toLocaleString('zh-CN')
    }
  }
}
</script>

<style scoped>
.message-board {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.add-message-card {
  margin-bottom: 20px;
}

.message-item {
  margin-bottom: 10px;
}

.message-content {
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 10px;
}

.message-meta {
  display: flex;
  justify-content: space-between;
  color: #666;
  font-size: 14px;
}

.author {
  font-weight: bold;
}

.time {
  font-style: italic;
}
</style>
```

### 4.2 配置路由

**文件位置：** `frontend/src/router/index.js`

**需要修改的内容：**
```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import MessageBoard from '../views/MessageBoard.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/messages',
    name: 'MessageBoard',
    component: MessageBoard
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
```

### 4.3 修改首页添加导航

**文件位置：** `frontend/src/views/Home.vue`

**需要修改的内容：**
```vue
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>欢迎来到留言板系统</h1>
    <div style="margin-top: 30px;">
      <el-button type="primary" size="large" @click="$router.push('/messages')">
        进入留言板
      </el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>
```

## 🚀 第五阶段：测试完整功能

### 5.1 启动服务

**后端（保持运行）：**
```bash
cd backend
source venv/bin/activate
python manage.py runserver
```

**前端（新终端）：**
```bash
cd frontend
npm run serve
```

### 5.2 测试流程

1. **访问首页**
   - 打开浏览器访问：http://localhost:8080
   - 点击"进入留言板"按钮

2. **测试添加留言**
   - 填写作者名字
   - 填写留言内容
   - 点击"提交留言"
   - **预期效果：** 看到成功提示，表单清空，留言出现在下方列表

3. **测试查看留言**
   - 刷新页面
   - **预期效果：** 之前添加的留言依然存在
   - 点击"刷新"按钮
   - **预期效果：** 重新加载留言列表

4. **测试多条留言**
   - 添加多条不同的留言
   - **预期效果：** 最新留言显示在最上方

## 🐛 调试和验证

### 调试技巧

1. **后端API测试**
   - 直接访问：http://127.0.0.1:8000/api/messages/
   - 应该看到JSON格式的留言数据

2. **前端调试**
   - 打开浏览器开发者工具（F12）
   - 查看Console标签页的日志输出
   - 查看Network标签页的API请求

3. **数据验证**
   - 后端：访问 http://127.0.0.1:8000/admin （需要先创建超级用户）
   - 前端：在浏览器Console中输入 `console.log(this.messages)` 查看数据

### 常见问题排查

1. **CORS错误**
   - 检查Django settings.py中的CORS配置
   - 确保前端运行在8080端口

2. **API 404错误**
   - 检查URL配置是否正确
   - 确认后端服务正在运行

3. **数据不显示**
   - 检查浏览器Console是否有JavaScript错误
   - 确认API返回的数据格式

## 🎯 学习总结

通过这个简单的留言板项目，你学会了：

### 后端技能
- Django项目结构和配置
- 数据模型定义
- REST API创建
- 序列化器使用
- URL路由配置

### 前端技能
- Vue.js组件开发
- Element UI组件使用
- axios HTTP请求
- 数据绑定和事件处理
- 路由配置

### 前后端协作
- API接口设计
- 跨域问题解决
- 数据格式统一
- 错误处理

## 🚀 下一步扩展

完成基础功能后，你可以尝试：

1. **添加删除功能**
   - 后端：添加DELETE API
   - 前端：添加删除按钮

2. **添加编辑功能**
   - 后端：添加PUT API
   - 前端：添加编辑表单

3. **添加用户认证**
   - 实现登录/注册功能
   - 只有登录用户才能留言

4. **美化界面**
   - 添加更多CSS样式
   - 使用更多Element UI组件

这个基础项目为你提供了完整的前后端开发流程经验，是学习更复杂功能的良好基础。