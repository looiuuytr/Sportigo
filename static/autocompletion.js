$(document).ready(function(){

  $("#ville").autocomplete({
      source : function(requete, response){
      $.ajax({
              url : '/autocompletion', // on appelle le script JSON
              type: 'GET',
              dataType : 'json', // on spécifie bien que le type de données est en JSON
              data : 'ville='+$("#ville").val(),
              success: function (data){
              	response($.map(data, function (item){

              		return {
              			label: item.ville,
                    value: item.ville
              		}
              	}));
              }
          });//fin ajax
      }
  });

  $("#activite").autocomplete({
      source : function(requete, response){
      $.ajax({
              url : '/activitesAC', // on appelle le script JSON
              type: 'GET',
              dataType : 'json', // on spécifie bien que le type de données est en JSON
              data : 'activite='+$("#activite").val(),
              success: function (data){
                response($.map(data, function (item){

                  return {
                    label: item.activite,
                    value: item.activite
                  }
                }));
              }
          });//fin ajax
      }
  });
});
