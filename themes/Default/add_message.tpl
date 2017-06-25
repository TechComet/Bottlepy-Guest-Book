<form action="/add" method="POST">
<div class="container">
  <div class="panel-group">
    <div class="panel panel-default">
      <div class="panel-heading">إضافة رسالة لسجل الزوار</div>
      <div class="panel-body">
      <label for="utitle">عنوان الرسالة:</label> <input type="text" id="utitle" name="utitle" required /><br><br>
      <p><label for="ubody">الرسالة:</label></p><p><textarea name="ubody" id="ubody" cols="60" rows="10" required></textarea></p>
      <input type="hidden" name="doAdd" value="1" />
      <input type="submit" value="إضافة" />
      <input type="reset" value="تفريغ" />
      </div>
    </div>
  </div>
</div>
</form>
