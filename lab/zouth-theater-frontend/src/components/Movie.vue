<template>
    <article>
        <h2>{{ title }}</h2>
        <div>
            <label>Length:</label>
            <span>{{ length }} Minute </span>
        </div>
        <div>
            <label>Genre:</label>
            <span>{{ genreDisplay }}</span>
        </div>
        
        <router-link :to="{ name: 'ShowDate'}">Choose date to book</router-link>
        <router-view></router-view>
    </article>
</template>

<script>
import axios from "axios"

export default {
    props: ["id"],

    data: function () {
        return {
            title: "",
            length: 0,
            genre: []
        }
    },

    computed: {
        genreDisplay: function () {
            return this.genre.join(", ")
        }
    },

    beforeRouteEnter: function (to, from, next) {
        const id = to.params.id
        axios.get(`/showing-movies/${id}`)
             .then((response) => next(render(response.data)))
             .catch((err) => {
                 console.error(err)
                 next(false)
             })
    }
}

function render (data) {
    function _render (vm) {
        vm.title = data.title
        vm.length = data.length
        vm.genre = data.genre
    }

    return _render
}
</script>

<style>
  
</style>
