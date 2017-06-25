# -*- coding: utf-8 -*-

from bottle import template, html_escape, request
from config import CONFIG

def main_add(ADMIN):
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  templ += template('themes/Default/add_message.tpl')
  return templ


def doAdd(ADMIN, c, conn):
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  
  result = c.execute('INSERT INTO messages (title, txtBody, active) VALUES(?, ?, 1)', (html_escape(request.POST.utitle), html_escape(request.POST.ubody)))
  
  conn.commit()
  
  templ += template('themes/Default/message.tpl', msgid='', msg_title='رسالة إدارية', msg_body='تم إضافة رسالتك بنجاح.')
  return templ


