<template>
    <div class="header">
        <button @click="showMenu = !showMenu"><img src="../assets/list.svg"></button>
        <div v-if="showMenu" class="menu">
            <a @click="navigate('introduction')">Introduction</a>
            <a @click="navigate('test')">Test</a>
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
        navigate(componentId) {
            this.$emit('changePage', componentId);
            this.showMenu = false;
        }
    }
}
</script>

<style scoped>
.header {
    position: sticky;
    background-color: white;
    position: sticky;
    top: 10px;
}

.header button {
    background-color: transparent;
    border: none;
    cursor: pointer;
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
    border-radius: 5px;
    position: absolute;
    right: 10px;
    margin: 10px;
    top: 20px;
}

.menu a {
    padding: 10px;
    text-decoration: none;
    color: black;
    cursor: pointer;
}

.menu a:hover {
    background-color: #f0f0f0;
}
</style>