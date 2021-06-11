# mh-z19_thingsboard

Supports MH-Z19 (co2) sensor conected to a single device.


# Connecting sensors


MH-Z19 to rpi pins

    2 - 5v vin power
  
    6 - Ground
  
    8 - UART0 TXD
  
    10 - UART0 RXD


# OS installation

Start with a fresh installation of Raspberry PI OS Lite

''sudo raspi-config''

Enalbe the i2c interface

# Update and reboot host
``sudo apt-get update -y && sudo apt-get upgrade -y && sudo reboot now``

# Install drivers and software 

``sudo apt-get install  i2c-tools  python3-pip  i2c-tools  git  -y``

``sudo pip3 install  mh-z19  smbus2  paho-mqtt``

clone repo and run 

``python3 read_mh-z19.py``


# uses

https://github.com/sfduff/docker_thingsboard

