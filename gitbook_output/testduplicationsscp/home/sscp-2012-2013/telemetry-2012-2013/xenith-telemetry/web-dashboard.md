# web-dashboard

## SSCP - Web dashboard

## Web dashboard

The web dashboard is a node.js app.

It lives in SVN: https://solarcar.stanford.edu:81/svn/website, then in trunk/nodejs/telemweb

It currently provides two views:

* The dashboard view shows the current state of the car. It shows the battery pack and the array, color coded by variables like voltage and temperature. It also shows speed and immediate power consumption.The graph view shows all available telemetry measurement (for example, "battery\_pack.module0.voltage"). You can take any combination and graph them. The graph supports zoom and pan (so you can go backward in time).
* The dashboard view shows the current state of the car. It shows the battery pack and the array, color coded by variables like voltage and temperature. It also shows speed and immediate power consumption.
* The graph view shows all available telemetry measurement (for example, "battery\_pack.module0.voltage"). You can take any combination and graph them. The graph supports zoom and pan (so you can go backward in time).
* The dashboard view shows the current state of the car. It shows the battery pack and the array, color coded by variables like voltage and temperature. It also shows speed and immediate power consumption.
* The graph view shows all available telemetry measurement (for example, "battery\_pack.module0.voltage"). You can take any combination and graph them. The graph supports zoom and pan (so you can go backward in time).

The dashboard view shows the current state of the car. It shows the battery pack and the array, color coded by variables like voltage and temperature. It also shows speed and immediate power consumption.

The graph view shows all available telemetry measurement (for example, "battery\_pack.module0.voltage"). You can take any combination and graph them. The graph supports zoom and pan (so you can go backward in time).

The dashboard view client-side code is in telemweb/static/js/dash.js

The graph view client-side code is in telemweb/static/js/telemgraph.js. It uses a graphing control--custom, but not solar car specific--it just draws line graphs: telemweb/static/js/graph.js

Both the dashboard and graph views use the same server-side REST API. The API is defined in telemweb/telemetry.js. API routes:

[REST](http://en.wikipedia.org/wiki/Representational_state_transfer)

* /  - HTML, shows a splash screen/trips - HTML, shows a list of trips with a link to each one/trips/(id) - HTML, shows the graph view for that trip/trips/(id)/dashboard - HTML, shows the dashboard view for that trip/trips/(id)/latest - JSON, gets the latest val for each measurement for that trip/timeseries - Tab-separated text, returns all values for a given measurement id, start time, and end time
* /  - HTML, shows a splash screen
* /trips - HTML, shows a list of trips with a link to each one
* /trips/(id) - HTML, shows the graph view for that trip
* /trips/(id)/dashboard - HTML, shows the dashboard view for that trip
* /trips/(id)/latest - JSON, gets the latest val for each measurement for that trip
* /timeseries - Tab-separated text, returns all values for a given measurement id, start time, and end time
* /  - HTML, shows a splash screen
* /trips - HTML, shows a list of trips with a link to each one
* /trips/(id) - HTML, shows the graph view for that trip
* /trips/(id)/dashboard - HTML, shows the dashboard view for that trip
* /trips/(id)/latest - JSON, gets the latest val for each measurement for that trip
* /timeseries - Tab-separated text, returns all values for a given measurement id, start time, and end time

/  - HTML, shows a splash screen

/trips - HTML, shows a list of trips with a link to each one

/trips/(id) - HTML, shows the graph view for that trip

/trips/(id)/dashboard - HTML, shows the dashboard view for that trip

/trips/(id)/latest - JSON, gets the latest val for each measurement for that trip

/timeseries - Tab-separated text, returns all values for a given measurement id, start time, and end time
