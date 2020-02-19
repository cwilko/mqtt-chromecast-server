# mqtt-chromecast-server

Receive urls and commands over MQTT, and chromecast those urls to a local device.

# Installation

Edit server.config file to identify the device name

Run the server using the following (Python3 required)

    pip install catt
    python server.py


# Docker

Run from a docker file using

    docker run --rm --network=host -v server.config:app/server.config cwilko/mqtt-chromecast-server
