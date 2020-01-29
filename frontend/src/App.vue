<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      dark
      color=primary
    >
      <v-list dense>
        <v-list-item link v-for="Plot in Plots" v-bind:key="Plot.PlotNumber">
          <v-list-item-action>
            <v-icon>mdi-pine-tree</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Plot {{Plot.PlotNumber}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>        
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
      color=primary
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Recce</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-autocomplete
        v-model="SelectedLocation"
        :items="Locations"
        label="Location"
        item-text="name"
        item-value="name"
        class="mt-3"
        clearable=true
        dense
      ></v-autocomplete>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col class="shrink">
            
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer app>
      <span>Josh Dollinger &copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: () => ({
    drawer: false,
    LocationTimer: null,
    Locations: [],
    SetLocation: '',
    Plots: [{
      PlotNumber: 1
    }],
    Config: {
      headers: { Authorization: `` }
    },
    Params: {
      username: "Josh",
      password: "F1res1dew1ng",
      email:""
    }
  }),
  created: function(){
    this.GetToken();
  },
  methods: {
    GetLocations: function() {
      let v = this;
      axios.get("http://127.0.0.1:8000/api/v1/core/locations/", v.Config)
      .then(function (response) {
        v.Locations = response.data.results;
      })
      .catch(function(error) {
        alert(error)
        clearInterval(v.LocationTimer);
        v.LocationTimer = null;
      })
    },
    GetToken: function(){
      let v = this;
      axios.post("http://127.0.0.1:8000/api/v1/auth/login/", 
      v.Params,
      v.Config)
      .then(function (response) {
        v.Config.headers.Authorization = "Token " + response.data.key;
        v.GetLocations();
      })
      .catch(function(error) {
        alert(error)
      })
    }
  }
};
</script>
