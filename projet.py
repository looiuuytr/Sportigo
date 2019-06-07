#! /usr/bin/python
import cgi
import sys
path = "E:/IUT BACKUP/2ème année/4eme semestre/Technologie production Logiciels/Sportigo"
#path = "/hometu/etudiants/d/e/E155438E/workspace/semestre_4/techProdLogiciel/Sportigo"
sys.path.append(path)
from dao import *
from bottle import *

@route('/')
def myIndex() :
    return template('index.html')

@route('/resultat', method='POST')
def resultat() :
    dao = DAO()
    ville = request.forms.getunicode("ville")
    activiteR = request.forms.getunicode("activite")
    coord="vide"
    activiteChamp="vide"
    if ville!="" :
        coord = dao.selectCoordonneesVille(ville)
    if activiteR!="" :
        activiteChamp = dao.activiteExiste(activiteR)
    levenshtein = ""
    if coord=="erreur" and activiteChamp!="erreur" :
        levenshtein = dao.propositionsVille(ville)
    elif coord!="erreur" and activiteChamp=="erreur" :
        levenshtein = dao.propositionsActivite(activiteR)
    equipement = dao.selectDetailsIds(dao.selectIDEquipement(ville, activiteR))
    infos = list()
    infos.append(ville)
    infos.append(activiteR)
    return template('mapResult.tpl', equipements=equipement, coord=coord, activite=activiteChamp, propositions=levenshtein, champs=infos)


@route('/autocompletion')
def autocompletion():
    dao = DAO()
    ville = request.query.ville
    return dao.autocompletion(ville)

@route('/activitesAC')
def activitesAC():
    dao = DAO()
    activite = request.query.activite
    return dao.activitesAC(activite)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0", port=8002)
# AIzaSyAFIBBbt-tzIwCg_D0n2g9wYvLfXsPtgjA
# http://stackoverflow.com/questions/6877806/can-i-use-javascript-with-bottle-framework
