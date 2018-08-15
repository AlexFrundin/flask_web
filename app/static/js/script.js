
<script src="{{url_for('.static', filename='js/script.js')}}" charset="utf-8"></script>


$('.close').click(function(){
    $(this).parent('.close').alert('close');
});



var id_ = {{id_|tojson}};
$(function(){
  id_.forEach(function(item, i, id_){
      item = "#"+item;
      console.log(item);
       window.setTimeout(function(){
       $(item).alert('close');
     },(i*500)+2000);
    });
});



$(document).ready(function(){

})
