<template>
    <article>
        <h2>Hello {{ memberName }}, Your coming tickets</h2>

        <div v-for="ticket in tickets"
             :key="idOf(ticket)"
             class="member-ticket">
             <h3>{{ ticket.movieTitle }}</h3>
             <p>{{ ticket.showDate}} {{ ticket.showTime }} @ {{ ticket.cinema }}</p>
             <p>Seat: {{ ticket.row }}{{ ticket.col }}</p>
        </div>
    </article>
</template>

<script>
import axios from "axios"

export default {
    data: function () {
        return {
            memberName: "",
            tickets: []
        }
    },

    methods: {
        idOf: function (ticket) {
            return ticket.movieId + ticket.showDate + ticket.showTime + ticket.row + ticket.col
        }
    },

    beforeRouteEnter: function (to, from, next) {
        const memberName = to.params.name

        axios.get(`/members/${memberName}/tickets`)
             .then((response) =>
                next((vm) => {
                    vm.memberName = memberName
                    vm.tickets = response.data
                })
             )
             .catch((err) => {
                 console.error(err)
                 next(false)
             })
    }
}
</script>

<style>
  
</style>
