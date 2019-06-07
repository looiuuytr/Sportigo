$(document).ready(function(){

  $('#apropos').click(function() {

    $( ".modal" ).css( "display", "block" );
    $( ".modalbg" ).css( "display", "block" );


  });
  $('.modal_close').click(function(){
    $( ".modal" ).css( "display", "none" );
        $( ".modalbg" ).css( "display", "none" );
  })

});
