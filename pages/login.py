# -*- coding: utf-8 -*-

from bottle import template, request, response, redirect
from config import CONFIG

def main_login(ADMIN):
  #ADMIN = admin
  if ADMIN:
    exit(redirect('/'))
    
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  templ += template('themes/Default/login.tpl', config=CONFIG, admin=ADMIN)
  
  return templ


def doLogin():

  if request.POST.uname == CONFIG['userName'] and request.POST.psw == CONFIG['userPass']:
  
    response.set_cookie('UNAME', request.POST.uname) #, True, hashlib.sha512)
    response.set_cookie('PSW', request.POST.psw) #, True, hashlib.sha512)
    
    msg = 'تم تسجيل الدخول بنجاح.'
  else:
    msg = 'فشل تسجيل الدخول.'
  
  ADMIN = True
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  templ += template('themes/Default/message.tpl', msgid='', msg_title='رسالة إدارية', msg_body = msg)
  
  return templ


def logout():
  response.set_cookie('UNAME', '') #, True, hashlib.sha512)
  response.set_cookie('PSW', '') #, True, hashlib.sha512)
  
  response.delete_cookie('UNAME')
  response.delete_cookie('PSW')
  
  #ADMIN = admin
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=False)
  templ += template('themes/Default/message.tpl', msgid='', msg_title='aaa', msg_body='aaaaaaaaaa')
  
  return templ
