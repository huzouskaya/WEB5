<template>
    <div class="diary_container">
      <div class="diary_content">
        <h1>Личный дневник</h1>
        <ul class="diary_list">
          <li v-for="entry in entries" :key="entry.id">
            <h2>{{ entry.title }}</h2>
            <p>{{ entry.content }}</p>
            <p><em>{{ entry.date }}</em></p>
            <button @click="deleteEntry(entry)">Удалить</button>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        entries: [] // Записи дневника
      };
    },
    methods: {
      async getData() {
        try {
          const response = await this.$http.get('http://localhost:8000/api/diary/');
          this.entries = response.data; 
        } catch (error) {
          console.log(error);
        }
      },
      async deleteEntry(entry) {
        try {
          await this.$http.delete(`http://localhost:8000/api/diary/${entry.id}/`);
          this.entries = this.entries.filter(e => e.id !== entry.id);
        } catch (error) {
          console.log(error);
        }
      }
    },
    created() {
      this.getData(); // Получение записей при загрузке страницы
    }
  }
  </script>
  
  <style scoped>
  .diary_container {
    padding: 20px;
  }
  
  .diary_content {
    max-width: 600px;
    margin: auto;
  }
  
  .diary_list {
    list-style-type: none;
    padding: 0;
  }
  
  .diary_list li {
    border: 1px solid #ccc;
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
  }
  
  button {
    margin-top: 10px;
  }
  </style>