<template>
    <div class="appHeader">
        <h1>{{ title }}</h1>
        <button><img src="../assets/list.svg" /></button>
    </div>
</template>

<script>
export default {
    name: 'AppHeaderComponent',
    props: {
        title: {
            type: String,
            required: true,
            default: 'Default Title'
        }
    }
}
</script>

<style scoped>
.appHeader {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem;
}

.appHeader button {
    background: none;
    border: none;
    cursor: pointer;
}
</style>