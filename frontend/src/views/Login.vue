<template>
  <div class="login">
    <div class="form">
      <div class="form__wrapper">
        <div class="form__title">Auth</div>
        <input type="hidden" autocomplete="false">
        <div class="form__field">
          <label class="form__label" for="login">login</label>
          <input class="form__input" id="login" type="text" >
        </div>
        <div class="form__field">
          <label class="form__label" for="password">password</label>
          <input class="form__input" id="password" type="password">
        </div>
        <div class="form__buttons">
          <div class="button form__button">login ></div>
          <div class="button button--lined form__button">/registration</div>
        </div>
      </div>
    </div>
    <div class="art">
      <pre class="art__ascii-image">
   ____________________________________________________
  |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
  ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|
  | _____________________  ||      __   __  _  __    _ |
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|
  | _____   _   __  |/      \../      \|  __   __   ___|
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
__|  \/\|/   /(____|/ //                    /  /||~|~|~|__
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|
      /                  \|________)     /  / | |


      </pre>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {}
  }
}
</script>

<style lang="scss" scoped>
@import '../styles/vars.scss';
.login {
  display: flex;
  height: 100%;
}

.form {
  flex: 1 0 50%;
  padding: 2em;
  height: 100%;
  justify-self: stretch;
  border-right: 2px solid $subbase-color;
  box-sizing: border-box;

  &__wrapper {
    width: 80%;
    min-width: 320px;
    margin: 0 auto;
  }

  &__title {
    font-size: 2.2em;
    line-height: 1.4;
    margin-bottom: 0.5em;
    text-align: center;
  }

  &__field {
    margin-bottom: 1em;
  }

  &__label {
    display: block;
    margin-bottom: 0.5em;
  }

  &__input {
    width: 100%;
    display: block;
  }

  &__buttons {
    display: flex;
    flex-direction: row;
  }

  &__button {
    flex: 1 1 auto;
    text-align: center;

    & + & {
      margin-left: 1em;
    }
  }
}

.art {
  height: 100%;
  overflow: hidden;
  flex: 0 1 auto;
  position: relative;

  &__ascii-image {
    padding: 1em;
  }
}
</style>