<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        
        <h2>Branches</h2>

        <div class="col-md-12">
          <b-table 
            striped
            hover
            :items="branches"
            :fields="fields"
          >
            
          </b-table>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        fields: [
          { key: 'name', label:'Nombre' },
          { key: 'action', label: ''},
        ],
        branches: [],
      }
    },
    
    methods: {
      getBranches () {

        const path = 'http://localhost:8000/branches/'
        axios.get(path).then((response) => {
          this.branches = response.data
        })
        .catch((error) => {
          console.log(error)
        })

      }
    },

    created() {
      this.getBranches()
    }
  }
</script>

<style lang="css" scoped>
  
</style>