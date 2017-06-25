<form action="/admin/search" method="POST">
<div class="container">
  <div class="panel-group">
    <div class="panel panel-default">
      <div class="panel-heading">{{result[1] if result else msg_title}}</div>
      <div class="panel-body">
      %if result:
      {{result[2]}}
      %else:
      <input type="text" name="input_search" required />
        <select name="search_type">
          <option value="search_all">حسب العنوان والمحتوى</option>
          <option value="search_bytitle">حسب العنوان</option>
          <option value="search_bybody">حسب المحتوى</option>
        </select><p>
        <input type="radio" name="msgDisplay" id="label_displayAll" value="all" checked="checked"><label for="label_displayAll">عرض جميع الرسائل</label><br>
        <input type="radio" name="msgDisplay" id="label_displayActive" value="active"><label for="label_displayActive">عرض الرسائل المفعلة</label><br>
        <input type="radio" name="msgDisplay" id="label_displayUnActive" value="unactive"><label for="label_displayUnActive">عرض الرسائل بإنتظار الموافقة</label>
        </p>
      <input type="submit" value="بحث" />
      %end
      </div>
    </div>
  </div>
</div>
</form>
