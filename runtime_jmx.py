from xml.etree import ElementTree as ET


def read_xml():
    tree = ET.parse('config.jmx')
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
    # TODO:  validate if > encoding to &gt; is going to work ok


def write_config(root):
    with open('myconfig.jmx', 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f)
