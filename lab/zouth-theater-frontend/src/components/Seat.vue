<template>
    <article>
        <h3>Choose your seat on {{ date }} {{ time }} ({{ cinema }})</h3>
        <div v-for="seat in seats"
             :key="seat.row + seat.col"
             @click="book(seat)"
             class="seat-item">
            <h4>{{ seat.row }}{{ seat.col }}</h4>
            <div>
                <label>Type: </label>
                <span>{{ seat.seatType }}</span>
            </div>
            <div>
                <label>Price: </label>
                <span>{{ seat.price }} BHT</span>
            </div>
            <div class="seat-status__booked" v-if="!seat.availability">Booked</div>
        </div>
    </article>
</template>

<script>
import axios from "axios"

export default {
    data: function () {
        return {
            movieId: "",
            date: "",
            time: "",
            cinema: "",
            seats: []
        }
    },

    methods: {
        setUpModel: function (movieId, date, time, cinema, seats) {
            this.movieId = movieId
            this.date = date
            this.time = time
            this.cinema = cinema
            this.seats = seats
        },

        book: function (seat) {
            const memberId = prompt("What's your name?")
            if (memberId === null || memberId.length === 0) {
                alert("Don't fill blank name.")
            } else {
                const data = {
                    memberId: memberId,
                    price: seat.price
                }

                axios.post(`/showing-movies/${this.movieId}/seats/` +
                            `${this.date}T${this.time}/${this.cinema}/book` +
                            `/${seat.row}/${seat.col}`, data)
                     .then((response) => alert("Your booking is success"))
                     .catch((err) => {
                         if (err.response.status === 409) {
                             alert("The seat was booked")
                         } else {
                             console.error(err)
                             alert("Something bad happened")
                         }
                     })
            }
        }
    },

    beforeRouteEnter: function (to, from, next) {
        const date = to.params.date
        const time = to.params.time
        const cinema = to.params.cinema
        const movieId = to.params.id

        axios.get(`/showing-movies/${movieId}/seats/${date}T${time}/${cinema}`)
             .then((response) => {
                 next((vm) => vm.setUpModel(movieId, date, time, cinema, response.data))
             })
             .catch((err) => {
                 console.error(err)
                 next(false)
             })
    },

    beforeRouteUpdate: function (to, from, next) {
        const date = to.params.date
        const time = to.params.time
        const cinema = to.params.cinema
        const movieId = to.params.id

        axios.get(`/showing-movies/${movieId}/seats/${date}T${time}/${cinema}`)
             .then((response) => {
                 this.setUpModel(movieId, date, time, cinema, response.data)
             })
             .catch((err) => {
                 console.error(err)
                 next(false)
             })
    }
}
</script>

<style>
    .seat-item {
        border: solid 1px #ccc;
        padding: 5px;
        margin: 3px 0px;
        cursor: pointer;
    }

    .seat-item:hover {
        background: #eee;
    }

    .seat-item h4 {
        margin: 3px 0px;
    }

    .seat-status__booked {
        color: red;
        font-style: italic;
    }
</style>
