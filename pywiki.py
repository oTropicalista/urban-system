#!/usr/bin/python
#------------------------------------------------------------------+
# Name: pywiki.py                                                  |
# Autor: oTropicalista                                             |
# Github: https://github.com/oTropicalista/                        |
# Repository: https://github.com/oTropicalista/urban-system        |
# Data: 14/12/2020                                                 |
#------------------------------------------------------------------+

# TODO
# pesquisar itens e trazer resultados
# ir para página específica


import os
import time
import pycurl
import argparse
from io import BytesIO
from bs4 import BeautifulSoup
from configparser import ConfigParser
from rich.console import Console
from rich.table import Table

class params:
    cfg = ConfigParser()
    cfg.read('config.txt')

    NAME = cfg['app']['NAME']
    VERSION = cfg['app']['VERSION']
    DESCRIPTION = cfg['app']['DESCRIPTION']
    AUTOR = cfg['app']['AUTOR']
    GITHUB = cfg['app']['GITHUB']
    TITLE = """
                          _ _    _ 
     _ __  _   ___      _(_) | _(_)
    | '_ \| | | \ \ /\ / / | |/ / |
    | |_) | |_| |\ V  V /| |   <| |
    | .__/ \__, | \_/\_/ |_|_|\_\_|
    |_|    |___/                 {}
    """.format(VERSION)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def msg(name=None):
    return """
    + Autor: {}
    + Github: {}

    pywiki.py [options] <NAME>
    [-S, --search]
    """.format(params.AUTOR, params.GITHUB)

def init():
    print(color.BLUE + color.BOLD + params.TITLE + color.END)
    
    # tratar os argumentos de entrada
    psr = argparse.ArgumentParser(description=''.format(), usage=msg())

    # argumentos
    psr.add_argument('Name',
                     metavar='name',
                     type=str,
                     help='Term for searching')
    psr.add_argument('-S',
                     action='store_true',
                     help='Flag for indicate searching')

    args = psr.parse_args()

    if args.S:
        search(args.Name)
    else:
        open_page(args.Name)

def search(name):
    pass

def open_page(name):
    pass

def get_html(url):
    # pegar pagina do AUR através da lib cUrl
    b_obj = BytesIO()
    crl = pycurl.Curl()

    crl.setopt(crl.URL, url)
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close() 

    get_body = b_obj.getvalue()

    return get_body.decode('utf-8')

if __name__ == "__main__":
    init()
