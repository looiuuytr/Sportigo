$(document).ready(function(){
  $(document).on("click", ".propoAct", function() {
    var texte = $(this).text();
    $("#activite").attr('value',texte);
  });
  $(document).on("click", ".propoVille", function() {
    var texte = $(this).text();
    $("#ville").attr('value',texte);
  });
});
