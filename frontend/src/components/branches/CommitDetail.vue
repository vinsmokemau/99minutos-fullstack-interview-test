<template lang="html">

  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Commit Id: {{ this.commitId }}</h2>
        <div class="row">
          <div class="col">
            <div class="card">
              <div class="card-body">
                <p>Autor: {{ this.author }}</p>
                <p>Correo: {{ this.mail }}</p>
                <p>Mensaje: {{ this.message }}</p>
                <p>Timestamp: {{ this.timestamp }}</p>
                <p>Archivos modificados: {{ this.files }}</p>
              </div>
            </div>
          </div>
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
        commitId: this.$route.params.commitId,
        files: '',
        author: '',
        mail: '',
        message: '',
        timestamp: '',
      }
    },

    methods: {
      getCommit () {

        const path = `http://localhost:8000/commits/${this.commitId}/`
        axios.get(path).then((response) => {
          this.files = response.data.files
          this.author = response.data.author
          this.mail = response.data.mail
          this.message = response.data.message
          this.timestamp = response.data.timestamp
        })
        .catch((error) => {
          console.log(error)
        })

      }
    },

    created () {
      this.getCommit()
    },
  }

</script>