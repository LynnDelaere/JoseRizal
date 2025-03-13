<template>
    <div>
        <AppHeaderComponent 
            title="Test" 
            @navigate="handleNavigation" 
        />
        
        <!-- Different sections controlled by currentSection -->
        <div v-if="currentSection === 'home'" class="section">
            <h2>Home Section</h2>
            <p>Welcome to the home section of the application.</p>
        </div>
        
        <div v-if="currentSection === 'about'" class="section">
            <h2>About Section</h2>
            <p>Learn more about our company and mission.</p>
        </div>
        
        <div v-if="currentSection === 'services'" class="section">
            <h2>Services Section</h2>
            <p>Explore the services we offer.</p>
        </div>
        
        <div v-if="currentSection === 'contact'" class="section">
            <h2>Contact Section</h2>
            <p>Get in touch with us.</p>
        </div>
    </div>
</template>

<script>
import AppHeaderComponent from './AppHeaderComponent.vue';

export default {
    name: 'Test',
    components: {
        AppHeaderComponent
    },
    data() {
        return {
            currentSection: 'home' // Default section
        }
    },
    methods: {
        handleNavigation(section) {
            this.currentSection = section;
            console.log('Test component received navigation to:', section);
        }
    }
}
</script>

<style>
.section {
    padding: 20px;
    margin: 20px;
    border-radius: 8px;
    background-color: #f9f9f9;
}
</style>