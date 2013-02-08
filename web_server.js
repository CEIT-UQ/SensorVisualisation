// Requires
var sys = require('sys');
var net = require('net');
var mqtt = require('./mqtt');
var fs = require('fs');
var exec = require('child_process').exec
var child;

// Configure
var server = '';
var topic = ''
var io  = require('socket.io').listen(#);
var client = new mqtt.MQTTClient(#, server, '');
var visualisation_cmd = '';

function generateVisualisation(s_info, s_data) {
    exec(visualisation_cmd, 
        function (error, stdout, stderr) {
        sys.print('stdout: ' + stdout);
        sys.print('stderr: ' + stderr);
        if (error !== null) {
            console.log('exec error: ' + error);
        }
        console.log("GENERATION END");
        io.sockets.emit('refresh_visualisation', {"data": "none"});
    });
}

// Load 'retained' data
var sensor_data;
sensor_data = require('./data.json');

// Load sensor info
var sensor_info;
sensor_info = require('./sensors.json');

// When connected to a client
io.sockets.on('connection', function (socket) {

    // Subscribe to the topic
    console.log('Subscribing to ' + topic);
    client.subscribe(topic);
    
    // Give client the 'retained' data
    io.sockets.emit('retained', sensor_data);
    io.sockets.emit('sensor_info', sensor_info);
});
 
// When receiving data
client.addListener('mqttData', function(topic, payload){
    console.log('got some data');

    // Genereate the visualisation textures
    generateVisualisation();

    // Update the 'retained' data
    data = JSON.parse(payload);
    sensor_data[data.id] = data.value;
  
    fs.writeFile(__dirname + "/data.json", JSON.stringify(sensor_data), 'utf8', function(err) {
        if(err) {
            console.log(err);
        } else {
            console.log("Retained Data Updated...");
        }
    });
    
    // Emit the MQTT payload
    io.sockets.emit('mqtt',{'topic':String(topic), 'payload':String(payload)});
});


