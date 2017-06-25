# -*- coding: utf-8 -*-

from bottle import template, html_escape, request
from config import CONFIG

def main_install():
  templ = template('themes/Default/header.tpl', config=CONFIG)
  templ += template('themes/Default/add_message.tpl')
  return templ

