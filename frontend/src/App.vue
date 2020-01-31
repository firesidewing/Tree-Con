<template>
  <v-app id="inspire">
    <Login v-on:auth-success="LoggedOn = true" v-show="ShowOnline && !LoggedOn"></Login>
    <v-navigation-drawer v-model="drawer" app clipped dark color="primary">
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

    <v-app-bar app clipped-left color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Tree - Con</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-autocomplete
        v-model="SelectedLocation"
        :items="Locations"
        label="Location"
        item-text="name"
        item-value="name"
        @change="LocationChange"
        class="mt-3"
        clearable
        dense
      ></v-autocomplete>
    </v-app-bar>

    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col class="shrink"></v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer app>
      <span>Josh Dollinger &copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import axios from 'axios';
import Login from './components/Login'

const Api = {
  Base: "https://tree-con.herokuapp.com/api/v1/",
  LatLong: "core/lat-longs",
  Locations: "core/locations",
  PlotData: "core/plot-datas",
  Plots: "core/plot"
};

export default {
  name: "TreeCon",
  components: {
    Login
  },
  data: () => ({
    drawer: false,
    Internet: navigator.onLine,
    ShowOnline: true,
    LoggedOn: false,
    LocationTimer: null,
    Locations: [],
    SelectedLocation: "",
    Plots: [
      {
        PlotNumber: 1
      }
    ],
    Config: {
      headers: {
        Authorization: ``
      }
    },
  }),
  created() {
  },
  mounted() {
    window.addEventListener("online", this.UpdateOnlineStatus);
    window.addEventListener("offline", this.UpdateOnlineStatus);
    if(localStorage.TokenConfig != "undefined"){
      this.Config = this.$localStorage.get('TokenConfig')
      this.LoggedOn = true
    }
  },
  watch: {
    Internet(v) {
      if (v) {
        this.ShowOnline = true;
        setTimeout(() => {
          this.ShowOnline = false;
        }, 1000);
      }
    },
    LoggedOn(){
      if(this.LoggedOn){
        this.Config = this.$localStorage.get('TokenConfig')
        this.GetLocations();
      }
    }
  },
  methods: {
    updateOnlineStatus: function(e) {
      const { type } = e;
      this.Internet = type === "online";
    },
    GetLocations: function() {
      let v = this;
      axios
        .get(Api.Base + Api.Locations, v.Config)
        .then(function(response) {
          v.Locations = response.data.results;
        })
        .catch(function(error) {
          alert(error);
          clearInterval(v.LocationTimer);
          v.LocationTimer = null;
          v.RetryLogin()
        });
    },
    RetryLogin: function() {
      let v = this
      v.LoggedOn = false
    },
    LocationChange: function() {
      let v = this;
      axios
        .get(Api.Base + Api.Locations, v.Config)
        .then(function(response) {
          v.Locations = response.data.results;
        })
        .catch(function(error) {
          alert(error);
          clearInterval(v.LocationTimer);
          v.LocationTimer = null;
          v.RetryLogin()
        });
    }
  }
};
</script>

<style lang="sass">
  @import '../node_modules/roboto-fontface/css/roboto/roboto-fontface.css'
</style>
