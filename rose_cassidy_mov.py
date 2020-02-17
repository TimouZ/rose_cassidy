import time
from os import system

def create_slowmo_movie():
    print('Converting to film now')
    system('avconv -r 24 -i image%04d.jpg -vcodec libx264 -crf 20 -g 15 `date +%H%M%%d%m%Y`timelapse.mp4')

    #create film
    print('moving completed mp4 file')
    system('mv *.mp4 ~/rose_cassidy/completed/')

    print('cleaning up old jpgs')
    system('rm *.jpg')

    print('Done')