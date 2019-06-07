
<!DOCTYPE html>
<html>
  <head>
    <title>Sportigo</title>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Baloo+Bhaina|Source+Sans+Pro" rel="stylesheet">
    <script type="text/javascript" src="static/autocompletion.js"></script>
        <script type="text/javascript" src="static/popin.js"></script>
            <script type="text/javascript" src="static/propositions.js"></script>
    <link rel="stylesheet" type="text/css" href="static/css/resultat.css" />
  </head>
  <body>
    <div class="modal">
      <h2>A propos de nous...</h2>
      <p>Ce site a été réalisé dans le cadre du cours de Technologies de production de logiciels par Louis De L'Hommeau et Dimitri Fort.</p>
      <p style="color: rgb(215, 215, 215);font-size: 1.3em;font-weight: bold;">Sportigo - 2017</p>
      <span class="modal_close">Retour</span>
   </div>
   <div class="modalbg"></div>
    <div id="map"></div>
    <div id="cadreRecherche">
      <h1>Sportigo</h1>
      <h2>L'activité à votre portée</h2>

        <h3>Rechercher une activité à pratiquer </h3>
        <form method="post" action="resultat" id="formRecherche">
          <div id="formpart1">
            <input placeholder="Recherchez votre ville..." type="text" name="ville" id="ville"/>
            <input placeholder="Recherchez une activité..." type="text" name="activite" id="activite" />
          </div>
          <div id="formpart2">
            <input id="boutonrRechercher" type="submit" name="envoyer" value="Valider">
          </div>
        </form>
        <div id="footer">
        <a href="http://finda.photo/" target="_blank">Photos</a>
        <a href="http://www.univ-nantes.fr/" target="_blank">Université de Nantes</a>
        <a id="apropos"> A propos</a>


        </div>

        <p id="message"></p>
        <div id="smileyDiv"><p id="smiley"></p></div>
        <p id="listePropositions"></p>
        <p id="conseil"></p>
        <script type="text/javascript">
        $(function() {
          <%
              if coord=="vide" and activite=="vide" :
          %>
          $('#message').html("Veuillez entrer une ville, une activité, ou les deux");
          $('#smiley').html(":)");
          $('#listePropositions').html("");
          $('#conseil').html("");
          <%
              elif coord=="erreur" and activite=="erreur" :
          %>
          $('#message').html("La ville et l'activité que vous avez saisies ne sont pas dans la base de données");
          $('#smiley').html(":(");
          $('#listePropositions').html("");
          $('#conseil').html("conseil : des propositions sont faites lors de la saisie de caractères");
          <%
              elif activite=="erreur" :
          %>
          $("#ville").attr('value', "{{champs[0]}}");
          $('#message').html("L'activité que vous avez saisie n'est pas dans la base de données");
          $('#smiley').html(":(");
          $('#listePropositions').html("Vouliez vous dire : <a href='#' class='propoAct'>{{propositions[0]}}</a>, <a href='#' class='propoAct'>{{propositions[1]}}</a>, <a href='#' class='propoAct'>{{propositions[2]}}</a> ?");
          $('#conseil').html("conseil : des propositions sont faites lors de la saisie de caractères");
          <%
              elif coord=="erreur" :
          %>
          $("#activite").attr('value',"{{champs[1]}}");
          $('#message').html("La ville que vous avez saisie n'est pas dans la base de données");
          $('#smiley').html(":(");
          $('#listePropositions').html("Vouliez vous dire : <a href='#' class='propoVille'>{{propositions[0]}}</a>, <a href='#' class='propoVille'>{{propositions[1]}}</a>, <a href='#' class='propoVille'>{{propositions[2]}}</a> ?");
          $('#conseil').html("conseil : des propositions sont faites lors de la saisie de caractères");
          <%
              else :
          %>
          $('#message').html("{{len(equipements)}} équipement"+({{len(equipements)}}>1 ? "s " : " ")+"correspondant à votre recherche");
          $('#smiley').html("");
          $('#listePropositions').html("");
          $('#conseil').html("");
          <%
              end
          %>
        });
        </script>
    </div>
    <script type="text/javascript">

    var map;
    var myLatLng;
    var myZoom;
    <%
        if len(coord)==2 :
    %>
    myLatLng = {lat: {{coord[1]}}, lng: {{coord[0]}}};
    myZoom = 14;
    <%
        else :
    %>
    myLatLng = {lat: 47.4727, lng: -0.856177};
    myZoom = 9;
    <%
        end
    %>
    var selectedInfoWindow;

    function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: myLatLng,
          zoom: myZoom
        });

        <%
            i = 1
            for eq in equipements :
              listeActivite = ', '.join(map(str, eq[11]))
        %>

        var marker{{i}} = new google.maps.Marker({
          position: {lat:{{eq[1]}}, lng:{{eq[2]}}},
          map: map,
          title: '{{eq[3]}}'
        });
        var contentString{{i}} = '<div id="content">'+
              '<div id="siteNotice">'+
              '</div>'+
              '<a href="https://www.google.fr/search?q={{eq[3]}}+{{eq[9]}}" target="_blank" id="firstHeading" class="firstHeading">{{eq[3]}}</a>'+
              '<div id="bodyContent">'+
              '<p>Activité : {{listeActivite}}</p>'+
              '<p>Nom de l\'équipement : {{eq[10]}}</p>'+
              '<p>Adresse : {{eq[4] if eq[4]!='' else (str(eq[5])+" "+eq[6] if eq[5]!=0 else eq[6])+" ("+eq[9]+")"}}</p>'+
              '<p>Accès handicap moteur : {{"Oui" if eq[7]!=0 else "Non"}}</p>'+
              '<p>Accès handicap sensoriel : {{"Oui" if eq[8]!=0 else "Non"}}</p>'+
              '</div>'+
              '</div>';

          var infoWindow{{i}} = new google.maps.InfoWindow({
            content: contentString{{i}}
          });

          marker{{i}}.addListener('click', function() {
            map.setCenter(marker{{i}}.getPosition());
            map.setZoom(16);
            //Check if there some info window selected and if is opened then close it
            if (selectedInfoWindow != null && selectedInfoWindow.getMap() != null) {
            selectedInfoWindow.close();
              //If the clicked window is the selected window, deselect it and return
              if (selectedInfoWindow == infoWindow{{i}}) {
                selectedInfoWindow = null;
                return;
              }
            }
            //If arrive here, that mean you should open the new info window
            //because is different from the selected
            selectedInfoWindow = infoWindow{{i}};
            selectedInfoWindow.open(map, marker{{i}});
          });

          google.maps.event.addListener(infoWindow{{i}}, 'closeclick', function() {
                map.setZoom(14);
          });
        <%
            i=i+1
          end
        %>

    }



    </script>
    <script async defer
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAFIBBbt-tzIwCg_D0n2g9wYvLfXsPtgjA&callback=initMap">
    </script>
  </body>
</html>
