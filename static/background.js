$(document).ready(function(){
  var images = ['football.jpeg','lutte.jpeg','moto.jpeg','muscu.jpeg','skate.jpeg','velo.jpeg'];


  $('body').css({'background-image': 'url(static/images/' + images[Math.floor(Math.random() * images.length)] + ')'});


});
