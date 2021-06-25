const App = {
  data() {
    return {
      counter: 0,
      gauge: null,
      currentBalance: 0,
      powerProductionTotal: null,
      productionByBike: new Array(10),
      powerDemand: null,
    }
  },
  methods: {
    initGauge() {
      const target = document.getElementById('gauge'); // your canvas element
      this.gauge = new Gauge(target).setOptions(OPTS); // create sexy gauge!
      this.gauge.maxValue = 100; // set max gauge value
      this.gauge.setMinValue(-100);  // Prefer setter over gauge.minValue = 0
      this.gauge.animationSpeed = 32; // set animation speed (32 is default value)
      this.gauge.set(this.currentBalance); // set actual value
    },
  },
  mounted() {
    this.initGauge();
    socket = io();
    socket.on('connect', () => {
      console.log("connected");
    });
    socket.on("data", (data) => {
      data = JSON.parse(data)
      this.productionByBike = data.production;
      this.powerProductionTotal = data.production.reduce(function (a, b) {
        return a + b + 0;
      })
      this.powerDemand = data.demand.power;
      this.currentBalance = this.powerProductionTotal - this.powerDemand;
      // HACK pour pas que les valeur dépassent -100 et 100
      if (this.currentBalance > 100) {
        this.currentBalance = 100
      };
      if (this.currentBalance < -100) {
        this.currentBalance = -100;
      };
      this.gauge.set(this.currentBalance);
    });

  },
  delimiters: ['${', '}']
}

Vue.createApp(App).mount('#app')






