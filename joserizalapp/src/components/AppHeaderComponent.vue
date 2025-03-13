<template>
    <div class="header">
        <button @click="showMenu = !showMenu"><img src="../assets/list.svg"></button>
        <div v-if="showMenu" class="menu">
            <router-link to="/test">Test</router-link>
            <router-link to="/introduction">Introduction</router-link>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showMenu: false
        };
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
    width: 50px;
    height: 50px;
}

.header button img {
    width: 25px;
    height: 25px;
}

.menu {
    display: flex;
    flex-direction: column;
    background-color: white;
    position: absolute;
    top: 50px;
    left: 0;
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