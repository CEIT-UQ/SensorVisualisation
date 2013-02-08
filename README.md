SensorVisualisation Version 0.9 08/01/2013

GENERAL USE
------------
SensorVisualisation is a simple webpage and webserver for visualising data collected by sensors within an area. Data is taken from an MQTT stream, a visualisation is processed, 
and the result is presented as an interactive webpage.

This package is useful for students looking to survey temperature, humidity or other variables 
within an environment or anyone else that is interested in visualising sensor data.
----------------------------------------------------------------------------------------------

Setup & Installation
---------------------

1. Install Dependencies:
	- nodejs
	http://nodejs.org/
	- SocketIO
	In Terminal type: npm install socket.io
	- Python 2.7
	http://www.python.org/download/
	- The Python PNG module: 
	http://packages.python.org/pypng/png.html


2. Configure the WebServer:

Open web_server.js in a text editor and change the following lines at the top of the file:

Change: var server = '';
    To: var server = [ip address of mqtt server];
    Eg: var server = 130.102.23.4;

Change: var topic = '';
    To: var topic = [put your data topic here];
    Eg: var tipoc = '/data/sensor/temperature';

Change: var io = require('socket.io').listen(#);
    To: var io = require('socket.it').listen([your website port number]);
    Eg: var io = require('socket.io').listen(5000);

Change: var client = new mqtt.MQTTClient(#, server, '');
    To: client = new mqtt.MQTTClient([mqtt server port number], server, [mqtt client name]);
    Eg: client = new mqtt.MQTTClient(1883, server, 'dataGrabber');

Change: visualisation_cmd = '';
    To: visualisation_cmd = 'python [your python visuliasation generation file]';

3. Create a visualisation generation script in Python

An example script 'heatmap.py' is supplied is the root directory.

The visualisation script should follow the general format :
	------------------------------------------------------
	# Load data from data.json & sensors.json

	# Manipulate the data above 

	# Create a PNG compliant list

	# Save the PNG
	------------------------------------------------------

4. Choose Area Image Overlays:

Create or choose an overlay image for your visualisation.
Example images can be seen in the root directory.
The images should be made so that transparent regions are the parts of the image that will 
show the underlying visulisation layer.

5. Testing:

Run the web server:

In Terminal type:
$ cd /directory/of/the/web/server
$ node web_server.js

In a web browser open index.html

If everything worked correctly you should see your visualisation in your web browser that 
updates automatically when new data is published to your specified MQTT topic.
----------------------------------------------------------------------------------------------

Contact Me:

Email: roscoe.hart@me.com
