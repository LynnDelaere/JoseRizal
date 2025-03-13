<template>
  <div class="app-container">
    <div class="page-container">
      <div class="page-content">
        <AppHeaderComponent class="header-position" @navigate="navigateTo" />
        <IntoductionPageComponent ref="introduction" />
        <test ref="test" />
      </div>
    </div>
  </div>
</template>

<script setup>
import AppHeaderComponent from './components/AppHeaderComponent.vue';
import IntoductionPageComponent from './components/IntoductionPageComponent.vue';
import test from './components/test.vue';
</script>

<style>
.page-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.page-content {
  position: relative;
}

.header-position {
  position: absolute;
  top: 0;
  right: 0;
}
</style>