<!DOCTYPE html>
<html dir="rtl">
  <head>
  	<meta charset="UTF-8" />
  	<title>{{config['siteTitle']}}</title>
  	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
  	<link rel="stylesheet" type="text/css" media="screen" href="/css" />
  </head>

<body>

<div class="container">
  <div class="breadcrumb">
    <h1>{{config['siteTitle']}}</h1>
    <p>{{config['siteDescription']}}</p>
  </div>
</div>
<div class="container">
  <ul class="breadcrumb">
    <li><a href="/">الرئيسية</a></li>
    % if admin == True:
    <li><a href="/admin">الإدارة</a></li>
    <li><a href="/logout">خروج</a></li>
    % else:
    <li><a href="/add">إضافة</a></li>
    <li><a href="/login">دخول</a><!--//<a href="#login" onclick="document.getElementById('id01').style.display='block'">دخول</a>--></li>
    % end
  </ul>
</div>
