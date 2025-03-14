<template>
  <div class="app-container">
    <div class="page-container">
      <div class="page-content">
        <AppHeaderComponent @changePage="scrollToComponent" />
        <div id="introduction" class="pageContent">
          <IntoductionPageComponent />
        </div>
        <div id="test" class="pageContent">
          <test />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import AppHeaderComponent from './components/AppHeaderComponent.vue';
import IntoductionPageComponent from './components/IntroductionPageComponent.vue';
import test from './components/test.vue';
</script>

<script>
export default {
  data() {
    return {
      selectedComponent: 'introduction'
    }
  },
  methods: {
    scrollToComponent(componentId) {
      this.selectedComponent = componentId;
      this.$nextTick(() => {
        const element = document.getElementById(componentId);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      });
    }
  },
  components: {
    IntoductionPageComponent,
    test,
  }
}
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