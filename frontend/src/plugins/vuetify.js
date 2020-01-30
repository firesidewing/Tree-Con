import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
          light: {
            primary: '#474747',
            secondary: '#FF5722',
            accent: '#8c9eff',
            error: '#c55e5e',
            success: '#368141',
            warning: '#ffe033'
          },
        },
      },
      icons: {
        iconfont: 'mdi'
      },
});
