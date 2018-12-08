// Zips for each item out of two arrays together and returns an array of objects
function JSONify(arr1, arr2) {
        var JSONdata = [];
        var o;
        arr1.forEach(function(e, i) {
            o = arr2[i];
            JSONdata.push({e, o});
        })
        return JSONdata;
    }

// Function that takes removes duplicates in an array and returns a new array
function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}

// Filter JSON based on entity/country
function filterbyEntity(JSON, val) {
    var filteredData = [];
    JSON.forEach(function(data) {
        if (data.Entity === val) {
            filteredData.push(data);
        }
    });
    return filteredData;
}

// Set height and width of SVGs
var svgWidth = 1000;
var svgHeight = 500;

// Set margins
var margin = {
    top: 30,
    right: 30,
    bottom: 100,
    left: 30
}

// Set the height and width of the actual plot/chart
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create the barChartSVG
var barChartSVG = d3.select("#barChart")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// Create the lineChartSVG
var lineChartSVG = d3.select("#lineChart")
    .append("svg")
    .attr("width", svgWidth + 40)
    .attr("height", svgHeight);

// Add an SVG group to each chart
var barChartGroup = barChartSVG.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

var lineChartGroup = lineChartSVG.append("g")
    .attr("transform", `translate(${margin.left + 30}, ${margin.top})`);

// Links to RESTful APIs
const barLink = "http://127.0.0.1:5000/collections/avgpricepack";
const lineLink = "http://127.0.0.1:5000/collections/numdeathstobaccosmoking";

// Time parser for d3
var parseTime = d3.timeParse("%Y");

d3.json(barLink, function(error, barJSON) {
    if (error) throw error;

    // Creates arrays for filtered data
    var entityArr = [];
    var cigPricesArr = [];

    // Filters JSON based on the year of 2014 and pushes the parsed data
    barJSON.forEach(function(data) {
        if (data.Year === 2014) {
            entityArr.push(data.Entity);
            cigPricesArr.push(+Object.values(data).slice(2, 3));
        }
    })

    // Creates the scales based on the data
    var xScaleD = d3.scaleBand()
        .domain(entityArr)
        .range([0, width])
        .padding(.1);
    var yScaleD = d3.scaleLinear()
        .domain([0, d3.max(cigPricesArr)])
        .range([height, 0]);

    // Creates the axes based on the data
    var bottomAxis = d3.axisBottom(xScaleD);
    var leftAxis = d3.axisLeft(yScaleD);

    // Appends bottom axis svg group to svg
    var xAxis = barChartGroup.append("g")
        .classed("x-axis", true)
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis)
        .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", "-.55em")
        .attr("transform", "rotate(-45)");

    // Appends the left axis to the svg
    var yAxis = barChartGroup.append("g")
        .classed("y-axis", true)
        .call(leftAxis);

    // Stores the JSONified version of two arrays in a var
    var objDJSON = JSONify(entityArr, cigPricesArr)

    // Creates the bar chart
    var barChart = barChartGroup.selectAll(".bar")
        .data(objDJSON)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .style("fill", "orange")
        .attr("x", d => xScaleD(d.e))
        .attr("y", d => yScaleD(d.o))
        .attr("width", xScaleD.bandwidth())
        .attr("height", d => height - yScaleD(d.o));

    // Creates the tool tips
    var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -60])
        .html(function(d) {
            return (`<b>Avg Price per Pack</b> (<i>in Int'l Dollars</i>)<br/><br/>${d.e}: $${d.o}`);
        });

    // Calls the tool tips to the bar chart
    barChart.call(toolTip);

    // Adds interaction for the tool tips to activate
    barChart.on("mouseover", function(data) {
        toolTip.show(data);
    })
        .on("mouseout", function(data) {
            toolTip.hide(data);
        });

})

// Function that creates line chart
function lineChartMaker(countryName) {

    d3.json(lineLink, function(error, lineJSON) {
        if (error) throw error;

        // Stores the filtered JSON (by country/region) into a var
        var countryData = filterbyEntity(lineJSON, countryName);
    
        // Creates the appropriate scales for the data provided
        var xTimeScale = d3.scaleTime()
            .range([0, width])
            .domain(d3.extent(countryData, d => d.Year));
        var yLinearScale = d3.scaleLinear()
            .range([height, 0])
            .domain([0, d3.max(countryData, d => d.smokeCount)]);

        // Creates the axes for which the plots
        var bottomAxis = d3.axisBottom(xTimeScale);
        var leftAxis = d3.axisLeft(yLinearScale);

        // Clears the line chart when a new option is chosen
        lineChartGroup.html("")

        // Creates a map to draw a line based on the data
        var drawLine = d3
            .line()
            .x(d => xTimeScale(d.Year))
            .y(d => yLinearScale(d.smokeCount));

        // Appends a line to the svg
        lineChartGroup.append("path")
            .attr("d", drawLine(countryData))
            .classed("line", true);

        // Appends the left axis
        lineChartGroup.append("g")
            .classed("axis", true)
            .call(leftAxis);

        // Appends the bottom axis
        lineChartGroup.append("g")
            .classed("axis", true)
            .attr("transform", `translate(0, ${height})`)
            .call(bottomAxis);

    })
}

// Function that initializes the line chart
function init() {
    d3.json(lineLink, function(error, JSON) {
        if (error) throw error;

        // Creates an array based on the countries/regions in JSON
        var entityArr = JSON.map((d) => d.Entity)

        // Removes duplicates
        var uniqueEntities = entityArr.filter(onlyUnique);

        // Selects the select HTML tag
        var selector = d3.select("#selDataset");
        
        // Grabs the first val in the arr
        var initEnt = uniqueEntities[0];

        // Appends options based on the unique entities in the arr
        uniqueEntities.forEach((Ent) => {
            selector.append("option")
            .text(Ent)
            .property("value", Ent)
        })

        // Creates a line chart based on the first val of the arr
        lineChartMaker(initEnt);
    })
}

// Function that makes a new line chart based on the val chosen by the end user
function optionChanged(newEnt) {
    lineChartMaker(newEnt);
}

// Initializes line chart
init();
