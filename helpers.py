#!/usr/bin/env python3
"""
A module for helper functions
"""

import os
import configparser


def create_config(path):
    """
    :param path:
    :return:
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
    """
    :param path:
    :return:
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    with open(path) as config_file:
        config.read_file(config_file)
    return config


def get_setting(path, section, setting):
    """
    :param path:
    :param section:
    :param setting:
    :return:
    """
    config = get_config(path)
    value = config.get(section, setting)
    message = "Get {section} {setting}".format(section=section, setting=setting)
    print(message)
    return value


def update_setting(path, section, setting, value):
    """
    :param path:
    :param section:
    :param setting:
    :param value:
    :return:
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    :param path:
    :param section:
    :param setting:
    :return:
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)
