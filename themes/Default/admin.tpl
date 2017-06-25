<div class="container" style="width:50%;float:right">
  <div class="panel-group">
    <div class="panel panel-default">
      <div class="panel-heading">إحصائيات الموقع</div>
      <div class="panel-body">
        <p>عدد الرسائل المفعلة: {{active_num}}</p>
        <p>عدد الرسائل بإنتظار التفعيل: {{unactive_num}}</p>
        <p>إجمالي عدد الرسائل: {{active_num+unactive_num}}</p>
      </div>
    </div>
  </div>
</div>

<div class="container" style="width:50%;float:right">
  <div class="panel-group">
    <div class="panel panel-default">
      <div class="panel-heading">إحصائيات الموقع</div>
      <div class="panel-body">
      <p>إصدار Python: {{python['version']}}</p>
      <p>اسم الخدوم: {{server['name']}}</p>
      <p>منفذ الخدوم: {{server['port']}}</p>
      <p>إصدار wsgi هو: {{server['wsgi_version']}}</p>
      <p>خادوم wsgi هو: {{server['sofrware']}}</p>
      <p>عنوان ip هو: {{server['address']}}</p>
      <p>نوع قاعدة البيانات: {{db['type']}}</p>
      <p>إصدار قاعدة البيانات: {{db['version']}}
      <p>اسم قاعدة البيانات: <a href="/dbBackup">{{db['name']}}</a></p>
      <p>حجم قاعدة البيانات: {{db['size']}}</p>
      </div>
    </div>
  </div>
</div>
