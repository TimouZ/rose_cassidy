#!/usr/bin/env python3
"""Movie converter

The script converts photos to time-lapse movie

"""

import os
import helpers

CONFIG_FILE_NAME = 'rose_cassidy.ini'


def create_timelapse_movie():
    """Creates time-lapse movie and moves it to specific directory

    :return:
    """
    # Initial movie settings
    movie_dir = helpers.get_setting(CONFIG_FILE_NAME, 'Environment', 'movie_dir')

    # TODO Replace this printings with logging
    print('-------Converting photos to movie now-------')
    os.system('ffmpeg -r 24 -i image%04d.jpg -vcodec libx264 -crf 20 -g 15 `date +%Y%m%d%H%M`timelapse.mp4')
    print('----------------Movie ready-----------------')

    # TODO Replace this printings with logging
    # Checking if dir exists or creating directory
    if not os.path.exists(movie_dir):
        print('Can`t find dir for movie, creating...')
        try:
            os.mkdir(movie_dir)
        except Exception as e:
            print('Can`t create dir for movie, error {} occured '.format(e))

    print('Moving completed mp4 file')
    os.system('mv *.mp4 {}'.format(movie_dir))

    print('Cleaning up old jpgs')
    os.system('rm *.jpg')

    print('Done')
