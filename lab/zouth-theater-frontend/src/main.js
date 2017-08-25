// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue"
import axios from "axios"

import App from "./App"
import router from "./router"

Vue.config.productionTip = false

axios.defaults.baseURL = "http://localhost:5000"
axios.defaults.headers.post["Content-Type"] = "application/json"

/* eslint-disable no-new */
new Vue({
    el: "#app",
    router,
    template: "<App/>",
    components: { App }
})
