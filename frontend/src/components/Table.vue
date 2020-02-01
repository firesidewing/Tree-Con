<template>
  <v-row>
    <v-col>
      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">Tree</th>
              <th class="text-left">Calories</th>
              <th class="text-left">DBH</th>
              <th class="text-left">Height</th>
              <th class="text-left">Gross PS</th>
              <th class="text-left">Net PS</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in value" :key="row.tree">
              <td>{{ row.tree }}</td>
              <td>{{ row.species }}</td>
              <td>{{ row.dbh }}</td>
              <td>{{ row.height }}</td>
              <td>{{ row.gross_piece_size }}</td>
              <td>{{ row.net_piece_size }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "PlotTable",
  props: ['value'],
  data: () => ({}),
  localStorage: {},
  methods: {
    GetPlotData: function() {

    }
  }
};
</script>

<style>
</style>