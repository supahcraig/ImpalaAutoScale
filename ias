#!/usr/bin/env python

from xml.etree import ElementTree as et
import argparse
import configurations

def read_xml():
    tree = et.parse('config.jmx')
    root = tree.getroot()
    return root


def replace_username(root, username):
    root.find('.//stringProp[@name="username"]').text = username


def replace_password(root, password):
    root.find('.//stringProp[@name="password"]').text = password


def replace_dbUrl(root, dbUrl):
    root.find('.//stringProp[@name="dbUrl"]').text = dbUrl


def replace_sql(root, sql):
    root.find('.//stringProp[@name="query"]').text = sql


def write_config(root):
    with open('myconfig.jmx', 'wb') as f:
        tree = et.ElementTree(document_root)
        tree.write(f)


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', default='default', help="the name of the config section from impala_autoscale.conf to be used")
parser.add_argument('-s', '--sql', help="SQL statement to be used, overrides SQL provided using -F or --sqlFile")
parser.add_argument('-F', '--sqlFile', help="file containing SQL to be used, unless -s or --sql is present")

args = parser.parse_args()

if args.config:
    config_section = args.config
    print(f'Using config section {config_section}')

if args.sql:
    sql = args.sql
    if args.sqlFile:
        print(f'Overriding {args.sqlFile} with aurgment-supplied SQL statment')
    else:
        print('Using argument-supplied SQL')

if args.sqlFile and not args.sql:
    print(f'reading SQL from {args.sqlFile}')
    with open(args.sqlFile, 'r') as f:
        sql = f.read()

if not args.sqlFile and not args.sql:
    print('A query must be supplied using --sql OR --sqlFile')
    # TODO:  validate if > encoding to &gt; is going to work ok
    raise Exception('No SQL supplied either via command line argument or SQL file.')


# read boilerplate XML config for JMeter
document_root = read_xml()

# get specific config values from impala_autoscale.conf
config = configurations.get_configuration(config_section)

# replace placeholder values with actual values & write out myconfig.jmx
replace_username(root=document_root, username=config['username'])
replace_password(root=document_root, password=config['password'])
replace_dbUrl(root=document_root, dbUrl=config['jdbc_url'])
replace_sql(root=document_root, sql=sql)
write_config(root=document_root)
