const OPTS = {
    angle:-0.1, // The span of the gauge arc
    lineWidth: 0.2, // The line thickness
    radius: 100,
    radiusScale: 1, // Relative radius
    pointer: {
      length: 0.6, // // Relative to gauge radius
      strokeWidth: 0.035, // The thickness
      color: '#000000' // Fill color
    },
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#6FADCF',   // Colors
    colorStop: '#8FC0DA',    // just experiment with them
    strokeColor: '#E0E0E0',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support
    staticLabels: {
      font: "10px sans-serif",  // Specifies font
      labels: [0, 250,  500, 750, 1000],  // Print labels at these values
      color: "#000000",  // Optional: Label text color
      fractionDigits: 0  // Optional: Numerical precision. 0=round off.
    },
    staticZones: [
      {strokeStyle: "#F03E3E", min: 0, max: 250}, // Red from 100 to 130
      {strokeStyle: "#FFDD00", min: 250, max: 400}, // Yellow
      {strokeStyle: "#30B32D", min: 400, max: 600}, // Green
      {strokeStyle: "#FFDD00", min: 600, max: 750}, // Yellow
      {strokeStyle: "#F03E3E", min: 750, max: 1000}  // Red
   ],
    
  };