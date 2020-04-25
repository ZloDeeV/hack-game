<template>
  <div id="app">
    <router-link to="/" class="title">HackGame</router-link>
    <Header />
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue';

export default {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style lang="scss">
@import './styles/global.scss';
@import './styles/vars.scss';

#app {
  display: flex;
  flex-direction: column;
  justify-content: stretch;
  position: relative;
  width: 100%;
  height: 100%;
  padding: 7px;
  border: 2px solid $subbase-color;
  box-shadow: 0 0 0 5px inset $base-color, 
    0 0 0 7px inset $subbase-color;
  box-sizing: border-box;
}

.title {
  position: absolute;
  display: inline-block;
  text-decoration: none;
  outline: none;
  color: inherit;
  font-size: 1.5em;
  line-height: 1;
  padding: 0.5em;
  top: -1em;
  left: 50%;
  transform: translateX(-50%);
  background-color: $base-color;

  // &.router-link-active {
  //   text-decoration: underline;
  // }
}

.content {
  height: 100%;
  overflow: hidden;
}
</style>
