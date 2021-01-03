const d3 = require("d3");


d3.csv("cities.csv")
	.then(data => {
		console.log(data[0])
	})
