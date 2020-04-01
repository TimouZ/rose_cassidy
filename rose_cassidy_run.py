#!/usr/bin/env python3
"""Time-lapse movie maker

The script allows user to create time-lapse movie from photo

"""

import time
import picamera
from rose_cassidy_mov import create_timelapse_movie
import helpers

CONFIG_FILE_NAME = 'rose_cassidy.ini'


def run_cam():
    camera = picamera.PiCamera()

    sleep_time = int(helpers.get_setting(CONFIG_FILE_NAME, 'Photos', 'sleep_time'))
    frame_count = int(helpers.get_setting(CONFIG_FILE_NAME, 'Photos', 'frame_count'))

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
