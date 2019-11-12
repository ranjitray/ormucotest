import configparser
import os
import sys
from datetime import datetime


PAGE_LOAD_TIMEOUT = 20
IMPLICIT_WAIT = 10


def get_project_path():
    return os.path.abspath(os.path.dirname(__file__)+'/../')

def set_project_path():
    sys.path.append(get_project_path())

def get_properties(lable, key):
    cf = configparser.ConfigParser()
    propfile = get_project_path() + '/Config/Config.properties'
    cf.read(propfile)
    return cf.get(lable, key)






