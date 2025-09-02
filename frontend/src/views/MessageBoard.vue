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
              <div class="message-actions">
                <el-button
                type="danger"
                size="mini"
                @click="deleteMessage(message.id)"
                :loadinig="deletingIds.includes(message.id)"
                >删除</el-button>
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
      deletingIds: [], // 记录正在删除的留言ID
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
    },

    // 删除留言
    async deleteMessage(messageId) {
      // 确认删除
      try {
        await this.$confirm('确定要删除这条留言吗？', '确认删除', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
      } catch {
        // 用户取消删除
        return
      }
      
      // 添加到删除中的ID列表（显示loading状态）
      this.deletingIds.push(messageId)
      
      try {
        await this.$http.delete(`/messages/${messageId}/`)
        this.$message.success('留言删除成功！')
        
        // 重新加载留言列表
        this.loadMessages()
      } catch (error) {
        console.error('删除留言失败:', error)
        this.$message.error('删除留言失败，请重试')
      } finally {
        // 从删除中的ID列表移除
        const index = this.deletingIds.indexOf(messageId)
        if (index > -1) {
          this.deletingIds.splice(index, 1)
        }
      }
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
  align-items: center;
  color: #666;
  font-size: 14px;
}

.message-info {
  display: flex;
  flex-direction: column;
}
.message-actions {
  flex-shrink: 0; /* 防止按钮被压缩 */
} 

.author {
  font-weight: bold;
}

.time {
  font-style: italic;
}
</style>