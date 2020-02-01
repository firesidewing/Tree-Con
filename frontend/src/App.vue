<template>
  <v-app id="inspire">

    <Login v-on:auth-success="LoggedOn = true" v-show="ShowOnline && !LoggedOn"></Login>

    <v-navigation-drawer v-model="drawer" app clipped dark color="primary">
      <v-list v-if="SelectedLocation">
        <v-list-item 
          link 
          v-for="Plot in PlotList" 
          v-bind:key="Plot.PlotNumber">
          <v-list-item-action>
            <v-icon>mdi-pine-tree</v-icon>
          </v-list-item-action>
          <v-list-item-content @click="SelectedPlotData = Plot.PlotData; drawer = false">
            <v-list-item-title>Plot {{Plot.plot_number}}</v-list-item-title>
          </v-list-item-content>
          <v-btn 
            @click.stop="DeletePlot(Plot.plot_number)"
            text 
            icon 
            color="accent">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </v-list-item>
        
      </v-list>
      <template v-slot:append>
        <div class="pa-2" v-if="SelectedLocation">
          <v-btn 
            block
            @click.stop="AddPlot"
            color="secondary"
          >Add Plot</v-btn>
        </div>
      </template>
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
        item-value="id"
        @change="LocationChange"
        class="mt-3"
        clearable
        dense
      ></v-autocomplete>
    </v-app-bar>

    <v-overlay :value="Loading">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>

    <v-content>
      <v-container fluid>
        <v-row>
          <v-col>
            <v-fade-transition>
              <Table 
                v-if="SelectedPlotData != ''" 
                v-model="SelectedPlotData"
              ></Table>
            </v-fade-transition>            
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
import axios from "axios";
import Login from "./components/Login";
import Table from "./components/Table"

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
    Login,
    Table
  },
  data: () => ({
    drawer: false,
    Loading: false,
    Internet: navigator.onLine,
    ShowOnline: true,
    LoggedOn: false,
    Locations: [],
    SelectedLocation: "",
    SelectedPlotData: '',
    Plots: [
      {
        PlotNumber: 1
      }
    ],
    Config: {
      headers: {
        Authorization: ``
      }
    }
  }),
  created() {},
  mounted() {
    window.addEventListener("online", this.UpdateOnlineStatus);
    window.addEventListener("offline", this.UpdateOnlineStatus);
    if (localStorage.TokenConfig != "undefined") {
      this.Config = this.$localStorage.get("TokenConfig");
      this.LoggedOn = true;
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
    LoggedOn() {
      if (this.LoggedOn) {
        this.Config = this.$localStorage.get("TokenConfig");
        this.GetLocations();
      }
    },
  },
  computed: {
    PlotList: function() {
      return this.Plots.slice(0).sort(function(a, b){return a.plot_number - b.plot_number})
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
          v.RetryLogin();
        });
    },
    GetPlotData: function() {
      let v = this;
      if (v.Plots.length > 0) {
        v.Plots.forEach(Plot => {
          axios
            .get(Api.Base + Api.PlotData + "?plot_key=" + Plot.id + "&ordering=id", v.Config)
            .then(function(response) {
              Plot["PlotData"] = response.data.results;
              v.Loading = false
            })
            .catch(function(error) {
              alert(error);
              v.RetryLogin();
            });
        });
        
      }
    },
    RetryLogin: function() {
      let v = this;
      v.LoggedOn = false;
      v.Loading = false;
    },
    LocationChange: function() {
      let v = this;
      v.Loading = true
      axios
        .get(Api.Base + Api.Plots + "?location=" + v.SelectedLocation + "&ordering=id", v.Config)
        .then(function(response) {
          v.Plots = response.data.results;          
          v.GetPlotData()
        })
        .catch(function(error) {
          alert(error);
          v.RetryLogin();
        });
    },
    AddPlot: function() {
      let UnusedId = 1;
      let Used = this.Plots.reduce(function(o, v) {
          o[v['plot_number']] = true;
          return o;
      }, {});
      for (var i=1; Used[i]; i++){
        UnusedId = i <= 0 ? 1 : i + 1;
      }
      this.Plots.push({
        location: this.SelectedLocation,
        plot_number: UnusedId,
        PlotData: []
      })
    },
    DeletePlot: function(PlotNumber) {
      let v = this
      v.Plots = v.Plots.filter(function( obj ) {
        return obj.plot_number !== PlotNumber;
      });
    },
  }
};
</script>

<style lang="sass">
  @import '../node_modules/roboto-fontface/css/roboto/roboto-fontface.css'
</style>
