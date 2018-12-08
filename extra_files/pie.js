const url = "http://127.0.0.1:5000/collections/consumepersmokerperday";

// Fetch the JSON data and console log it
d3.json(url, function(data) {
  console.log(data)
});

function buildMetadata(sample) {

    var url = `/metadata/${sample}`;
  
    // @TODO: Complete the following function that builds the metadata panel
  
    // Use `d3.json` to fetch the metadata for a sample
  
    d3.json(url).then((meta) => {
      var entries_arr = [];
      entries_arr = (Object.entries(meta));
      // Use d3 to select the panel with id of `#sample-metadata`
      var metaPanel = d3.select("#plot3");
      // Use `.html("") to clear any existing metadata
      metaPanel.html("");
      // Use `Object.entries` to add each key and value pair to the panel
      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
      entries_arr.forEach((entry) => {
        metaPanel
          .append("p")
          .text(`${entry[0]}: ${entry[1]}`)
      })
    })
  }
  
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
  
  function buildCharts(sample) {
  
    var url = `/samples/${sample}`;
  
    // @TODO: Use `d3.json` to fetch the sample data for the plots
    d3.json(url, function(data) {
      var Code = [];
      var Entity = [];
      var cigarettes = [];
      Code = (Object.values(data)[0]);
      Entity = (Object.values(data)[1]);
      cigarettes = (Object.values(data)[2]);
  
    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    var cigarettes = sample_values.sort(function(a, b) {return b-a}).slice(0, 10)
    var pieTrace = [{
      values: cigarettes,
      labels: Entity,
      type: 'pie',
      hoverinfo: Entity
    }];
  
   // var pieData = [pieTrace]
  
    Plotly.newPlot("plot3", pieTrace);
  
    })
  }
  
  function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
    // Use the list of sample names to populate the select options
    d3.json("/names").then((sampleNames) => {
      var firstSample = sampleNames[0];
      sampleNames.forEach((sample) => {
        selector.append("option")
          .text(sample)
          .property("value", sample)
      })
      // Use the first sample from the list to build the initial plots
      buildCharts(firstSample);
      buildMetadata(firstSample);
    })
  }
  
  function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildCharts(newSample);
    buildMetadata(newSample);
  }
  
  // Initialize the dashboard
  init();

