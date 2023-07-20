<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/profile">Profile</router-link> |
  </nav>
  <router-view/>
</template>

<script>
import { useStore } from 'vuex'
import { onMounted } from "vue";

export default {
	setup() {
		const store = useStore()

		onMounted(() => {
			store.dispatch('onStart')
    })

    
		return {
			
		}

    },
	watch: {
		$route() {
			this.$store.dispatch('onStart')
		},

	},

}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
