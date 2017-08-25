<template>
    <section>
        <h3>Show Time {{ date }} </h3>
        <div v-if="emptyShowTime">
            No show today.
        </div>
        <ul v-else>
            <li v-for="showTime in times" 
                :key="showTime"
                @click="book(showTime)">
                <b>{{ showTime.startTime }}</b>
                <span>at {{ showTime.cinema }}</span>
            </li>
        </ul>
        <router-link :to="{ name: 'ShowDate' }">Back</router-link>
    </section>
</template>

<script>
import axios from "axios"

export default {
    data: function () {
        return {
            date: "",
            times: []
        }
    },
    computed: {
        emptyShowTime: function () {
            return this.times.length <= 0
        }
    },

    beforeRouteEnter: function (to, from, next) {
        const movieId = to.params.id
        const date = to.params.date
        axios.get(`/showing-movies/${movieId}/show-times/${date}`)
             .then((response) => next((vm) => vm.setTimes(date, response.data)))
             .catch((err) => {
                 console.error(err)
                 next(false)
             })
    },

    methods: {
        setTimes: function (date, times) {
            this.date = date
            this.times = times
        },

        book: function (showTime) {
            this.$router.push({
                name: "BookSeat",
                params: { date: this.date, time: showTime.startTime, cinema: showTime.cinema }
            })
        }
    }
}
</script>

<style>
  
</style>
