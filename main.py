#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import sqlite3, os
from bottle import route, hashlib, redirect, response, html_escape, request, template, static_file, abort, error
from config import CONFIG
import sys
from math import ceil

if sys.version_info < (3, 0):
  reload(sys).setdefaultencoding('UTF8')

def get_hash(string):
  return hashlib.sha512(string.encode('utf8')).hexdigest()

def get_cookie(key):
  if sys.version_info < (3, 0):
    get_cookie_ = get_hash(request.get_cookie(key, ''))
  else:
    get_cookie_ = get_hash(request.get_cookie(key, '').encode('latin1').decode('utf8'))
    
  return get_cookie_


def check_admin():
  return get_cookie('UNAME') == get_hash(CONFIG['userName']) and get_cookie('PSW') == get_hash(CONFIG['userPass'])

def admin_isAccess():
  admin = check_admin()
  if admin:
    return admin
  else:
    abort(404) #exit(redirect('/'))

conn = sqlite3.connect(CONFIG['dbName'])
c = conn.cursor()


@route('/install')
def install():
  from pages.add import main_install
  return main_install()

@route('/css')
def css():
  return static_file('style.css', root='./css/')

@route('/')
@route('/p/<p_id:int>')
@route('/<m_id:int>')
def main(p_id=1, m_id=''):
  ADMIN = check_admin()
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)

  numRows = c.execute('SELECT COUNT(msgid) FROM messages WHERE active=1').fetchone()[0]

  if m_id:
    result = c.execute('SELECT * FROM messages WHERE msgid=? LIMIT 1', (m_id,))
  else:
    result = c.execute('SELECT * FROM messages WHERE active=1 ORDER BY msgid DESC LIMIT ?, ?', ((p_id - 1) * CONFIG['num_rows'], CONFIG['num_rows']))

  msg = ''

  for msg in result.fetchall():
    templ += template('themes/Default/message.tpl',msgid=msg[0] ,msg_title='{{msg_title}}', msg_body=msg[2]).replace('{{msg_title}}', '<a href="' + str(msg[0]) + '">' + msg[1] + '</a>')
    #templ += template('themes/Default/message.tpl',msgid=msg[0] ,msg_title=msg[1], msg_body=msg[2])

  else:
    if not msg:
      templ += template('themes/Default/message.tpl', msgid='' , msg_title='رسالة إدارية', msg_body='لا يوجد رسائل حالياً.')
    
    if not m_id:
      for i in range(1, int(ceil(numRows / CONFIG['num_rows'])) + 1):
        if p_id == i:
          templ += '{} | '.format(i)
        else:
          templ += '<a href="/p/{}">{}</a> | '.format(i, i)
    
  return templ

@route('/add')
def add():
  from pages.add import main_add
  return main_add(check_admin())


@route('/add', method='POST')
def doAdd():
  from pages.add import doAdd
  
  return doAdd(check_admin(), c, conn)


@route('/login')
def login():

  from pages.login import main_login
  
  return main_login(check_admin())

@route('/login', method='POST')
def doLogin():

  from pages.login import doLogin
  
  return doLogin()


@route('/logout')
def logout():
  from pages.login import logout
  return logout()


@route('/dbBackup')
def databaseBackup():
  if admin_isAccess():
    return static_file(CONFIG['dbName'], root='', download=True)

@route('/admin')
@route('/admin/<page>')
def admin(page=''):

  from pages.admin import main_admin
  return main_admin(page, admin_isAccess(), c)


@route('/admin/delete/<delete_id:int>')
def delete(delete_id):

  from pages.admin import delete
  return delete(delete_id, CONFIG, admin_isAccess(), c)


@route('/admin/delete/<delete_id:int>', method='POST')
def doDelete(delete_id):

  from pages.admin import doDelete
  return doDelete(delete_id, admin_isAccess(), c, conn)


@route('/admin/active/<active_id:int>')
def active(active_id):

  from pages.admin import active
  return active(active_id, admin_isAccess(), c)


@route('/admin/active/<active_id:int>', method='POST')
def doActive(active_id):

  from pages.admin import doActive
  return doActive(active_id, admin_isAccess(), c, conn)


@route('/admin/search', method='POST')
def doSearch():

  from pages.admin import doSearch
  return doSearch(admin_isAccess(), c)


@error(404)
def error404(error):
  ADMIN=check_admin()
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  return static_file('404.html', root='./statics')

