#!/usr/bin/python
import time
from os import system

from picamera import PiCamera
import configparser

from rose_cassidy_mov import create_film

def init_data(config_file_name):
    global SLEEP_TIME
    global START_FRAME
    global STOP_FRAME

    config = configparser.ConfigParser()
    config.read(config_file_name)
    camera.resolution = config['DEFAULT']['Resolution']
    SLEEP_TIME = config['DEFAULT']['SleepTime']
    START_FRAME = config['DEFAULT']['FrameCount']
    STOP_FRAME = config['DEFAULT']['FrameStop']

def run_cam():

    camera = PiCamera()
    init_data(rose_cassidy.ini)

    print('Photography process will take approximately ', str(int(STOP_FRAME) * int(SLEEP_TIME) / 60), ' minutes')
    print('Taking photos now')


    for _ in range(STOP_FRAME):
        print('Picture: ' + str(START_FRAME) + ' of ' + str(STOP_FRAME))
        camera.capture('image' + str(START_FRAME).zfill(4) + '. jpg')
        time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    run_cam()
    create_slowmo_movie()
