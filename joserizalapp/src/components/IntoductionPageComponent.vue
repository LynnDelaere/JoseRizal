<template>
    <div>
        <AppHeaderComponent title="José Rizal" @navigate="$emit('navigate')" />
        <div class="pageContent" v-for="title in titles" :key="title.id">
            <h3>{{ title.title }}</h3>
            <p>{{text.find(t => t.id === title.id).text}}</p>
        </div>
    </div>
</template>

<script setup>
import AppHeaderComponent from './AppHeaderComponent.vue';
</script>

<script>
export default {
    name: 'IntroductionPageComponent',
    data() {
        return {
            titles: [
                { id: 1, title: '' },
                { id: 2, title: 'Education' },
                { id: 3, title: 'Personal life, relationships and ventures' }
            ],
            text: [
                { id: 1, text: 'José Rizal (1861–1896) was a Filipino nationalist, writer, and polymath who played a key role in the Filipino Propaganda Movement against Spanish colonial rule. An ophthalmologist by profession, he authored Noli Me Tángere and El filibusterismo, which inspired the Philippine Revolution. Though not directly involved in the revolution, his writings fueled the movement for independence. Executed by the Spanish in 1896 for rebellion, he remains a revered national hero. His ancestry was a mix of Chinese, Spanish, and Tagalog, and he was known for his intelligence and literary prowess from a young age.' },
                { id: 2, text: 'José Rizal pursued his education at the Ateneo Municipal de Manila, excelling in multiple fields. Initially studying law at the University of Santo Tomas, he switched to medicine upon learning of his mother’s blindness, specializing in ophthalmology. He continued his studies in Madrid, Paris, and Heidelberg, where he trained under renowned doctors and became a polyglot fluent in 22 languages. A polymath, Rizal was also a writer, painter, sculptor, historian, and Freemason. His novels, Noli Me Tángere and El filibusterismo, became catalysts for Philippine nationalism, blending literature with his advocacy for reform.' },
                { id: 3, text: 'José Rizal\'s life is one of the most well- documented among 19th - century Filipinos due to his extensive writings and letters.A prolific diarist, Rizal recorded his travels, relationships, and experiences, often switching between languages in his writings. His first love was Segunda Katigbak, though she was engaged to another.His longest and most significant relationship was with Leonor Rivera, who inspired the character of María Clara in Noli Me Tángere.Their love endured years of secret correspondence, but her family opposed the match, and she eventually married an Englishman, devastating Rizal. During his travels in Europe and Asia, Rizal was linked to several women, including Gertrude Beckett in London, Nelly Boustead of an English- Iberian family, and Seiko Usui in Japan.In Hong Kong, he practiced ophthalmology and lived with his family. In 1895, Rizal met Josephine Bracken, an Irishwoman who brought her adoptive father to Rizal for eye treatment.They fell in love, but the Catholic Church refused to marry them due to Rizal’s political reputation.Instead, they lived in a common - law marriage in Dapitan and had a son who died shortly after birth. Rizal’s personal life, much like his political endeavors, was marked by passion, hardship, and unwavering dedication to his beliefs.' }],
        }
    }
}
</script>