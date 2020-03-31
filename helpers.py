#!/usr/bin/env python3
"""
A module for helper functions
"""

import os
import configparser


# Config handling functions
def create_config(path):
    """Creates new config file with name 'path' using default setting values

    :param path: Config file
    :return: Nothing
    """
    config = configparser.ConfigParser()
    config.add_section("camera_settings")
    config.set("Resolution", "1920, 1080")
    config.add_section("photos_settings")
    config.set("SleepTime", "1")
    config.set("FrameCount", "5")
    config.add_section("environment_settings")
    config.set("Movie_dir", "/movie ready/")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """Returns ConfigParser object for further processing

    :param path: Config file
    :return: ConfigParser object
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    with open(path) as config_file:
        config.read_file(config_file)
    return config


def get_setting(path, section, setting):
    """Retrieves from a file and returns the specified setting

    :param path: Config file
    :param section: Section in file
    :param setting: Specified setting
    :return: Specified setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    message = "Get {section} {setting}".format(section=section, setting=setting)
    print(message)
    return value


def update_setting(path, section, setting, value):
    """Updates the specified setting in file

    :param path: Config file
    :param section: Section in file
    :param setting: Specified setting
    :param value: New value of the specified setting
    :return: Nothing
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """Deletes specified setting in config file

    :param path: Config file
    :param section: Section in file
    :param setting: Specified setting to delete
    :return:
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)
