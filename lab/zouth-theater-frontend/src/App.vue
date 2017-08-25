<template>
    <div id="app">
        <h1>Zouth Theater</h1>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: "app"
}
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    padding: 0px 20px;
}

h1 {
    text-align: center;
    margin: 10px 0;
}
</style>
