class Employe:
    def __init__(self, numero_permis, nom, prenom):
        self.numero_permis = numero_permis
        self.nom = nom
        self.prenom = prenom
        self.voiture_service = None

    def afficher_info(self):
        print(f"Employé : {self.nom} {self.prenom} - Permis : {self.numero_permis}")
        if self.voiture_service:
            print(f"Voiture de service : {self.voiture_service.marque} ({self.voiture_service.matricule})")
        else:
            print("Aucune voiture de service")

    def affecter_voiture(self, voiture):
        if self.voiture_service:
            print(f"Erreur : {self.nom} a déjà une voiture.")
            return
        if voiture.chauffeur:
            print(f"Erreur : la voiture {voiture.matricule} est déjà attribuée à {voiture.chauffeur.nom}.")
            return
        self.voiture_service = voiture
        voiture.chauffeur = self
        print(f"{self.nom} reçoit la voiture {voiture.matricule}.")

    def retirer_voiture(self):
        if not self.voiture_service:
            print(f"{self.nom} n’a pas de voiture à retirer.")
            return
        print(f"{self.nom} a rendu la voiture {self.voiture_service.matricule}.")
        self.voiture_service.chauffeur = None
        self.voiture_service = None
class Voiture:
    def __init__(self, matricule, annee, kilometrage, marque):
        self.matricule = matricule
        self.annee = annee
        self.kilometrage = kilometrage
        self.marque = marque
        self.chauffeur = None

    def afficher_info(self):
        print(f"Voiture : {self.marque} ({self.matricule}) - Année : {self.annee}, Km : {self.kilometrage}")
        if self.chauffeur:
            print(f"Attribuée à : {self.chauffeur.nom} {self.chauffeur.prenom}")
        else:
            print("Aucun chauffeur")
e1= Employe("265", "Zoubir", "jshg")
e2= Employe("P002", "Tahar", "ravah")
e3= Employe("P003", "Mohand", "MERIEM")
v1= Voiture("A54dd", 2012, 128000, "Camaro")
v2= Voiture("Bfhr52", 1998, 218000, "Maruti")
v3= Voiture("Cf562e", 2021, 35000, "BMW")

e1.afficher_info()
e2.afficher_info()
e3.afficher_info()
v1.afficher_info()
v2.afficher_info()
v3.afficher_info()

e1.affecter_voiture(v2)
e2.affecter_voiture(v3)
e1.afficher_info()
e2.afficher_info()
v1.afficher_info()
v2.afficher_info()
e1.retirer_voiture()
e1.afficher_info()
v1.afficher_info()

e2.affecter_voiture(v3)

