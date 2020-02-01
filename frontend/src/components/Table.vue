<template>
  <v-row>
    <v-col>
      <v-data-table 
        :headers="Headers" 
        :items="value"
        hide-default-footer
      >
        <template v-slot:item.tree="props">
          <v-edit-dialog
            :return-value.sync="props.item.tree"
            @save="save"
            @cancel="cancel"
          >
            {{ props.item.tree }}
            <template v-slot:input>
              <v-text-field
                v-model="props.item.tree"
                label="Edit"
                single-line
                counter
              ></v-text-field>
            </template>
          </v-edit-dialog>
        </template>
        <template v-slot:item.species="props">
          <v-edit-dialog
            :return-value.sync="props.item.species"
            large
            persistent
            @save="save"
            @cancel="cancel"
          >
            <div>{{ props.item.species }}</div>
            <template v-slot:input>
              <div class="mt-4 title">Update Species</div>
            </template>
            <template v-slot:input>
              <v-text-field
                v-model="props.item.species"
                label="Edit"
                single-line
                counter
                autofocus
              ></v-text-field>
            </template>
          </v-edit-dialog>
        </template>
      </v-data-table>

      <v-btn
        class="my-5"
        color="secondary"
        @click="AddTree"
      >
        Add Tree
      </v-btn>

      <v-snackbar v-model="snack" :timeout="3000" :color="snackColor">
        {{ snackText }}
        <v-btn text @click="snack = false">Close</v-btn>
      </v-snackbar>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "PlotTable",
  props: ["value"],
  data: () => ({
    snack: false,
    snackColor: "",
    snackText: "",
    Headers: [
      { text: "Tree", value: "tree" },
      { text: "Species", value: "species" },
      { text: "DBH", value: "dbh" },
      { text: "Height", value: "height" },
      { text: "Gross PS", value: "gross_piece_size" },
      { text: "Net PS", value: "net_piece_size" }
    ]
  }),
  methods: {
    save: function() {
      this.snack = true;
      this.snackColor = "success";
      this.snackText = "Data saved";
    },
    cancel: function() {
      this.snack = true;
      this.snackColor = "error";
      this.snackText = "Canceled";
    },
    AddTree: function() {
      let UnusedId = 1;
      let Used = this.value.reduce(function(o, v) {
          o[v['tree']] = true;
          return o;
      }, {});
      for (var i=1; Used[i]; i++){
        UnusedId = i <= 0 ? 1 : i + 1;
      }
      this.value.push({
        tree: UnusedId,
        species: '',
        dbh: 0,
        height: 0,
        gross_piece_size: 0,
        net_piece_size: 0
      })
    }
  }
};
</script>

<style>
</style>