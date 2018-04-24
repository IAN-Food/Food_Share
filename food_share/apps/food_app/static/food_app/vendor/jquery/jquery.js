


$( document ).ready(function() {
    console.log( "ready!" );

    $('#id01').hide();
    $('#id02').hide();
    $('#id03').hide();


  	$("button#login_reg").click(function(){
      $(this).hide();
      $('#id01').show();
    });
 

    $("button#log_close").click(function(){
      $("button#login_reg").show();
      $('#id01').hide();
      $('#id02').hide();
    });

    $("a#reg_link").click(function(){
      $("button#login_reg").show();
      alert("things");
      $('#id02').show();
      $('#id01').hide();
     
    });

    $("button#reg_close").click(function(){
      $("button#login_reg").show();
      $('#id02').hide();
      $('#id01').hide();
    });

    $("#reg_btn").click(function(){



    });

});	





