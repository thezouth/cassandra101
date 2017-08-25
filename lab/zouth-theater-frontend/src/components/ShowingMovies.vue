<template>
    <section>
        <h2>Showing Movies</h2>
        <article v-for="movie in showingMovies" 
                 :key="movie.id" 
                 @click="routeTo(movie.id)"
                 class="movie-list">

            <h3 class="movie-list_title">{{ movie.title }}</h3>

        </article>
    </section>
</template>

<script>
import axios from "axios"

export default {
    data: function () {
        return {
            showingMovies: []
        }
    },

    beforeRouteEnter: function (to, from, next) {
        axios.get("showing-movies")
             .then((response) => {
                 next((vm) => { vm.showingMovies = response.data })
             })
             .catch((err) => {
                 console.error(err)
                 next((vm) => { vm.showingMovies = [] })
             })
    },

    methods: {
        routeTo: function (movieId) {
            this.$router.push({
                name: "Movie",
                params: { id: movieId }
            })
        }
    }
}
</script>

<style>
  .movie-list_title {
      color: teal;
  }
  .movie-list {
      cursor: pointer;
  }
</style>
