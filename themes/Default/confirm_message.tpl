<div class="container">
  <form action="{{action}}" method="post">
  
    <div class="panel-group">
      <div class="panel panel-default">
    
        <div class="panel-heading"><input type="hidden" name="_hidden" value="1">{{msg_title}}</div>
        <div class="panel-body">{{msg_body}}</div>

        <div class="container" style="background-color:#f1f1f1"><button type="submit" class="cancelbtn">{{txt_do}}</button>  <button type="button" onclick="return location.href=document.referrer;" class="cancelbtn">إلغاء اﻷمر</button></div>

      </div>

    </div>

  </form>
  
</div>
