<template>
    <div class="header">
        <button @click="showMenu = !showMenu"><img src="../assets/list.svg"></button>
        <div v-if="showMenu" class="menu">
            <a href="#" @click.prevent="navigate('introduction')">Introduction</a>
            <a href="#" @click.prevent="navigate('test')">Test</a>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showMenu: false
        };
    },
    methods: {
        navigate(page) {
            this.$emit('navigate', page);
            this.showMenu = false;
        }
    }
}
</script>

<style scoped>
.header button {
    background-color: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    margin: 0;
    right: 0;
    position: absolute;
}

.header button img {
    width: 25px;
    height: 25px;
}

.menu {
    display: flex;
    flex-direction: column;
    background-color: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.menu a {
    padding: 10px;
    text-decoration: none;
    color: black;
}

.menu a:hover {
    background-color: #f0f0f0;
}
</style>