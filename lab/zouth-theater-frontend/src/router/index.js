import Vue from "vue"
import Router from "vue-router"
import ShowingMovies from "@/components/ShowingMovies.vue"
import Movie from "@/components/Movie.vue"
import ShowDate from "@/components/ShowDate.vue"
import ShowTime from "@/components/ShowTime.vue"
import Seat from "@/components/Seat.vue"
import MemberTicket from "@/components/MemberTicket"

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: "/",
            name: "ShowingMovies",
            component: ShowingMovies
        },
        {
            path: "/movie/:id",
            name: "Movie",
            component: Movie,
            props: true,
            children: [
                {
                    path: "show-date",
                    name: "ShowDate",
                    component: ShowDate
                },
                {
                    path: "show-time/:date",
                    name: "ShowTime",
                    component: ShowTime
                },
                {
                    path: "book/:date/:time/:cinema",
                    name: "BookSeat",
                    component: Seat
                }
            ]
        },
        {
            path: "/member/:name/ticket",
            name: "MemberTicket",
            component: MemberTicket
        }
    ]
})
