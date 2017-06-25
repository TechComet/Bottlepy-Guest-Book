# -*- coding: utf-8 -*-

from bottle import template, request
from config import CONFIG
import sys, os, sqlite3

def main_admin(page, ADMIN, c):
  #ADMIN = admin_isAccess()
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  
  templ += template('themes/Default/admin_navbar.tpl', config=CONFIG, admin=ADMIN)
  
  if ADMIN == 1:
  
    if page == 'revision':
      result = c.execute('SELECT * FROM messages WHERE active<>1 ORDER BY msgid DESC')
      
      for msg in result.fetchall():
        templ += template('themes/Default/message.tpl', msgid=msg[0], msg_title=msg[1], msg_body=msg[2])
    
    elif page == 'search':
      templ += template('themes/Default/search_main.tpl', msg_title='بحث', result='')
      
    else:
    
      python = {
        'version': sys.version
      }
      
      server = {
        #'DESKTOP_SESSION': request.environ['DESKTOP_SESSION'],
        'name': request.environ['SERVER_NAME'],
        'port': request.environ['SERVER_PORT'],
        'wsgi_version': str(request.environ['wsgi.version'])[1:5],
        'sofrware': request.environ['SERVER_SOFTWARE'],
        'address': request.environ['REMOTE_ADDR']
      }
      
      db = {
        'type': CONFIG['dbType'],
        'name': os.path.basename(CONFIG['dbName']),
        'version': sqlite3.sqlite_version,
        'size': os.path.getsize(CONFIG['dbName']) / 1000
      }
      
      active_num = c.execute('SELECT count(*) FROM messages WHERE active=1').fetchone()[0]
      unactive_num = c.execute('SELECT count(*) FROM messages WHERE active<>1').fetchone()[0]
      
      templ += template('themes/Default/admin.tpl', active_num=active_num, unactive_num=unactive_num, server=server, db=db, python=python)
      
  else:
    redirect('/')
  
  return templ


def active(active_id, ADMIN, c):
  #ADMIN = admin_isAccess()
  result = c.execute('SELECT * FROM messages WHERE msgid=? LIMIT 1', (active_id,)).fetchone()
  
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  templ += template('themes/Default/confirm_message.tpl', msgid='', msg_title='هل انت متأكد من رغبتك في ' + ('تفعيل' if not result[3] else 'إلغاء تفعيل') + ' "' + result[1] + '" ؟', msg_body=result[2], action='/admin/active/' + str(active_id), txt_do='تفعيل؟' if not result[3] else 'إلغاء التفعيل؟')
  
  return templ


def doActive(active_id, ADMIN, c, conn):
  result = c.execute('SELECT * FROM messages WHERE msgid=? LIMIT 1', (active_id,)).fetchone()[3]
  result = c.execute('UPDATE messages SET active=? WHERE msgid=? LIMIT 1', (not result,active_id,))
  conn.commit()
  
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  templ += template('themes/Default/message.tpl', msgid='', msg_title='vvvvvvv', msg_body='doActive')
  
  return templ


def delete(delete_id, CONFIG, ADMIN, c):

  result = c.execute('SELECT * FROM messages WHERE msgid=? LIMIT 1', (delete_id,)).fetchone()
  
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  templ += template('themes/Default/confirm_message.tpl', msgid='', msg_title='هل انت متأكد من رغبتك في ' + ('حذف' if not result[3] else 'حذف') + ' "' + result[1] + '" ؟', msg_body=result[2], txt_do='تأكيد الحذف؟', action='/admin/delete/' + str(delete_id))
  
  return templ


def doDelete(delete_id, ADMIN, c, conn):

  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  templ += template('themes/Default/message.tpl', msgid='', msg_title='', msg_body='')
  
  return templ


def doSearch(ADMIN, c):
  #ADMIN = admin_isAccess()
  templ = template('themes/Default/header.tpl', config=CONFIG, admin=ADMIN)
  
  display = ' AND active='
  
  if request.POST.msgDisplay == 'active': display += '1'
  elif request.POST.msgDisplay == 'unactive': display += '0'
  else: display = ''
  
  if request.POST.search_type == 'search_bytitle':
    search = c.execute('SELECT * FROM messages WHERE title LIKE ? ORDER BY msgid DESC', ('%' + request.POST.input_search + '%' + display,))
  elif request.POST.search_type == 'search_bybody':
    search = c.execute('SELECT * FROM messages WHERE txtbody LIKE ? ORDER BY msgid DESC', ('%' + request.POST.input_search + '%' + display,))
  else:
    search = c.execute('SELECT * FROM messages WHERE (title LIKE ? OR txtbody LIKE ?) {} ORDER BY msgid DESC'.format(display), ('%' + request.POST.input_search + '%', '%' + request.POST.input_search + '%',))
  
  #c.comment()
  
  result = ''
  
  for result in search.fetchall():
    templ += str(search) + template('themes/Default/search_main.tpl', msg_title='نتائج البحث', result=result)
  else:
    if not result:
      templ += template('themes/Default/message.tpl',msgid='', msg_title='رسالة إدارية', msg_body='لم يتم العثور على رسائل تطابق بحثك.')
    
  return templ







