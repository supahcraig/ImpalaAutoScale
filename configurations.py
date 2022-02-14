#!/usr/bin/env python

import configparser
from configparser import ConfigParser

config_filename = '.impala_autoscale.conf'

def mask_password(password):
    return "*******" + password[-3:]


def list_configurations():
    config = ConfigParser()
    config.read(config_filename)

    for section in config.sections():
        print(f'Impala profile [{section}]:')
        print(f'username = {config[section]["username"]}')
        print(f'password = {mask_password(config[section]["password"])}')
        print(f'jdbc_url = {config[section]["jdbc_url"]}\n')


def get_configuration(config_name):
    config = ConfigParser()
    config.read(config_filename)

    if config_name in config:
        username = config[config_name]['username']
        password = config[config_name]['password']
        jdbc_url = config[config_name]['jdbc_url']

        #configD = {'username': username, 'password': password, 'jdbc_url': jdbc_url}
        return {'username': username, 'password': password, 'jdbc_url': jdbc_url}

    else:
        raise KeyError(f'No configuration for [{config_name}] is found in {config_filename}')


def add_configuration(config_name):
    config = ConfigParser()
    config.read(config_filename)

    # attempt to fetch existing profile to show user existing values
    try:
        existing_profile = get_configuration(config_name)
        existing_user = existing_profile['username']
        existing_password = existing_profile['password']
        existing_jdbc_url = existing_profile['jdbc_url']

    except KeyError:
        pass

    # allows user to "enter" through to keep existing values
    username = input(f'CDP Username [{existing_user}]: ') or existing_user
    password = input(f'password= [{mask_password(existing_password)}]: ') or existing_password
    jdbc_url = input(f'jdbc_url= [{existing_jdbc_url}]: ') or existing_jdbc_url

    try:
        config.add_section(config_name)

    except configparser.DuplicateSectionError:
        # just don't add the section if it already exists
        pass

    finally:
        config.set(config_name, 'username', username)
        config.set(config_name, 'password', password)
        config.set(config_name, 'jdbc_url', jdbc_url)

    with open(config_filename, 'w') as configfile:
        config.write(configfile)
