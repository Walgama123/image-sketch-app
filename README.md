
<h1 align="center">Image to Pencil Sketch </h1>
<h3 align="center">Python & JavaScript</h1>
<div align="center">
	<img src="/image-sketch-app/images/final.png">
</div>


## Background.
The United States Geological Survey, or USGS for short, is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment, and the impacts of climate and land-use change.
Their scientists develop new methods and tools to supply timely, relevant, and useful information about the Earth and its processes.
The USGS is interested in building a new set of tools that will allow them to visualize their earthquake data.
They collect a massive amount of data from all over the world each day, but they lack a meaningful way of displaying it.
In this challenge, you have been tasked with developing a way to visualize USGS data that will allow them to better educate the public and other government organizations (and hopefully secure more funding) on issues facing our planet.

## Data sources.
- [The United States Geological Survey](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson)
- [Tectonic Plates](https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_plates.json)

## Tools and libraries used
- [D3.js](https://d3js.org/d3.v7.min.js)
- [Leaflet CSS](https://unpkg.com/leaflet@1.9.4/dist/leaflet.css)
- [Leaflet JavaScript](https://unpkg.com/leaflet@1.9.4/dist/leaflet.css)

## Activities. 
- [Leaflet-Part-1.](Leaflet-Part-1/static/js/logic.js)
  - [Create the street map tile layer that will be the background of our map.](https://www.openstreetmap.org) 
  - Create a baseMaps object to hold the street map layer.
  - Create legend control ti display the color code as per the magnitude.
  - Create functions that returns the size of the marker and color codes according to the magnitude.
  - sample_values - Value of the bacteria found in the sample.
  - Create creatEqMap function to plot the earthquake markers.
  - Create createEQMarkers function that create the marker group.
  - Import data from the website and calling the functions to deploy the map.  
- [Leaflet-Part-2.](Leaflet-Part-2/static/js/logic.js)
  - [Create the satellite map tile layer that will be the background of our map.](http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}) 
  - [Create topo layer.](https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png)
  - [Creat outdoor layer.](https://www.openstreetmap.org/copyright)
  - Create a baseMaps object to hold the three views layers.
  - Create legend control ti display the color code as per the magnitude.
  - Create functions that returns the size of the marker and color codes according to the magnitude.
  - sample_values - Value of the bacteria found in the sample.
  - Create creatEqMap function to plot the earthquake markers.
  - Create createEQMarkers function that create the marker group.
  - Import data from the website and calling the functions to deploy the map.  
  

## Functions.
- markerSize  : This function accept the magnitude of the earthquake and return the size of the marker accordingly.
- markerColor : This function accept the depth of the earthquake and return the marker color.
- creatEqMap  : This function create the base map accepting one argument (layer group).
- createEQMarkers : This function create the markers and the layer group and pass it to create the map.

## How to run the code.
- Create a new folder in your local machine.
- Download both Leaflet-Part-1 and the Leaflet-Part-2 folders from the GitHub.
- [Open the newly created folder by using VS code.](https://visualstudio.microsoft.com/downloads/)
- [Run the index.html by open with live server ](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)