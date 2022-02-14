#!/usr/bin/env python

import configparser
from configparser import ConfigParser

config_filename = '.impala_autoscale.conf'


def list_configurations():
    config = ConfigParser()
    config.read(config_filename)

    for section in config.sections():
        print(f'Impala profile [{section}]:')
        print(f'username = {config[section]["username"]}')
        print(f'password = { "*******" + config[section]["password"][-3:]}')
        print(f'jdbc_url = {config[section]["jdbc_url"]}\n')

def get_configuration(config_name):
    config = ConfigParser()
    config.read(config_filename)

    if config_name in config:
        username = config[config_name]['username']
        password = config[config_name]['password']
        jdbc_url = config[config_name]['jdbc_url']

        configD = {'username': username, 'password': password, 'jdbc_url': jdbc_url}
        return configD

    else:
        raise KeyError(f'No configuration for [{config_name}] is found in {config_filename}')


def add_configuration(config_name):
    config = ConfigParser()
    config.read(config_filename)

    # TODO: present existing values if the config section already exists, e.g. aws configure
    username = input('username= ')
    password = input('password= ')
    jdbc_url = input('jdbc_url= ')

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
