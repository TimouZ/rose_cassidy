#!/usr/bin/env python3
import time
import os
import configparser
from os import system

CONFIG_FILE_NAME = 'rose_cassidy.ini'


def init_data(config_file_name):
    global MOVIE_DIR
    config = configparser.ConfigParser()   
    try: 
        with open(config_file_name) as config_file:
            config.read_file(config_file)
            MOVIE_DIR = config.get('environment_settings','Movie_dir')
    except Exception as e:
        print('Can`t read config file {}, error {} occured '.format(config_file_name, e))


def create_timelapse_movie():
    init_data(CONFIG_FILE_NAME)    
    
    print('-------Converting photos to movie now-------')
    system('ffmpeg -r 24 -i image%04d.jpg -vcodec libx264 -crf 20 -g 15 `date +%Y%m%d%H%M`timelapse.mp4')
    print('----------------Movie ready-----------------')
    
     #Checking directory and creating directory
    if not os.path.exists(MOVIE_DIR):
        print('Can`t find dir for movie, creating...')
        try: 
            os.mkdir(MOVIE_DIR)
        except Exception as e:
            print('Can`t create dir for movie, error {} occured '.format(e))
 
    print('Moving completed mp4 file')
    system('mv *.mp4 {}'.format(MOVIE_DIR))

    print('Cleaning up old jpgs')
    system('rm *.jpg')

    print('Done')
