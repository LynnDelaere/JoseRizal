<template>
    <div class="appHeader">
        <h1>{{ title }}</h1>
        <button id="menu" @click="toggleMenu"><img src="../assets/list.svg" /></button>
        
        <!-- Menu bar that shows/hides based on isMenuOpen -->
        <div class="menu-bar" v-if="isMenuOpen">
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
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
    },
    data() {
        return {
            isMenuOpen: false
        }
    },
    methods: {
        toggleMenu() {
            this.isMenuOpen = !this.isMenuOpen;
            console.log('Menu clicked, isMenuOpen:', this.isMenuOpen);
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
    position: relative;
}

.appHeader button {
    background: none;
    border: none;
    cursor: pointer;
}

.menu-bar {
    position: absolute;
    top: 100%;
    right: 0;
    background-color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 4px;
    width: 200px;
    z-index: 10;
}

.menu-bar ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.menu-bar li {
    padding: 0;
}

.menu-bar a {
    display: block;
    padding: 10px 15px;
    text-decoration: none;
    color: #333;
    transition: background-color 0.3s;
}

.menu-bar a:hover {
    background-color: #f5f5f5;
}
</style>