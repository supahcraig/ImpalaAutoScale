import configparser
from configparser import ConfigParser


def get_configuration(config_name):
    config = ConfigParser()
    config.read('impala_autoscale.conf')

    if config_name in config:
        username = config[config_name]['username']
        password = config[config_name]['password']
        jdbc_url = config[config_name]['jdbc_url']

        configD = {'username': username, 'password': password, 'jdbc_url': jdbc_url}
        return configD

    else:
        raise KeyError(f'No configuration for [{config_name}] is found in impala_autoscale.conf')


def add_configuration(config_name):
    config = ConfigParser()
    config.read('impala_autoscale.conf')







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

    with open('impala_autoscale.conf', 'w') as configfile:
        config.write(configfile)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config',
                        help="the name of the config section create/update")

    args = parser.parse_args()

    if args.config:
        add_configuration(args.config)