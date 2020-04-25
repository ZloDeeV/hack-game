<template>
  <div class="header">
    <div class="header__nav">
      <router-link to="scanner" class="header__nav-item">>_scanner</router-link>
      <router-link to="shop" class="header__nav-item">$_shop</router-link>
      <router-link to="rating" class="header__nav-item">^_rating</router-link>
      <router-link to="about" class="header__nav-item">@_about</router-link>
      <div class="header__nav-item">logout_></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {}
  }
}
</script>

<style lang="scss" scoped>
@import '../styles/vars.scss';
.header {
  display: flex;
  width: 100%;
  padding: 1em;
  border-bottom: 2px solid $subbase-color;
  box-sizing: border-box;

  &__nav {
    display: flex;
    width: 100%;
    font-size: 1.2em;
  }

  &__nav-item {
    cursor: pointer;
    padding: .5em 1em;
    border: 1px solid transparent;
    text-decoration: none;
    color: inherit;
    box-sizing: border-box;
    & + & {
      margin-left: 0.5em;
    }

    &:hover, &.router-link-active {
      text-shadow: $text-shadow-invert;
      border-color: $subbase-color;
      // &::after {
      //   content: '░'
      // }
    }

    &:last-child {
      margin-left: auto;
    }
  }
}
</style>