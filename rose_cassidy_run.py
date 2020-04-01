#!/usr/bin/env python3

import time
import os
import configparser

from picamera import PiCamera

from rose_cassidy_mov import create_timelapse_movie
import helpers

CONFIG_FILE_NAME = 'rose_cassidy.ini'


def run_cam():
    camera = PiCamera()
    camera_resolution = helpers.get_setting(CONFIG_FILE_NAME, 'Camera', 'resolution')
    sleep_time = int(helpers.get_setting(CONFIG_FILE_NAME, 'Photos', 'sleep_time'))
    frame_count = int(helpers.get_setting(CONFIG_FILE_NAME, 'Photos', 'frame_count'))
    #camera.resolution(CAMERA_RESOLUTION)

    print('Photography process will take approximately ', str(int(frame_count) * int(sleep_time) / 60), ' minutes')
    print('Taking photos now...')

    try:
        for frame in range(frame_count):
            print('Picture: ' + str(frame) + ' of ' + str(frame_count))
            camera.capture('image' + str(frame).zfill(4) + '.jpg')
            time.sleep(sleep_time)
    except Exception as e:
        print('Can`t take photos, error {} occured '.format(e))
    else:
        print('No errors occured during the photographing process.')
    finally:
        camera.close()

if __name__ == '__main__':
    run_cam()
    create_timelapse_movie()
