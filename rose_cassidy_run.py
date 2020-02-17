#!/usr/bin/python
import time
from os import system

from picamera import PiCamera
import configparser

from rose_cassidy_mov import create_slowmo_movie

def init_data(config_file_name):
    global SLEEP_TIME
    global START_FRAME
    global STOP_FRAME
    global CAM_RESOLUTION

    config = configparser.ConfigParser()
    config.read(config_file_name)
    #CAM_RESOLUTION = tuple(config['DEFAULT']['Resolution'])
    SLEEP_TIME = int(config['DEFAULT']['SleepTime'])
    START_FRAME = int(config['DEFAULT']['FrameCount'])
    STOP_FRAME = int(config['DEFAULT']['FrameStop'])

def run_cam():

    camera = PiCamera()
    init_data('rose_cassidy.ini')
    #camera.resolution = CAM_RESOLUTION

    print('Photography process will take approximately ', str(int(STOP_FRAME) * int(SLEEP_TIME) / 60), ' minutes')
    print('Taking photos now')


    for frame in range(STOP_FRAME):
        print('Picture: ' + str(frame) + ' of ' + str(STOP_FRAME))
        camera.capture('image' + str(frame).zfill(4) + '.jpg')
        time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    run_cam()
    create_slowmo_movie()
