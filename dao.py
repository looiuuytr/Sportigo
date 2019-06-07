import json
import csv
import mysql.connector
import urllib.request
import collections


class DAO:
    def __init__(self):

         self.connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')


    def actCommunelocal(self,commune):
        fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/csv/J334_equipements_activites.csv"
        file = open(fname)
        try :
            commune=str(commune)
        except ValueError:
            print("Veuillez indiquer un nom valide svp")

        try:

            lecteur = csv.reader(file)
            for row in lecteur:
                if row[1]==commune:
                    print(row[1],row[5], row[6])
        finally:
            file.close()



    def majtableActCommunes(self):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()

            fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/csv/J334_equipements_activites.csv"
            #fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/test csv/petit.csv"


            file = open(fname)
            try:
                lecteur = csv.reader(file)
                #lecteur.next()
                for row in lecteur:

                    s = """insert into `ActivitesCommunes` (,`Ville`,`IDEquipement`,`Activite`) values ('"""

                    s+=row[1]+'"'+",'"+row[2]+"',"+'"'+row[5]+'"'+")"

                    cursor.execute(s)
                    connexion.commit()


            finally:

                file.close()


        finally:
            connexion.close()

    def majtableInstallations(self):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()

            fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/csv/23440003400026_J335_installations_table.csv"
            #fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/test csv/petit.csv"


            file = open(fname)
            try:
                lecteur = csv.reader(file)
                #lecteur.next()
                accesHandiMoteurs="0"
                accesHandiSensoriels="0"
                for row in lecteur:
                    if(row[12]=="Oui"):
                        accesHandiMoteurs="1"
                    else:
                        accesHandiMoteurs="0"
                    if(row[13]=="Oui"):
                        accesHandiSensoriels="1"
                    else:
                        accesHandiSensoriels="0"

                    s = """insert into `Installations` (`NomInstallation`,`NumInstallation`, `NomLieuDit`,`NumVoie`,`NomVoie`,`AccesHandiMoteurs`,`AccesHandiSens`) values ("""

                    s+='"'+row[0]+'"'+",'"+row[1]+"',"+'"'+row[5]+'"'+",'"+row[6]+"',"+'"'+row[7]+'"'+",'"+accesHandiMoteurs+"','"+accesHandiSensoriels+"')"
                    #print(s)
                    cursor.execute(s)
                    connexion.commit()


            finally:

                file.close()


        finally:
            connexion.close()

    def majtableEquipement(self):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()

            fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/csv/equipements.csv"
            #fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/test csv/petit.csv"


            file = open(fname)
            try:
                lecteur = csv.reader(file)

                for row in lecteur:

                    s = """insert into `Equipements` (`IDEquipement`,`NomEquipement`, `NumInstallation`,`Longitude`,`Latitude`) values ("""

                    s+="'"+row[4]+"'"+","+'"'+row[5]+'"'+",'"+row[2]+"','"+row[179]+"','"+row[180]+"')"
                    #print(s)
                    cursor.execute(s)
                    connexion.commit()


            finally:

                file.close()


        finally:
            connexion.close()

    def majtableVille(self):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()

            fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/csv/23440003400026_J335_installations_table.csv"
            #fname = "/hometu/etudiants/d/e/E155583M/2ème année/4eme semestre/Technologie production Logiciels/test csv/petit.csv"

            ensemble=set()
            file = open(fname)
            try:
                lecteur = csv.reader(file)

                liste=[]
                for row in lecteur:
                    liste=(row[2],row[3],row[9],row[10])

                    ensemble.add(liste)

            finally:

                file.close()
            for tuple in ensemble:
                s = """insert into `Ville` (`Nom`,`CodeInsee`, `Longitude`,`Latitude`) values ("""

                s+='"'+tuple[0]+'"'+','+tuple[1]+','+tuple[2]+','+tuple[3]+')'
                #print(s)
                cursor.execute(s)
                connexion.commit()


        finally:
            connexion.close()



    def selectIDEquipement(self,commune,sport):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        cursor = connexion.cursor()
        if (commune!=""):
            if (sport!=""):
                try:
                    requete="SELECT IDEquipement FROM `ActivitesCommunes` WHERE NomVille='"+commune+"' and NomActivite='"+sport+"'"
                    cursor.execute(requete)
                    resultat = list()
                    for (IDEquipement) in cursor:
                        resultat.append(IDEquipement[0])
                finally:
                    connexion.close()
                    return (resultat)
            else :
                try:
                    requete="SELECT IDEquipement FROM `ActivitesCommunes` WHERE NomVille='"+commune+"'"
                    cursor.execute(requete)
                    resultat = list()
                    for (IDEquipement) in cursor:
                        resultat.append(IDEquipement[0])
                finally:
                    connexion.close()
                    return (resultat)
        else:
            if (sport!=""):
                try:
                    requete="SELECT IDEquipement FROM `ActivitesCommunes` WHERE NomActivite='"+sport+"'"
                    cursor.execute(requete)
                    resultat = list()
                    for (IDEquipement) in cursor:
                        resultat.append(IDEquipement[0])
                finally:
                    connexion.close()
                    return resultat


    def selectCoordonnees(self,idsEquipements):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()
            requete="SELECT longitude, latitude FROM `Equipements` WHERE IDEquipement in ("+','.join(map(str, idsEquipements)) + ')'
            cursor.execute(requete)
            coord = list()

            for (coordonnee) in cursor:
                l = list()
                l.append(coordonnee[0])
                l.append(coordonnee[1])
                coord.append(l)

        finally:
            connexion.close()
            return coord

    def selectDetailsIds(self,idsEquipements):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        listDetails = list()
        listetmp = list()
        listact = list()
        try:
            cursor = connexion.cursor()
            requete="""SELECT e.IDEquipement, e.latitude, e.longitude, i.NomInstallation, i.NomLieuDit, i.NumVoie, i.NomVoie, i.AccesHandiMoteurs, i.AccesHandiSens, a.NomVille, e.NomEquipement, a.NomActivite FROM Equipements e, Installations i, ActivitesCommunes a WHERE e.IDEquipement in ("""+','.join(map(str, idsEquipements)) +""") AND i.NumInstallation=e.NumInstallation AND e.IDEquipement=a.IDEquipement"""

            cursor.execute(requete)
            curseur =cursor.fetchall()
            idEqu = curseur[0][0]
            for j in range(len(curseur[0])-1):
                listetmp.append(curseur[0][j])
            listact.append(curseur[0][len(curseur[0])-1])
            for tuple in curseur:

                if (tuple[0]==idEqu):
                    listact.append(tuple[len(tuple)-1])

                else:
                    listetmp.append(listact)
                    listDetails.append(listetmp)
                    listetmp=[]
                    for h in range(len(tuple)-1):
                        listetmp.append(tuple[h])
                    idEqu = tuple[0]
                    listact=[tuple[len(tuple)-1]]
            listetmp.append(listact)
            listDetails.append(listetmp)
        finally:
            connexion.close()
            return listDetails

    def selectDetails(self,longitude,latitude):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()
            requete="""SELECT i.NomInstallation, i.NomLieuDit, i.NumVoie, i.NomVoie,
    i.AccesHandiMoteurs, i.AccesHandiSens, a.NomVille, e.NomEquipement,
    a.NomActivite
    FROM Equipements e, Installations i, ActivitesCommunes a WHERE
    CAST(e.Longitude AS DECIMAL(6,5)) = CAST("""+longitude+""" AS DECIMAL(6,5)) AND
    CAST(e.Latitude AS DECIMAL(6,5)) = CAST("""+latitude+"""AS DECIMAL(6,5)) AND
    i.NumInstallation=e.NumInstallation AND e.IDEquipement=a.IDEquipement"""
            cursor.execute(requete)
            listDetails = list()
            for (ligneDetail) in cursor:
                for i in range(len(ligneDetail)):
                    listDetails.append(ligneDetail[i])

        finally:
            connexion.close()
            return listDetails

    def autocompletion(self,chaine):
        res = "["
        if(len(chaine)>2):

            connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
            try:

                cursor = connexion.cursor()
                requete="""SELECT Nom,CodeInsee FROM `Ville` WHERE Nom LIKE '"""+chaine+"""%'or CodeInsee LIKE '"""+chaine+"%' limit 10"
                cursor.execute(requete)





                for ligne in cursor:
                    res+=('{"ville":"'+ligne[0]+'"},')

            finally:
                if (len(res)==1):
                    return res+"]"
                res = res[0:-1]
                connexion.close()
                res+="]"
                return res
        else:
            return ("")

    def selectCoordonneesVille(self, nomVille):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()
            requete="SELECT longitude, latitude FROM `Ville` WHERE Nom='"+nomVille+"'"
            cursor.execute(requete)
            curseur = cursor.fetchone()
        finally:
            connexion.close()
            if type(curseur)==tuple :
                return curseur
            else :
                return "erreur"

    def activiteExiste(self, activite) :
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()
            requete="SELECT CASE WHEN EXISTS (SELECT * FROM `ActivitesCommunes` WHERE NomActivite='"+activite+"') THEN True ELSE False END"
            cursor.execute(requete)
            curseur = cursor.fetchone()
        finally:
            connexion.close()
            if curseur[0]==1 :
                return "Ok"
            else :
                return "erreur"


    def activitesAC(self,activite):
        res = "["
        if(len(activite)>2):

            connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')

            try:

                cursor = connexion.cursor()
                requete="""SELECT DISTINCT NomActivite FROM `ActivitesCommunes` WHERE 1 and NomActivite like '"""+activite+"""%' limit 10 """
                cursor.execute(requete)





                for ligne in cursor:
                    res+=('{"activite":"'+ligne[0]+'"},')

            finally:
                if (len(res)==1):
                    return res+"]"
                res = res[0:-1]
                connexion.close()
                res+="]"
                return res
        else:
            return ("")

    def selectAllVilles(self):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()
            requete="SELECT nom FROM `Ville` WHERE 1"
            cursor.execute(requete)
            curseur=list()
            for (tuple) in cursor:
                curseur.append(tuple[0])

        finally:
            connexion.close()
            return curseur

    def selectAllActivites(self):
        connexion = mysql.connector.connect(user='E155438E', password='E155438E',host='infoweb',database='E155438E')
        try:
            cursor = connexion.cursor()
            requete="SELECT DISTINCT nomActivite FROM `ActivitesCommunes` WHERE 1"
            cursor.execute(requete)
            curseur=list()
            for (tuple) in cursor:
                curseur.append(tuple[0])

        finally:
            connexion.close()
            return curseur

    def levenshtein(self,s1, s2):
        if len(s1) < len(s2):
            return DAO.levenshtein(self, s2, s1)

        # len(s1) >= len(s2)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
                deletions = current_row[j] + 1       # than s2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def propositionsVille(self,chaine):
        propositions={}
        listeVilles = self.selectAllVilles()
        i=0
        for ville in listeVilles:
            score=DAO.levenshtein(self, ville,chaine)
            propositions[score,i]=ville
            i+=1

        i=1
        resultat=list()
        propositions=collections.OrderedDict(sorted(propositions.items()))
        for cle,ville in propositions.items():
           resultat.append(ville)
           if (i>=3):
               break
           i+=1
        return resultat

    def propositionsActivite(self,chaine):
        propositions={}
        listeActivites = self.selectAllActivites()
        i=0
        for activite in listeActivites:
            score=DAO.levenshtein(self, activite,chaine)
            propositions[score,i]=activite
            i+=1

        i=1
        resultat=list()
        propositions=collections.OrderedDict(sorted(propositions.items()))
        for cle,activite in propositions.items():
           resultat.append(activite)
           if (i>=3):
               break
           i+=1
        return resultat


    def downloadFile(self):
        url = 'http://data.paysdelaloire.fr/fileadmin/data/datastore/pdl/PLUS15000/J334_equipements_activites.csv'
        urllib.request.urlretrieve(url, "/tmp/test.csv")
