#!/usr/bin/python3
import time
from os import system
from os import path

from picamera import PiCamera
import configparser

from rose_cassidy_mov import create_slowmo_movie

CONFIG_FILE_NAME = 'rose_cassidy.ini'


def init_data(config_file_name):
    global SLEEP_TIME
    global FRAME_COUNT
    global CAMERA_RESOLUTION

    config = configparser.ConfigParser()
    
    try: 
        with open(config_file_name) as config_file:
            config.read_file(config_file)
           
            #CAMERA_RESOLUTION = config.get('camera_settings','Resolution')
            SLEEP_TIME = int(config.get('camera_settings', 'SleepTime'))
            FRAME_COUNT = int(config.get('camera_settings','FrameCount'))
            
    except Exception as e:
        print('Can`t read config file {}, error {} occured '.format(config_file_name, e))
        

def run_cam():

    camera = PiCamera()
    init_data(CONFIG_FILE_NAME)
    #camera.resolution(CAMERA_RESOLUTION)

    print('Photography process will take approximately ', str(int(FRAME_COUNT) * int(SLEEP_TIME) / 60), ' minutes')
    print('Taking photos now')

    try:
        for frame in range(FRAME_COUNT):
            print('Picture: ' + str(frame) + ' of ' + str(FRAME_COUNT))
            camera.capture('image' + str(frame).zfill(4) + '.jpg')
            time.sleep(SLEEP_TIME)
    except Exception as e:
        pass
    else:
        print('No errors occured during the photographing process.')
    finally:
        camera.close()

if __name__ == '__main__':
    run_cam()
    create_slowmo_movie()
