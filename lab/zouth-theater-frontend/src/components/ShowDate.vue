<template>
    <section>
        <h3>Book Ticket on</h3>
        <ul>
            <li v-for="date in availableDates" 
                :key="date">
                <router-link :to="{ name: 'ShowTime', params: { date: date }}">
                    {{ date }}
                </router-link>
            </li>
        </ul>
    </section>
</template>

<script>
export default {
    data: function () {
        const sevenDays = []
        const currDate = new Date()

        for (let i = 0; i < 10; i++) {
            sevenDays.push(currDate.toJSON().slice(0, 10))
            currDate.setDate(currDate.getDate() + 1)
        }

        return {
            movieId: "",
            availableDates: sevenDays
        }
    },

    beforeRouteEnter: function (to, from, next) {
        const id = to.params.id
        next((vm) => { vm.movieId = id })
    },

    beforeRouteUpdate: function (to, from, next) {
        const id = to.params.id
        this.movieId = id
    }
}
</script>
