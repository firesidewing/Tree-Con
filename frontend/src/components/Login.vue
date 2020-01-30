<template>
  <v-app id="inspire" v-if="overlay">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-overlay v-bind:value="overlay">
              <v-card class="elevation-12">
                <v-toolbar color="secondary" dark flat>
                  <v-toolbar-title>Login</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <v-form>
                    <v-text-field
                      v-model="Params.username"
                      label="Login"
                      name="login"
                      prepend-icon="person"
                      type="text"
                    />
                    <v-text-field
                      v-model="Params.password"
                      label="Password"
                      name="password"
                      prepend-icon="lock"
                      type="password"
                    />
                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn color="secondary" @click.stop="GetToken">Login</v-btn>
                </v-card-actions>
              </v-card>
            </v-overlay>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from "axios";

const LoginUrl = "https://tree-con.herokuapp.com/api/v1/auth/login/";

export default {
  props: {
    source: String,
    overlay: Boolean
  },
  data: () => ({
    Config: {
      headers: {
        Authorization: ``
      }
    },
    Params: {
      username: "",
      password: "",
      email: ""
    }
  }),
  localStorage: {
    TokenConfig: {
      type: Object      
    },
    UserParams: {
      type: Object      
    }
  },
  methods: {
    GetToken: function() {
      let v = this;
      axios
        .post(LoginUrl, v.Params, v.Config)
        .then(function(response) {
          v.Config.headers.Authorization = "Token " + response.data.key;
          v.$localStorage.set("TokenConfig", v.Config);
          v.$localStorage.set("UserParams", v.Params);
          v.overlay = false;
        })
        .catch(function(error) {
          alert(error);
        });
    }
  }
};
</script>