# rose_cassidy

A simple application for creating time-lapse videos using RaspberryPi camera.

### Prerequisites

Firs of all you need to install OS on RPi and enable SSH or use keyboard + mouse + display.

How install OS:
https://www.raspberrypi.org/documentation/installation/installing-images/

How to discover your RPi in network:
```
nmap -sn 192.168.0.0/24 – to discover raspberry IP
```
How to setup SSH on RPi
https://www.raspberrypi.org/documentation/remote-access/ssh/

How to connect camera to RPi and enable it 
https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera

**Dev environment deployment**

1. Install python and virtualenv
```
apt-get install python3.7
apt-get install python3-pip
pip install virtualenv 
```
2. Create and activate virualenv

3. Install packages to create photos
```
apt-get update
apt-get install ffmpeg
```
4. Install packages to create movies
```
apt install libdvdnav4 libdvdread4 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libdvd-pkg
apt install ubuntu-restricted-extras
```

### Installing

```
pip install -r requirements.txt
```

### Usage

1. Open and edit rose_cassidy.ini
2. Run application
```
python3 rose_cassidy_run.py
```
3. Open and enjoy time-lapse ready movie


