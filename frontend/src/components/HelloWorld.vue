<template>
  <div>
     <v-overlay :value="loading">
      <v-progress-circular indeterminate size="68"></v-progress-circular>
    </v-overlay>
    <div style="height: 28vh; min-height:120px">
      <v-container fill-height fluid>
        <v-row align="center" justify="center">
            <v-col cols="12" class="mt-12 pt-10" sm="10" md="5">
              <v-layout justify-center>
                <v-text-field
                  outlined
                  rounded
                  dense
                  v-model="query"
                  @keydown.enter="getElements"
                  :rules="blankRule"
                  placeholder="Introduzca su búsqueda aquí"
                ></v-text-field>
                <v-btn
                  depressed
                  dark
                  large
                  @click="getElements"
                  color="success"
                  style="border-radius: 0px 25px 25px 0px; height: 42px; left: -3rem; top: -1px"
                  >
                    <v-icon class="py-5">mdi-magnify</v-icon>
                  </v-btn>
              </v-layout>
            </v-col>
        </v-row>
      </v-container>
    </div>
    <v-card
      tile
      width="96vw"
      class="mx-auto mt-12"
    >
      <div>
        <v-sheet
          style="border-radius: 50px;"
          class="v-sheet--offset mx-auto"
          color="primary darken-3"
          max-width="calc(100% - 36px)"
        >
          <div class="py-5 ml-3 text-center font-weight-bold white--text">
            Resultados
          </div>
        </v-sheet>
      </div>
      <div>
        <v-data-table
          :headers="headers"
          :page.sync="page"
          :items="elements"
          @page-count="pageCount = $event"
        >
        </v-data-table>
      </div>
    </v-card>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data() {
      return {
        query: "",
        loading: false,
        page: 1,
        pageCount: 0,
        blankRule: [(v) => v.length > 0 || "Debe ingresar un parametro para su búsqueda."],
        headers: [
          { text: "Nombre", value: "name", align: "center" },
          { text: "Tipo", value: "type_", align: "center" },
          { text: "Origen", value: "source", align: "center" },
        ],
        elements: [],
      }
    },
    methods: {
      async getElements(){
        this.elements = [];
        this.loading = true;
        await this.$http.post('api/', {query: this.query}).then(
          response => {this.elements = response.data}
        ).catch((error) => {
          alert("there was an error processing your request, please try again.");
          console.log(error);
        });
        this.loading = false;
      }
    }
  }
</script>
