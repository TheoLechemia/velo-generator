const App = {
    data() {
      return {
        counter: 0, 
        gauge: null,
        currentBalance: 0,
        powerProduction: null,
        powerDemand: null,
      }
    },
    methods : {
        initGauge() {
            const target = document.getElementById('gauge'); // your canvas element
            this.gauge = new Gauge(target).setOptions(OPTS); // create sexy gauge!
            this.gauge.maxValue = 1000; // set max gauge value
            this.gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
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
        socket.on("production", (data) => {
          console.log('JY AI Recu ,,')
          console.log(data);
          this.powerProduction = data.list;  
          this.gauge.set(this.powerProduction)
        });
        socket.on("demand", (data) => {
          console.log('JY AI Recu ,,')
          console.log(data);
          this.powerDemand = data.list;  
          this.gauge.set(this.powerProduction)
        });
    },
    delimiters: ['${','}']
  }
  
  Vue.createApp(App).mount('#app')






