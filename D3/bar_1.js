var data = [4, 8, 15, 16, 20, 32,42, 100];

var width = 200, barHeight = 20;
	
var chart = d3.select(".chart")
    .attr("width", width)
    .attr("height", barHeight * data.length);
	
var bar = chart.selectAll("g")
    .data(data)
  .enter().append("g")
    .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
	
bar.append("rect")
    .attr("width", function(d){return d * 10;})
    .attr("height", barHeight - 1);	
	
bar.append("text")
    .attr("x", function(d) { return d * 10 - 3; })
    .attr("y", barHeight / 2)
    .attr("dy", ".35em")
    .text(function(d) { return d; });