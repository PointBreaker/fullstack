# 简单留言板项目
> Vue.js + Element UI + Django REST Framework (DRF)

> HomePage

![主页](https://github.com/PointBreaker/fullstack/blob/main/asset/homepage.png?raw=true)

> 主界面


![App](https://github.com/PointBreaker/fullstack/blob/main/asset/app.png?raw=true)

## 📋 项目简介

这是一个从零开始构建的全栈留言板应用，采用前后端分离架构。通过这个项目可以学习现代Web开发的完整流程，包括前端Vue.js开发、后端API设计、数据库操作等核心技术。

建议按照DOCS.md文档逐步实现，如果遇到问题可以参考项目代码。

## 🏗️ 技术栈

### 后端技术
- **Django 4.x** - Python Web框架
- **Django REST Framework** - RESTful API开发
- **SQLite** - 轻量级数据库
- **django-cors-headers** - 跨域请求处理

### 前端技术
- **Vue.js 2.x** - 渐进式JavaScript框架
- **Element UI** - Vue.js组件库
- **Axios** - HTTP客户端
- **Vue Router** - 路由管理

## 🚀 项目结构

```
fullstack_project/
├── backend/                 # Django后端
│   ├── config/             # 项目配置
│   ├── messages/           # 留言应用
│   └── manage.py           # Django管理脚本
├── frontend/               # Vue.js前端
│   ├── src/
│   │   ├── components/     # Vue组件
│   │   ├── views/          # 页面视图
│   │   └── main.js         # 入口文件
│   └── package.json        # 前端依赖
├── DOCS.md                 # 详细开发文档
└── README.md               # 项目说明
```

## ✅ 已完成功能

### 1. 后端API开发 (100% 完成)
- [x] **Django项目初始化**
  - 项目配置和应用创建
  - 数据库配置和迁移
  - CORS跨域配置

- [x] **留言数据模型**
  - Message模型设计（标题、内容、作者、时间）
  - 数据库迁移文件生成和执行

- [x] **RESTful API接口**
  - `GET /api/messages/` - 获取留言列表
  - `POST /api/messages/` - 创建新留言
  - `PUT /api/messages/{id}/` - 编辑留言
  - `DELETE /api/messages/{id}/` - 删除留言

- [x] **API视图实现**
  - ListCreateAPIView - 列表和创建
  - RetrieveUpdateDestroyAPIView - 详情、更新、删除
  - 数据序列化和验证

### 2. 前端界面开发 (100% 完成)
- [x] **Vue.js项目搭建**
  - 项目初始化和依赖安装
  - Element UI集成和配置
  - Axios HTTP客户端配置

- [x] **留言板主界面**
  - 响应式布局设计
  - 留言列表展示
  - 留言卡片样式

- [x] **留言管理功能**
  - 添加留言表单（标题、内容、作者）
  - 编辑留言功能（弹窗表单）
  - 删除留言功能（确认对话框）
  - 表单验证和错误处理

- [x] **用户交互优化**
  - 加载状态提示
  - 成功/错误消息提示
  - 操作确认对话框

### 3. 前后端集成 (100% 完成)
- [x] **API接口对接**
  - 前端Axios配置
  - 后端CORS配置
  - 请求响应数据格式统一

- [x] **错误处理机制**
  - 网络错误处理
  - 服务器错误处理
  - 用户友好的错误提示

## 🔄 项目运行

### 后端启动
```bash
cd backend
python manage.py runserver
# 访问: http://127.0.0.1:8000/api/messages/
```

### 前端启动
```bash
cd frontend
npm run serve
# 访问: http://localhost:8080
```

## 📝 TODO 列表

### 🔐 用户认证系统 (优先级: 高)

#### 1. 后端用户认证 (预计工作量: 5-7天)
- [ ] **用户模型设计**
  - [ ] 扩展Django User模型或创建自定义用户模型
  - [ ] 用户信息字段设计（用户名、邮箱、头像等）
  - [ ] 数据库迁移

- [ ] **JWT认证实现**
  - [ ] 安装和配置django-rest-framework-simplejwt
  - [ ] JWT token生成和验证
  - [ ] Token刷新机制

- [ ] **认证API接口**
  - [ ] `POST /api/auth/register/` - 用户注册
  - [ ] `POST /api/auth/login/` - 用户登录
  - [ ] `POST /api/auth/logout/` - 用户登出
  - [ ] `GET /api/auth/profile/` - 获取用户信息
  - [ ] `PUT /api/auth/profile/` - 更新用户信息

- [ ] **权限控制系统**
  - [ ] API权限装饰器
  - [ ] 留言与用户关联
  - [ ] 只能编辑/删除自己的留言

#### 2. 前端用户系统 (预计工作量: 7-10天)
- [ ] **用户状态管理**
  - [ ] 用户登录状态管理
  - [ ] Token存储和管理
  - [ ] 页面刷新状态保持

- [ ] **用户界面开发**
  - [ ] 登录页面设计和实现
  - [ ] 注册页面设计和实现
  - [ ] 用户个人中心页面
  - [ ] 导航栏用户信息显示

- [ ] **路由权限控制**
  - [ ] 路由守卫实现
  - [ ] 未登录用户重定向
  - [ ] 权限页面访问控制

- [ ] **HTTP请求拦截**
  - [ ] Axios请求拦截器添加Token
  - [ ] 响应拦截器处理Token过期
  - [ ] 自动刷新Token机制

#### 3. 功能集成和优化 (预计工作量: 3-5天)
- [ ] **留言系统改造**
  - [ ] 留言显示作者信息
  - [ ] 编辑/删除按钮权限控制
  - [ ] 留言创建时自动关联当前用户

- [ ] **用户体验优化**
  - [ ] 登录状态的友好提示
  - [ ] 表单验证优化
  - [ ] 加载状态和错误处理
  - [ ] 响应式设计适配

### 🚀 功能增强 (优先级: 中)

#### 1. 留言系统增强 (预计工作量: 3-5天)
- [ ] **留言分类功能**
  - [ ] 分类模型设计
  - [ ] 分类管理界面
  - [ ] 按分类筛选留言

- [ ] **留言搜索功能**
  - [ ] 后端搜索API
  - [ ] 前端搜索界面
  - [ ] 关键词高亮显示

- [ ] **留言排序和分页**
  - [ ] 多种排序方式（时间、热度等）
  - [ ] 分页加载优化
  - [ ] 无限滚动加载

#### 2. 用户交互增强 (预计工作量: 2-3天)
- [ ] **留言点赞功能**
  - [ ] 点赞数据模型
  - [ ] 点赞API接口
  - [ ] 前端点赞交互

- [ ] **留言评论功能**
  - [ ] 评论数据模型
  - [ ] 评论API接口
  - [ ] 评论界面实现

### 🔧 技术优化 (优先级: 低)

#### 1. 性能优化 (预计工作量: 2-3天)
- [ ] **前端性能优化**
  - [ ] 组件懒加载
  - [ ] 图片懒加载
  - [ ] 打包优化

- [ ] **后端性能优化**
  - [ ] 数据库查询优化
  - [ ] API缓存机制
  - [ ] 静态文件处理

#### 2. 部署和运维 (预计工作量: 3-5天)
- [ ] **容器化部署**
  - [ ] Docker配置
  - [ ] docker-compose编排
  - [ ] 环境变量管理

- [ ] **生产环境配置**
  - [ ] 生产数据库配置
  - [ ] 静态文件服务
  - [ ] 日志管理

## 🎯 学习目标

通过完成这个项目，你将掌握：

1. **前后端分离架构**的设计和实现
2. **RESTful API**的设计原则和最佳实践
3. **Vue.js**组件化开发和状态管理
4. **Django REST Framework**的使用
5. **用户认证和权限控制**系统
6. **前后端数据交互**和错误处理
7. **现代Web开发**的完整流程

## 📚 相关文档

- [DOCS.md](./DOCS.md) - 详细开发文档和教程
- [Django REST Framework 官方文档](https://www.django-rest-framework.org/)
- [Vue.js 官方文档](https://vuejs.org/)
- [Element UI 官方文档](https://element.eleme.io/)

## 🤝 贡献指南

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情
```

这个更新后的README.md包含了：

1. **完整的项目介绍**和技术栈说明
2. **详细的已完成功能**列表，展示当前进度
3. **结构化的TODO列表**，按优先级和工作量进行分类
4. **具体的工作拆解**，每个任务都有明确的子项目
5. **时间估算**，帮助规划开发进度
6. **学习目标**，明确项目的教育价值

重点突出了用户认证系统作为下一个主要开发目标，并将其分解为后端认证、前端用户系统和功能集成三个阶段，每个阶段都有详细的任务清单。