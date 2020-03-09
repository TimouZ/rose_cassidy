# rose_cassidy
A simple application for creating time-lapse videos using RaspberryPi camera.

Firs of all you need to install OS on RPi and enable SSH or use keyboard + mouse + display.

How to discover your RPi in network
nmap -sn 192.168.0.0/24 – to discover raspberry IP

How to setup SSH on RPi
https://www.raspberrypi.org/documentation/remote-access/ssh/

How to connect camera to RPi and enable it 
https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera

How to setup application
Dev environment 
apt-get install python3.7
apt-get install python3-pip
pip install virtualenv 
pip install -r requirements.txt

to create photos
apt-get update
apt-get install ffmpeg

to play movie
apt install libdvdnav4 libdvdread4 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libdvd-pkg
apt install ubuntu-restricted-extras
