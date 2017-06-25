<div class="container">
  <div class="panel-group">
    <div class="panel panel-default">
      <div class="panel-heading">{{msg_title}}
      %if msgid:
      <span style="float: left;">
  <ul class="breadcrumb2">
    <li><a href="/admin/delete/{{msgid}}">[حذف]</a></li>
    <li><a href="/admin/active/{{msgid}}">[تفعيل]</a></li>
  </ul>
</span>
%end
      </div>
      <div class="panel-body">{{msg_body}}</div>
    </div>
  </div>
</div>
