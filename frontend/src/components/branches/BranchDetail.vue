<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        
        <h2>Rama: {{ branchName }}</h2>

        <div class="col-md-12">
          <b-table 
            striped
            hover
            :items="commits"
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
        branchName: this.$route.params.branchName,
        fields: [
          { key: 'id', label:'Id' },
          { key: 'author', label:'Autor' },
          { key: 'message', label:'Mensaje' },
          { key: 'timestamp', label:'Timestamp' },
          { key: 'action', label: ''},
        ],
        commits: [],
      }
    },

    methods: {
      getCommits () {

        const path = `http://localhost:8000/branches/${this.branchName}/`
        axios.get(path).then((response) => {
          this.commits = response.data
        })
        .catch((error) => {
          console.log(error)
        })

      }
    },

    created () {
      this.getCommits()
    }
  }

</script>

<style lang="css" scoped>
  
</style>
