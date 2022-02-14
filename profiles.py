#!/usr/bin/env python

import configparser
from configparser import ConfigParser

config_filename = '.impala_autoscale.conf'

def mask_password(password):
    return "*******" + password[-3:]


def list_profiles():
    profile = ConfigParser()
    profile.read(config_filename)

    for section in profile.sections():
        print(f'Impala profile [{section}]:')
        print(f'username = {profile[section]["username"]}')
        print(f'password = {mask_password(profile[section]["password"])}')
        print(f'jdbc_url = {profile[section]["jdbc_url"]}\n')


def get_profile(profile_name):
    profile = ConfigParser()
    profile.read(config_filename)

    if profile_name in profile:
        username = profile[profile_name]['username']
        password = profile[profile_name]['password']
        jdbc_url = profile[profile_name]['jdbc_url']

        return {'username': username, 'password': password, 'jdbc_url': jdbc_url}

    else:
        raise KeyError(f'No configuration for [{profile_name}] is found in {config_filename}')


def add_profile(config_name):
    profile = ConfigParser()
    profile.read(config_filename)

    # attempt to fetch existing profile to show user existing values
    try:
        existing_profile = get_profile(config_name)
        existing_user = existing_profile['username']
        existing_password = existing_profile['password']
        existing_jdbc_url = existing_profile['jdbc_url']

    except KeyError:
        # thrown if profile isn't returned in get_profile()
        # custom exception might be better since we're using a dictionary which *could* also throw a KeyError
        existing_user = ''
        existing_password = ''
        existing_jdbc_url = ''

    # allows user to "enter" through to keep existing values
    # TODO: don't display ***** for a null password
    username = input(f'CDP Username [{existing_user}]: ') or existing_user
    password = input(f'password= [{mask_password(existing_password)}]: ') or existing_password
    jdbc_url = input(f'jdbc_url= [{existing_jdbc_url}]: ') or existing_jdbc_url

    try:
        profile.add_section(config_name)

    except configparser.DuplicateSectionError:
        # just don't add the section if it already exists
        pass

    finally:
        profile.set(config_name, 'username', username)
        profile.set(config_name, 'password', password)
        profile.set(config_name, 'jdbc_url', jdbc_url)

    with open(config_filename, 'w') as configfile:
        profile.write(configfile)
