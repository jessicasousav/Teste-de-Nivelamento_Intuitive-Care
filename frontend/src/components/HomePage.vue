<template>
  <div class="homepage">
    <h1>Operadoras Ativas</h1>
    <input 
      v-model="search" placeholder="Digite o nome de uma operadora"/>
      <button @click="SearchOperadora">Buscar</button>
    
    <ul>
      <li v-for="operadora in operadoras" :key="operadora['Registro_ANS']" >
          {{ operadora[0] }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "HomePage",
  data(){
    return {
      search: '',
      operadoras: []
    };
  },
  methods: {
    SearchOperadora() {
      const path = `http://127.0.0.1:5000/buscar?q=${this.search}`
      
      axios.get(path)
      .then ((res) => {
        console.log(res.data);
        this.operadoras = res.data;
      })

      .catch ((error) => {
        console.error("Erro: Tente Novamente", error);
        alert("Erro: Verifique a conexão");
      });
    },
  }
};
</script>


<style>

.homepage{
  display: flex;
  flex-direction: column;
  height: 90vw;
  justify-content: center;
  align-items: center;
  color:  rgb(66, 66, 66);
}
input {
  height: 2em;
  width: 400px;
  border-radius: 30px;
  border: 2px solid grey;
  padding: 0px 10px;
  color: rgb(66, 66, 66);
  outline: none;
}

button {
  height: 2em;
  width: 100px;
  border-radius: 10px;
  border: none;
  background-color: rgb(184, 9, 9);
  color: white;
  font-weight: bold;
  cursor: pointer;
  margin: 10px;
}

ul {
  display: flex;
  flex-direction: row;
  flex-flow: wrap;
  padding: 20px;
}

li {
  display: flex;
  flex-direction: column;
  flex-flow: wrap;
  text-decoration: none;
  color: rgb(66, 66, 66);
  list-style: none;
  gap: 5px;
}
</style>
