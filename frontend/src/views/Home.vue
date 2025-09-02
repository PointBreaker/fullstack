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