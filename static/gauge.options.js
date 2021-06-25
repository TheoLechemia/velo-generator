const OPTS = {
  angle: -0.1, // The span of the gauge arc
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
    labels: [-100, -50, 0, 50, 100],  // Print labels at these values
    color: "#000000",  // Optional: Label text color
    fractionDigits: 0  // Optional: Numerical precision. 0=round off.
  },
  staticZones: [
    { strokeStyle: "#F03E3E", min: -100, max: -50 }, // Red from 100 to 130
    { strokeStyle: "#dec535", min: -50, max: 0 }, // orange
    { strokeStyle: "#30B32D", min: 0, max: 50 }, // Green
    { strokeStyle: "#1ee619", min: 50, max: 100 }, // green +
  ],

};