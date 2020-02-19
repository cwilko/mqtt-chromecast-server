# mqtt-chromecast-server

Receive urls and commands over MQTT, and chromecast those urls to a local device.

# Installation

Edit server.ini file to identify the device name

Run the server using the following (Python3 required)

    pip install catt
    pip install paho-mqtt
    python server.py


# Docker

Edit the server.ini file and run from a docker container using

    docker run --rm --network=host -v server.init:server.ini cwilko/mqtt-chromecast-server
