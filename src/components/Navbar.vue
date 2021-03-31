<template>
  <header class="site-header">
    <div class="container">
      <a href="index.html" id="branding">
        <img src="@/assets/images/logo.png" alt="" class="logo" />
        <div class="logo-copy">
          <h1 class="site-title">DJ-V-Movies</h1>
          <small class="site-description">Django Vue Movies Website</small>
        </div>
      </a>
      <!-- #branding -->

      <div class="main-navigation">
        <button type="button" class="menu-toggle">
          <i class="fa fa-bars"></i>
        </button>
        <ul class="menu">
          <li
            class="menu-item"
            :class="{ 'current-menu-item': Home === 'True' }"
          >
            <router-link to="/">Home</router-link>
          </li>
          <li
            class="menu-item"
            :class="{ 'current-menu-item': About === 'True' }"
          >
            <router-link to="/about">About</router-link>
          </li>
          <li
            class="menu-item"
            :class="{ 'current-menu-item': Reviews === 'True' }"
          >
            <router-link to="/review">Movie reviews</router-link>
          </li>
          <li
            class="menu-item"
            :class="{ 'current-menu-item': Contact === 'True' }"
          >
            <router-link to="/contact">Contact</router-link>
          </li>
        </ul>
        <!-- .menu -->

        <form class="search-form">
          <input type="text" placeholder="Search..." />
          <button><i class="fa fa-search"></i></button>
        </form>
      </div>
      <!-- .main-navigation -->

      <div class="mobile-navigation">
        <ul class="menu">
          <li
            class="menu-item"
            :class="{ 'current-menu-item': Home === 'True' }"
          >
            <router-link to="/">Home</router-link>
          </li>
          <li
            class="menu-item"
            :class="{ 'current-menu-item': About === 'True' }"
          >
            <router-link to="/about">About</router-link>
          </li>
          <li
            class="menu-item"
            :class="{ 'current-menu-item': Reviews === 'True' }"
          >
            <router-link to="/review">Movie reviews</router-link>
          </li>
          <li
            class="menu-item"
            :class="{ 'current-menu-item': Contact === 'True' }"
          >
            <router-link to="/contact">Contact</router-link>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {};
  },
  props: {
    Home: String,
    About: String,
    Reviews: String,
    Contact: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
