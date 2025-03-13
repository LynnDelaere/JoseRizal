<template>
  <div>
    <div>
      <div style="position: relative;">
        <IntoductionPageComponent />
        <div style="position: absolute; top: 0; right: 0;">
          <AppHeaderComponent />
        </div>
      </div>
      <div style="position: relative;">
        <test />
        <div style="position: absolute; top: 0; right: 0;">
          <AppHeaderComponent />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import AppHeaderComponent from './components/AppHeaderComponent.vue';
import IntoductionPageComponent from './components/IntoductionPageComponent.vue';
import test from './components/test.vue';
</script>

<style></style>