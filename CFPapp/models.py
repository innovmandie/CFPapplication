from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import CFPapp
from CFPapp.models import User
import uuid
from django.core.validators import validate_slug


from django_currentuser.db.models import CurrentUserField
from django.core.validators import MinValueValidator, MaxValueValidator

class Villes(models.Model):
    nom= models.CharField(max_length=255)

    def __str__(self):
        return self.nom

codepostal_CHOICES=(
    ("76600","76600"),
("76000","76000"),
("14000","14000"),
("50100","50100"),
("27000","27000"),
("76200","76200"),
("76300","76300"),
("76800","76800"),
("61000","61000"),
("76120","76120"),
("27200","27200"),
("76140","76140"),
("14200","14200"),
("14100","14100"),
("50000","50000"),
("76130","76130"),
("76400","76400"),
("27400","27400"),
("14500","14500"),
("76500","76500"),
("76290","76290"),
("61100","61100"),
("76380","76380"),
("61200","61200"),
("14400","14400"),
("27100","27100"),
("76230","76230"),
("50400","50400"),
("76360","76360"),
("76190","76190"),
("27140","27140"),
("50440","50440"),
("76210","76210"),
("14123","14123"),
("76350","76350"),
("76150","76150"),
("76320","76320"),
("27300","27300"),
("76250","76250"),
("14140","14140"),
("76530","76530"),
("76170","76170"),
("14120","14120"),
("76160","76160"),
("76370","76370"),
("76700","76700"),
("14150","14150"),
("27500","27500"),
("76170","76170"),
("14260","14260"),
("76650","76650"),
("50200","50200"),
("76700","76700"),
("76320","76320"),
("14700","14700"),
("76420","76420"),
("76410","76410"),
("27130","27130"),
("27700","27700"),
("61300","61300"),
("76240","76240"),
("50480","50480"),
("14140","14140"),
("50300","50300"),
("14600","14600"),
("76310","76310"),
("76960","76960"),
("76260","76260"),
("27600","27600"),
("14110","14110"),
("50700","50700"),
("14460","14460"),
("76240","76240"),
("14140","14140"),
("76570","76570"),
("76220","76220"),
("76520","76520"),
("50600","50600"),
("27420","27420"),
("14350","14350"),
("50260","50260"),
("76770","76770"),
("76930","76930"),
("14160","14160"),
("27180","27180"),
("14550","14550"),
("14210","14210"),
("61410","61410"),
("27600","27600"),
("14670","14670"),
("14440","14440"),
("76580","76580"),
("27120","27120"),
("76410","76410"),
("50240","50240"),
("27190","27190"),
("14730","14730"),
("61800","61800"),
("76470","76470"),
("76710","76710"),
("14123","14123"),
("14123","14123"),
("14260","14260"),
("76270","76270"),
("27270","27270"),
("14360","14360"),
("27950","27950"),
("27160","27160"),
("27210","27210"),
("14130","14130"),
("27160","27160"),
("14380","14380"),
("50170","50170"),
("50160","50160"),
("27800","27800"),
("61700","61700"),
("61100","61100"),
("76480","76480"),
("61500","61500"),
("76460","76460"),
("27340","27340"),
("76490","76490"),
("14470","14470"),
("27110","27110"),
("76770","76770"),
("50420","50420"),
("76640","76640"),
("76430","76430"),
("50180","50180"),
("50380","50380"),
("50250","50250"),
("27220","27220"),
("61400","61400"),
("27930","27930"),
("50800","50800"),
("27150","27150"),
("76440","76440"),
("61000","61000"),
("14760","14760"),
("61160","61160"),
("14800","14800"),
("61130","61130"),
("27520","27520"),
("27100","27100"),
("14800","14800"),
("14370","14370"),
("14220","14220"),
("14230","14230"),
("76510","76510"),
("14390","14390"),

)

communes_CHOICES =(
    ("Le Havre ","Le Havre "),
("Rouen ","Rouen "),
("Caen ","Caen "),
("Cherbourg-en-Cotentin ","Cherbourg-en-Cotentin "),
("Évreux ","Évreux "),
("Dieppe ","Dieppe "),
("Sotteville-lès-Rouen ","Sotteville-lès-Rouen "),
("Saint-Étienne-du-Rouvray ","Saint-Étienne-du-Rouvray "),
("Alençon ","Alençon "),
("Le Grand-Quevilly ","Le Grand-Quevilly "),
("Vernon ","Vernon "),
("Le Petit-Quevilly ","Le Petit-Quevilly "),
("Hérouville-Saint-Clair ","Hérouville-Saint-Clair "),
("Lisieux ","Lisieux "),
("Saint-Lô ","Saint-Lô "),
("Mont-Saint-Aignan ","Mont-Saint-Aignan "),
("Fécamp ","Fécamp "),
("Louviers ","Louviers "),
("Vire Normandie ","Vire Normandie "),
("Elbeuf ","Elbeuf "),
("Montivilliers ","Montivilliers "),
("Flers ","Flers "),
("Canteleu ","Canteleu "),
("Argentan ","Argentan "),
("Bayeux ","Bayeux "),
("Val-de-Reuil ","Val-de-Reuil "),
("Bois-Guillaume ","Bois-Guillaume "),
("Granville ","Granville "),
("Barentin ","Barentin "),
("Yvetot ","Yvetot "),
("Gisors ","Gisors "),
("La Hague ","La Hague "),
("Bolbec ","Bolbec "),
("Ifs ","Ifs "),
("Oissel ","Oissel "),
("Maromme ","Maromme "),
("Caudebec-lès-Elbeuf ","Caudebec-lès-Elbeuf "),
("Bernay ","Bernay "),
("Déville-lès-Rouen ","Déville-lès-Rouen "),
("Mézidon Vallée d'Auge ","Mézidon Vallée d'Auge "),
("Grand-Couronne ","Grand-Couronne "),
("Port-Jérôme-sur-Seine ","Port-Jérôme-sur-Seine "),
("Mondeville ","Mondeville "),
("Darnétal ","Darnétal "),
("Petit-Caux ","Petit-Caux "),
("Gonfreville-l'Orcher ","Gonfreville-l'Orcher "),
("Ouistreham ","Ouistreham "),
("Pont-Audemer ","Pont-Audemer "),
("Lillebonne ","Lillebonne "),
("Souleuvre en Bocage ","Souleuvre en Bocage "),
("Petit-Couronne ","Petit-Couronne "),
("Coutances ","Coutances "),
("Harfleur ","Harfleur "),
("Saint-Pierre-lès-Elbeuf ","Saint-Pierre-lès-Elbeuf "),
("Falaise ","Falaise "),
("Bihorel ","Bihorel "),
("Saint-Aubin-lès-Elbeuf ","Saint-Aubin-lès-Elbeuf "),
("Verneuil d'Avre et d'Iton ","Verneuil d'Avre et d'Iton "),
("Les Andelys ","Les Andelys "),
("L'Aigle ","L'Aigle "),
("Le Mesnil-Esnard ","Le Mesnil-Esnard "),
("Carentan-les-Marais ","Carentan-les-Marais "),
("Saint-Pierre-en-Auge ","Saint-Pierre-en-Auge "),
("Avranches ","Avranches "),
("Honfleur ","Honfleur "),
("Sainte-Adresse ","Sainte-Adresse "),
("Notre-Dame-de-Bondeville ","Notre-Dame-de-Bondeville "),
("Eu ","Eu "),
("Gaillon ","Gaillon "),
("Condé-en-Normandie ","Condé-en-Normandie "),
("Valognes ","Valognes "),
("Colombelles ","Colombelles "),
("Bonsecours ","Bonsecours "),
("Livarot-Pays-d'Auge ","Livarot-Pays-d'Auge "),
("Pavilly ","Pavilly "),
("Gournay-en-Bray ","Gournay-en-Bray "),
("Franqueville-Saint-Pierre ","Franqueville-Saint-Pierre "),
("Saint-Hilaire-du-Harcouët ","Saint-Hilaire-du-Harcouët "),
("Vexin-sur-Epte ","Vexin-sur-Epte "),
("Valdallière ","Valdallière "),
("Bricquebec-en-Cotentin ","Bricquebec-en-Cotentin "),
("Malaunay ","Malaunay "),
("Octeville-sur-Mer ","Octeville-sur-Mer "),
("Dives-sur-Mer ","Dives-sur-Mer "),
("Saint-Sébastien-de-Morsent ","Saint-Sébastien-de-Morsent "),
("Blainville-sur-Orne ","Blainville-sur-Orne "),
("Thue et Mue ","Thue et Mue "),
("La Ferté Macé ","La Ferté Macé "),
("Le Val d'Hazey ","Le Val d'Hazey "),
("Troarn ","Troarn "),
("Douvres-la-Délivrande ","Douvres-la-Délivrande "),
("Le Trait ","Le Trait "),
("Pacy-sur-Eure ","Pacy-sur-Eure "),
("Cléon ","Cléon "),
("Saint-James ","Saint-James "),
("Conches-en-Ouche ","Conches-en-Ouche "),
("Giberville ","Giberville "),
("Tinchebray-Bocage ","Tinchebray-Bocage "),
("Le Tréport ","Le Tréport "),
("Montville ","Montville "),
("Cormelles-le-Royal ","Cormelles-le-Royal "),
("Fleury-sur-Orne ","Fleury-sur-Orne "),
("Les Monts d'Aunay ","Les Monts d'Aunay "),
("Neufchâtel-en-Bray ","Neufchâtel-en-Bray "),
("Mesnil-en-Ouche ","Mesnil-en-Ouche "),
("Trouville-sur-Mer ","Trouville-sur-Mer "),
("Saint-Marcel ","Saint-Marcel "),
("Breteuil ","Breteuil "),
("Beuzeville ","Beuzeville "),
("Pont-l'Évêque ","Pont-l'Évêque "),
("Mesnils-sur-Iton ","Mesnils-sur-Iton "),
("Noues de Sienne ","Noues de Sienne "),
("Pontorson ","Pontorson "),
("Torigny-les-Villes ","Torigny-les-Villes "),
("Brionne ","Brionne "),
("Domfront en Poiraie ","Domfront en Poiraie "),
("Athis-Val de Rouvre ","Athis-Val de Rouvre "),
("Duclair ","Duclair "),
("Sées ","Sées "),
("Saint-Valery-en-Caux ","Saint-Valery-en-Caux "),
("Pont-de-l'Arche ","Pont-de-l'Arche "),
("Rives-en-Seine ","Rives-en-Seine "),
("Courseulles-sur-Mer ","Courseulles-sur-Mer "),
("Le Neubourg ","Le Neubourg "),
("Le Houlme ","Le Houlme "),
("Condé-sur-Vire ","Condé-sur-Vire "),
("Terres-de-Caux ","Terres-de-Caux "),
("Saint-Romain-de-Colbosc ","Saint-Romain-de-Colbosc "),
("Agneaux ","Agneaux "),
("Saint-Pair-sur-Mer ","Saint-Pair-sur-Mer "),
("La Haye ","La Haye "),
("Saint-André-de-l'Eure ","Saint-André-de-l'Eure "),
("Mortagne-au-Perche ","Mortagne-au-Perche "),
("Gravigny ","Gravigny "),
("Villedieu-les-Poêles-Rouffigny ","Villedieu-les-Poêles-Rouffigny "),
("Étrépagny ","Étrépagny "),
("Forges-les-Eaux ","Forges-les-Eaux "),
("Saint-Germain-du-Corbéis ","Saint-Germain-du-Corbéis "),
("Bretteville-sur-Odon ","Bretteville-sur-Odon "),
("Gouffern en Auge ","Gouffern en Auge "),
("Touques ","Touques "),
("Val-au-Perche ","Val-au-Perche "),
("Grand Bourgtheroulde ","Grand Bourgtheroulde "),
("Le Vaudreuil ","Le Vaudreuil "),
("Deauville ","Deauville "),
("Argences ","Argences "),
("Thury-Harcourt-le-Hom ","Thury-Harcourt-le-Hom "),
("Isigny-sur-Mer ","Isigny-sur-Mer "),
("Saint-Nicolas-d'Aliermont ","Saint-Nicolas-d'Aliermont "),
("Cabourg ","Cabourg "),

)

class Utilisateur_infos(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    #id_utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_by = CurrentUserField()
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    anciennete = models.IntegerField(default = 0)
    GRM = "GRM"
    GPN = "GPN"
    GCN = "GCN"
    DDAT = "DDAT"
    DRFPIC = "DRFPIC"
    IFPRA = "IFPRA"
    Greta_CHOICES =(
        (GRM, "CFP au Greta Rouen Maritime"),
        (GPN, "CFP au Greta Portes Normandes"),
        (GCN, "CFP au Greta Côtes Normandes"),
        (DDAT, "DDAT"),
        (DRFPIC, "CFP DRFPIC"),
        (IFPRA, "CFP IFPRA"),
    )
    fonction= models.CharField(max_length=20, choices = Greta_CHOICES, default = GRM)
class User_infos(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_by = CurrentUserField()
    anciennete_annee = models.IntegerField()
    anciennete_mois = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(12)])
    GRM = "GRM"
    GPN = "GPN"
    GCN = "GCN"
    DDAT = "DDAT"
    DRFPIC = "DRFPIC"
    IFPRA = "IFPRA"
    Greta_CHOICES =(
        ('', 'Choisir votre fonction actuelle '),
        (GRM, "CFP au Greta Rouen Maritime"),
        (GPN, "CFP au Greta Portes Normandes"),
        (GCN, "CFP au Greta Côtes Normandes"),
        (DDAT, "DDAT"),
        (DRFPIC, "CFP DRFPIC"),
        (IFPRA, "CFP IFPRA"),
    )
    fonction= models.CharField(max_length=20, choices = Greta_CHOICES)
class CFP_infos(models.Model):
    created_by = CurrentUserField()
    anciennete_annee = models.IntegerField()
    anciennete_mois = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(12)])
    GRM = "GRM"
    GPN = "GPN"
    GCN = "GCN"
    DDAT = "DDAT"
    DRFPIC = "DRFPIC"
    IFPRA = "IFPRA"
    Greta_CHOICES =(
        ('', 'Choisir votre fonction actuelle '),
        (GRM, "CFP au Greta Rouen Maritime"),
        (GPN, "CFP au Greta Portes Normandes"),
        (GCN, "CFP au Greta Côtes Normandes"),
        (DDAT, "DDAT"),
        (DRFPIC, "CFP DRFPIC"),
        (IFPRA, "CFP IFPRA"),
    )
    fonction= models.CharField(max_length=20, choices = Greta_CHOICES)


class Post(models.Model):
    #CFP_id= models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    #id_utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="1")
    created_by = CurrentUserField()



    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A1_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais mon environnement proche de travail"),
        (Degre_2, "Degré 2 Je participe aux instances chargées de définir la stratégie de veille. "),
        (Degre_3, "Degré 3 Je suis force de proposition pour mettre en place une stratégie de veille au service du développement de ma structure"),
        (Degre_4, "Degré 4 Je contribue à l’organisation du système de veille dans les phases de collecte, traitement et diffusion."),
        (N_S_P, "Ne se prononce pas"),
    )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A1_C2_CHOICES =(
        (Degre_1, "Degré 1 J’évalue la fiabilité d’une source, crédibilité et réputation."),
        (Degre_2, "Degré 2 Je sélectionne les sources les plus pertinentes au regard de mes missions et de la stratégie de ma structure"),
        (Degre_3, "Degré 3 J’évalue la complétude de ma veille. Pour compléter ma veille j’identifie de nouveaux acteurs."),
        (Degre_4, "Degré 4 Je conseille les décideurs sur la recherche de prestataires et d’outils performants de veille."),
        (N_S_P, "Ne se prononce pas"),
    )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A1_C3_CHOICES =(
        (Degre_1, "Degré 1 Je consulte les outils et les acteurs ressources au regard de mes besoins et de mes missions."),
        (Degre_2, "Degré 2 Je recherche l’information utile dans le système d’informations."),
        (Degre_3, "Degré 3 Je contextualise les données recensées en fonction de l’organisation de mon environnement"),
        (Degre_4, "Degré 4 J’analyse la diversité des informations recueillies afin de comprendre les transformations"),
        (N_S_P, "Ne se prononce pas"),
    )



    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A2_C1_CHOICES =(
        (Degre_1, "Degré 1 Je mets en œuvre la démarche de diagnostic lors de mon année probatoire"),
        (Degre_2, "Degré 2 Je repère les enjeux, attentes et besoins du commanditaire."),
        (Degre_3, "Degré 3 J’organise ma démarche de diagnostic : identification des acteurs clés, choix des outils d’investigations"),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner mes pairs sur la structuration et la démarche de diagnostic"),
        (N_S_P, "Ne se prononce pas"),

    )
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A2_C2_CHOICES =(
        (Degre_1, "Degré 1 Je sélectionne et je fais apparaitre les données de mon territoire ou de mes secteurs d’activités"),
        (Degre_2, "Degré 2 Je contextualise les données à l’échelle de la problématique."),
        (Degre_3, "Degré 3 J’extraie et j’exploite les données pertinentes afin d’identifier les besoins en compétences."),
         (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner un collectif de travail pour produire des analyses concertées."),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A2_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les différents types de note et je connais la structure d’une note ou d’un document d’analyse."),
        (Degre_2, "Degré 2 Je repère les éléments de mon diagnostic à intégrer dans une note d’opportunité ou une note d’analyse en vue de partager les résultats."),
        (Degre_3, "Degré 3 Je produis régulièrement des notes et des documents d’analyse en toute autonomie."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner des pairs à la production de notes et de documents d’analyse."),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A3_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais le positionnement de mon organisation dans l’écosystème de la formation professionnelle"),
        (Degre_2, "Degré 2 Je sais positionner mon organisation dans le cadre réglementaire, législatif et sur le marché de la formation professionnelle."),
        (Degre_3, "Degré 3 Je m’approprie les analyses existantes (diagnostics, notes d’opportunité, plan de développement, …)."),
        (Degre_4, "Degré 4 Je suis un acteur ressource du réseau en capacité de former mes pairs sur la méthodologie d’analyse de marchés."),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A3_C2_CHOICES =(
        (Degre_1, "Degré 1 Je m’informe des résultats, des diagnostics, des enquêtes réalisés et des analyses produites."),
        (Degre_2, " Degré 2J’identifie les potentiels de développement à court, moyen et long terme à partir du diagnostic précis."),
        (Degre_3, "Degré 3 Je propose des axes de développement concrets (moyens et ressources à mobiliser, points de vigilances)."),
        (Degre_4, "Degré 4 Je capitalise et je mutualise les analyses réalisées pour ma structure, le réseau académique."),
        (N_S_P, "Ne se prononce pas"),
        )


    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A3_C3_CHOICES =(
        (Degre_1, "Degré 1 Je prends connaissance des comptes-rendus des différentes instances."),
        (Degre_2, "Degré 2 Je participe aux instances de concertation en apportant des éléments d’analyse à soumettre au collectif."),
        (Degre_3, "Degré 3 Je contribue à l’ordre du jour des instances de concertation."),
        (Degre_4, "Degré 4 Dans les instances de concertation à l’interne, je suis consulté sur des orientations précises"),
        (N_S_P, "Ne se prononce pas")
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A4_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les décideurs (à partir des organigrammes de l’organisation académique et de ma structure)"),
        (Degre_2, "Degré 2 J’identifie le décideur concerné au regard de la situation requérant un conseil."),
        (Degre_3, "Degré 3 Je m’empare du besoin de conseil, en caractérisant le périmètre, le degré d’urgence et l’impact"),
        (Degre_4, "Degré 4 J’anticipe des situations qui pourraient être sensibles et impactantes pour le développement de ma structure"),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A4_C2_CHOICES =(
        (Degre_1, "Degré 1 Je connais des méthodes et des outils d’analyse (grille MOFF, diagramme causes effets, brainstorming, etc.)."),
        (Degre_2, "Degré 2 J’utilise une méthode et les outils d’analyse nécessaires à la bonne compréhension de la situation"),
        (Degre_3, "Degré 3  A partir de mon analyse de la situation ou de la demande, j’envisage les pistes de réponses possibles."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau pour accompagner mes pairs sur les méthodes et les outils d’analys"),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A4_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les outils de communication adaptés au conseil "),
        (Degre_2, "Degré 2 Je choisis les outils de communication adaptés aux décideurs."),
        (Degre_3, "Degré 3 Je propose à l’écrit ou à l’oral un contenu synthétique pour être lu ou entendu par les décideurs."),
        (Degre_4, "Degré 4 A la demande des décideurs, je rédige et je présente un rapport circonstancié"),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A5_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les différentes instances de mon territoire, leurs rôles et leur fonctionnement."),
        (Degre_2, "Degré 2 Je participe aux échanges, aux réunions et aux groupes de travail du territoire."),
        (Degre_3, "Degré 3 J’adapte ma posture et mes propos en fonction de mes interlocuteurs et des instances auxquelles je participe"),
        (Degre_4, "Degré 4 Je suis sollicité en qualité d’expert de la formation professionnelle"),
        (N_S_P, "Ne se prononce pas"),
        )


    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A5_C2_CHOICES =(
        (Degre_1, "Degré 1 Je distingue les 3 voies de formation professionnelle. Je m’informe en interne sur les missions, l’offre et les moyens des structures"),
        (Degre_2, "Degré 2 J’identifie sur mon territoire l’offre de formation en m’aidant de la carte des formations professionnelles de l’éducation nationale"),
        (Degre_3, "Degré 3 J’explique la mission de service public de l’éducation nationale"),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’analyser et d’harmoniser les pratiques de promotion de l’organisation de la formation professionnelle à l’éducation nationale."),
        (N_S_P, "Ne se prononce pas"),
        )


    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A5_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les acteurs socio-économiques de mon territoire. "),
        (Degre_2, "Degré 2 Je construis un réseau de partenaires socio-économiques actualisé et mobilisable"),
        (Degre_3, "Degré 3 Je suis un interlocuteur reconnu et sollicité par les acteurs socio-économiques sur un territoire."),
        (Degre_4, "Degré 4 Je suis à l’initiative de rencontres partenariales sur un projet donné."),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A6_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les éléments constitutifs d’une politique commerciale d’une organisation."),
        (Degre_2, "Degré 2 J’apporte des éléments d’analyse permettant l’évolution de la politique commerciale au sein d’un collectif"),
        (Degre_3, "Degré 3 Je contribue à la définition des objectifs de la politique commerciale,"),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner les équipes en place et transmettre une méthodologie d’élaboration de la politique commerciale."),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A6_C2_CHOICES =(
        (Degre_1, "Degré 1 Je m’informe sur les compétences et les métiers d’avenir et les grands projets de mon territoire,"),
        (Degre_2, "Degré 2 Je rédige un compte-rendu d’entretien et de détection des besoins chez les prospects."),
        (Degre_3, "Degré 3 Je maitrise les techniques de questionnement et d’écoute active pour réaliser une phase de découverte pertinente."),
        (Degre_4, "Degré 4 Je partage la méthodologie d’identification des opportunités repérées à l’échelle de mon territoire, de la région académique."),
        (N_S_P, "Ne se prononce pas"),
        )

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A6_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les types d’action commerciale et l’offre de prestations de ma structure et du réseau."),
        (Degre_2, "Degré 2 Je participe aux évènements emploi-formation de mon territoire pour recueillir des besoins en compétences et réseauter."),
        (Degre_3, "Degré 3 J’élabore la fiche produit. Je cible les prospects prioritaires."),
        (Degre_4, "Degré 4 J’organise des manifestations à l’échelle d’un territoire."),
        (N_S_P, "Ne se prononce pas"),
        )

    A1_CO_01 = models.CharField(max_length=20, choices = A1_C1_CHOICES, default = Degre_1)
    A1_CO_02 = models.CharField(max_length=20, choices = A1_C2_CHOICES, default = Degre_1)
    A1_CO_03 = models.CharField(max_length=20, choices = A1_C3_CHOICES, default = Degre_1)
    A2_CO_01 = models.CharField(max_length=20, choices = A2_C1_CHOICES, default = Degre_1)
    A2_CO_02 = models.CharField(max_length=20, choices = A2_C2_CHOICES, default = Degre_1)
    A2_CO_03 = models.CharField(max_length=20, choices = A2_C3_CHOICES, default = Degre_1)
    A3_C1 = models.CharField(max_length=20, choices = A3_C1_CHOICES, default = Degre_1)
    A3_C2 = models.CharField(max_length=20, choices = A3_C2_CHOICES, default = Degre_1)
    A3_C3 = models.CharField(max_length=20, choices = A3_C3_CHOICES, default = Degre_1)
    A4_C1 = models.CharField(max_length=20, choices = A4_C1_CHOICES, default = Degre_1)
    A4_C2 = models.CharField(max_length=20, choices = A4_C2_CHOICES, default = Degre_1)
    A4_C3 = models.CharField(max_length=20, choices = A4_C3_CHOICES, default = Degre_1)
    A5_C1 = models.CharField(max_length=20, choices = A5_C1_CHOICES, default = Degre_1)
    A5_C2 = models.CharField(max_length=20, choices = A5_C2_CHOICES, default = Degre_1)
    A5_C3 = models.CharField(max_length=20, choices = A5_C3_CHOICES, default = Degre_1)
    A6_C1 = models.CharField(max_length=20, choices = A6_C1_CHOICES, default = Degre_1)
    A6_C2 = models.CharField(max_length=20, choices = A6_C2_CHOICES, default = Degre_1)
    A6_C3 = models.CharField(max_length=20, choices = A6_C3_CHOICES, default = Degre_1)

    time = models.DateTimeField(auto_now_add=True)
##################################################

class PostA1_C1(models.Model):

    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A1_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais mon environnement proche de travail."),
        (Degre_2, "Degré 2 Je participe aux instances chargées de définir la stratégie de veille."),
        (Degre_3, "Degré 3 Je suis force de proposition pour mettre en place une stratégie de veille au service du développement de ma structure."),
        (Degre_4, "Degré 4 Je contribue à l’organisation du système de veille dans les phases de collecte, traitement et diffusion."),
        (N_S_P, "Ne se prononce pas"),
    )
    A1_C1 = models.CharField(max_length=20, choices = A1_C1_CHOICES, default = Degre_1)



class PostA1_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A1_C2_CHOICES =(
        (Degre_1, "Degré 1 J’évalue la fiabilité d’une source, crédibilité et réputation."),
        (Degre_2, "Degré 2 Je sélectionne les sources les plus pertinentes au regard de mes missions et de la stratégie de ma structure."),
        (Degre_3, "Degré 3 J’évalue la complétude de ma veille. Pour compléter ma veille j’identifie de nouveaux acteurs."),
        (Degre_4, "Degré 4 Je conseille les décideurs sur la recherche de prestataires et d’outils performants de veille."),
        (N_S_P, "Ne se prononce pas"),
    )
    A1_C2 = models.CharField(max_length=20, choices = A1_C2_CHOICES, default = Degre_1)



class PostA1_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A1_C3_CHOICES =(
        (Degre_1, "Degré 1 Je consulte les outils et les acteurs ressources au regard de mes besoins et de mes missions."),
        (Degre_2, "Degré 2 Je recherche l’information utile dans le système d’informations."),
        (Degre_3, "Degré 3 Je contextualise les données recensées en fonction de l’organisation de mon environnement professionnel interne."),
        (Degre_4, "Degré 4 J’analyse la diversité des informations recueillies afin de comprendre les transformations."),
        (N_S_P, "Ne se prononce pas"),
    )

    A1_C3 = models.CharField(max_length=20, choices = A1_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)

##############################################

class PostA2_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A2_C1_CHOICES =(
        (Degre_1, "Degré 1 J’ai mis en œuvre la démarche de diagnostic lors de mon année probatoire."),
        (Degre_2, "Degré 2 Je repère les enjeux, attentes et besoins du commanditaire."),
        (Degre_3, "Degré 3 J’organise ma démarche de diagnostic : identification des acteurs clés, choix des outils d’investigations."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner mes pairs sur la structuration et la démarche de diagnostic."),
        (N_S_P, "Ne se prononce pas"),

    )
    A2_C1 = models.CharField(max_length=20, choices = A2_C1_CHOICES, default = Degre_1)

class PostA2_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A2_C2_CHOICES =(
        (Degre_1, "Degré 1 Je sélectionne et je fais apparaitre les données de mon territoire ou de mes secteurs d’activités."),
        (Degre_2, "Degré 2 Je contextualise les données à l’échelle de la problématique."),
        (Degre_3, "Degré 3 J’extraie et j’exploite les données pertinentes afin d’identifier les besoins en compétences."),
         (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner un collectif de travail pour produire des analyses concertées."),
        (N_S_P, "Ne se prononce pas"),
        )

    A2_C2 = models.CharField(max_length=20, choices = A2_C2_CHOICES, default = Degre_1)

class PostA2_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A2_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les différents types de note et je connais la structure d’une note ou d’un document d’analyse."),
        (Degre_2, "Degré 2 Je repère les éléments de mon diagnostic à intégrer dans une note d’opportunité."),
        (Degre_3, "Degré 3 Je produis régulièrement des notes et des documents d’analyse en toute autonomie."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner des pairs à la production de notes et de documents d’analyse."),
        (N_S_P, "Ne se prononce pas"),
        )
    A2_C3 = models.CharField(max_length=20, choices = A2_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)

##############################################
class PostA3_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A3_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les éléments qui positionnent une structure sur le marché de la formation professionnelle."),
        (Degre_2, "Degré 2 Je sais positionner mon organisation dans le cadre réglementaire et législatif de la formation professionnelle."),
        (Degre_3, "Degré 3 Je m’approprie les analyses existantes."),
        (Degre_4, "Degré 4 Je suis un acteur ressource du réseau en capacité de former mes pairs."),
        (N_S_P, "Ne se prononce pas"),
        )
    A3_C1 = models.CharField(max_length=20, choices = A3_C1_CHOICES, default = Degre_1)

class PostA3_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A3_C2_CHOICES =(
        (Degre_1, "Degré 1 Je m’informe des résultats, des diagnostics, des enquêtes réalisés et des analyses produites."),
        (Degre_2, " Degré 2 J’identifie les potentiels de développement à court, moyen et long terme"),
        (Degre_3, "Degré 3 Je propose des axes de développement concrets."),
        (Degre_4, "Degré 4 Je capitalise et je mutualise les analyses réalisées pour ma structure, le réseau académique."),
        (N_S_P, "Ne se prononce pas"),
        )
    A3_C2 = models.CharField(max_length=20, choices = A3_C2_CHOICES, default = Degre_1)

class PostA3_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A3_C3_CHOICES =(
        (Degre_1, "Degré 1 Je prends connaissance des comptes-rendus des différentes instances."),
        (Degre_2, "Degré 2 Je participe aux instances de concertation en apportant des éléments d’analyse."),
        (Degre_3, "Degré 3 Je contribue à l’ordre du jour des instances de concertation."),
        (Degre_4, "Degré 4 Dans les instances de concertation à l’interne, je suis consulté sur des orientations."),
        (N_S_P, "Ne se prononce pas")
        )

    A3_C3 = models.CharField(max_length=20, choices = A3_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)

##############################
class PostA4_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A4_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les décideurs, le circuit décisionnel de ma structure, les instances s’y référant."),
        (Degre_2, "Degré 2 J’identifie le décideur concerné au regard de la situation requérant un conseil."),
        (Degre_3, "Degré 3 Je m’empare du besoin de conseil, en caractérisant le périmètre, le degré d’urgence."),
        (Degre_4, "Degré 4 J’anticipe des situations qui pourraient être sensibles et impactantes pour le développement de ma structure."),
        (N_S_P, "Ne se prononce pas"),
        )
    A4_C1 = models.CharField(max_length=20, choices = A4_C1_CHOICES, default = Degre_1)

class PostA4_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A4_C2_CHOICES =(
        (Degre_1, "Degré 1 Je connais des méthodes et des outils d’analyse."),
        (Degre_2, "Degré 2 J’utilise une méthode et les outils d’analyse nécessaires à la bonne compréhension."),
        (Degre_3, "Degré 3 A partir de mon analyse de la situation ou de la demande, j’envisage les pistes de réponses."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau pour accompagner mes pairs sur les méthodes."),
        (N_S_P, "Ne se prononce pas"),
        )

    A4_C2 = models.CharField(max_length=20, choices = A4_C2_CHOICES, default = Degre_1)

class PostA4_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A4_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les outils de communication adaptés au conseil : synthèse, note d’opportunité, rapport, etc."),
        (Degre_2, "Degré 2 Je choisis les outils de communication adaptés aux décideurs."),
        (Degre_3, "Degré 3 Je propose à l’écrit ou à l’oral un contenu synthétique pour être lu ou entendu par les décideurs."),
        (Degre_4, "Degré 4 A la demande des décideurs, je rédige et je présente un rapport circonstancié."),
        (N_S_P, "Ne se prononce pas"),)

    A4_C3 = models.CharField(max_length=20, choices = A4_C3_CHOICES, default = Degre_1)

    time = models.DateTimeField(auto_now_add=True)

##############################
class PostA5_C1(models.Model):
    created_by = CurrentUserField()

    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A5_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les différentes instances de mon territoire, leurs rôles et leur fonctionnement."),
        (Degre_2, "Degré 2 Je participe aux échanges, aux réunions et aux groupes de travail du territoire."),
        (Degre_3, "Degré 3 J’adapte ma posture et mes propos en fonction de mes interlocuteurs et des instances."),
        (Degre_4, "Degré 4 Je suis sollicité en qualité d’expert de la formation professionnelle."),
        (N_S_P, "Ne se prononce pas"),
        )
    A5_C1 = models.CharField(max_length=20, choices = A5_C1_CHOICES, default = Degre_1)

class PostA5_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A5_C2_CHOICES =(
        (Degre_1, "Degré 1 Je distingue les 3 voies de formation professionnelle. Je m’informe en interne sur les missions."),
        (Degre_2, "Degré 2 J’identifie sur mon territoire l’offre de formations."),
        (Degre_3, "Degré 3 J’explique la mission de service public de l’éducation nationale."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’analyser et d’harmoniser les pratiques de promotion de l’organisation."),
        (N_S_P, "Ne se prononce pas"),
        )

    A5_C2 = models.CharField(max_length=20, choices = A5_C2_CHOICES, default = Degre_1)

class PostA5_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A5_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les acteurs socio-économiques de mon territoire."),
        (Degre_2, "Degré 2 Je construis un réseau de partenaires socio-économiques."),
        (Degre_3, "Degré 3 Je suis un interlocuteur reconnu et sollicité par les acteurs socio-économiques."),
        (Degre_4, "Degré 4 Je suis à l’initiative de rencontres partenariales sur un projet donné."),
        (N_S_P, "Ne se prononce pas"),
        )

    A5_C3 = models.CharField(max_length=20, choices = A5_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)

##################################################
class PostA6_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A6_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les éléments constitutifs d’une politique commerciale d’une organisation."),
        (Degre_2, "Degré 2 J’apporte des éléments d’analyse permettant l’évolution de la politique commerciale."),
        (Degre_3, "Degré 3 Je contribue à la définition des objectifs de la politique commerciale."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner les équipes en place et transmettre une méthodologie."),
        (N_S_P, "Ne se prononce pas"),
        )
    A6_C1 = models.CharField(max_length=20, choices = A6_C1_CHOICES, default = Degre_1)
class PostA6_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A6_C2_CHOICES =(
        (Degre_1, "Degré 1 Je m'informe sur les compétences et les métiers d’avenir et les grands projets de mon territoire."),
        (Degre_2, "Degré 2 Je rédige un compte-rendu d’entretien et de détection des besoins chez les prospects."),
        (Degre_3, "Degré 3 Je maitrise les techniques de questionnement et d’écoute active pour identifier les besoins des structures rencontrées."),
        (Degre_4, "Degré 4 Je partage la méthodologie d’identification des opportunités."),
        (N_S_P, "Ne se prononce pas"),
        )

    A6_C2 = models.CharField(max_length=20, choices = A6_C2_CHOICES, default = Degre_1)

class PostA6_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    A6_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les types d’action commerciale et l’offre de prestation de ma structure et du réseau."),
        (Degre_2, "Degré 2 Je participe aux évènements emploi-formation de mon territoire pour recueillir des besoins en compétences et réseauter."),
        (Degre_3, "Degré 3 J’élabore la fiche produit. Je cible les prospects prioritaires."),
        (Degre_4, "Degré 4 J’organise des manifestations à l’échelle d’un territoire."),
        (N_S_P, "Ne se prononce pas"),
        )

    A6_C3 = models.CharField(max_length=20, choices = A6_C3_CHOICES, default = Degre_1)

    time = models.DateTimeField(auto_now_add=True)


#################Pole B################################
class PostB1_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B1_C1_CHOICES =(
        (Degre_1, "Degré 1 Je repère les sources d’informations pédagogiques."),
        (Degre_2, "Degré 2 J’identifie et je sélectionne les sources d’informations me permettant de recenser des évolutions."),
        (Degre_3, "Degré 3 Je réalise ma veille en fonction de mes domaines d’activités."),
        (Degre_4, "Degré 4 Je suis un acteur ressources pour le réseau en capacité de croiser différentes sources d’informations."),
        (N_S_P, "Ne se prononce pas"),
        )

    B1_C1= models.CharField(max_length=20, choices = B1_C1_CHOICES, default = Degre_1)

class PostB1_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B1_C2_CHOICES =(
        (Degre_1, "Degré 1 Je m’informe sur les orientations pédagogiques ou techno-pédagogiques."),
        (Degre_2, "Degré 2 Je mesure les évolutions pédagogiques nécessaires au regard des pratiques actuelles du réseau."),
        (Degre_3, "Degré 3 Je sélectionne en autonomie les données pertinentes permettant d’identifier les évolutions."),
        (Degre_4, "Degré 4 Je sélectionne les données pertinentes à des fins de contribution académique, nationale."),
        (N_S_P, "Ne se prononce pas"),
        )

    B1_C2 = models.CharField(max_length=20, choices = B1_C2_CHOICES, default = Degre_1)

class PostB1_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B1_C3_CHOICES =(
        (Degre_1, "Degré 1 J’identifie les acteurs impliqués dans la dynamique d’évolution ou d’adaptation des pratiques pédagogiques."),
        (Degre_2, "Degré 2 J’identifie les tendances d’évolution ou d’adaptation."),
        (Degre_3, "Degré 3 Je présente les informations clés et les évolutions à engager aux équipes impliquées, lors de réunions."),
        (Degre_4, "Degré 4 Je partage les informations clés et les évolutions à engager avec les équipes impliquées, lors de réunions."),
        (N_S_P, "Ne se prononce pas"),
        )

    B1_C3 = models.CharField(max_length=20, choices = B1_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)

##################################################


class PostB2_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B2_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les techniques d’identification des besoins en compétences individuels ou collectifs."),
        (Degre_2, "Degré 2 Je recueille les besoins en compétences en mobilisant les techniques adaptées."),
        (Degre_3, "Degré 3 Je conduis un entretien d’analyse de la demande permettant de clarifier et d’identifier les besoins en compétences."),
        (Degre_4, "Degré 4 Je suis un acteur ressource du réseau en capacité d’accompagner et de former sur les techniques d’identification des besoins "),
        (N_S_P, "Ne se prononce pas"),
        )

    B2_C1 = models.CharField(max_length=20, choices = B2_C1_CHOICES, default = Degre_1)

class PostB2_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B2_C2_CHOICES =(
        (Degre_1, "Degré 1 Je connais les éléments qualifiant le contexte d’une demande."),
        (Degre_2, "Degré 2 Je pose des questions ciblées ou bien je décrypte les différens supports."),
        (Degre_3, "Degré 3 Je vérifie ma compréhension du contexte en reformulant la demande."),
        (Degre_4, "Degré 4 Je prends en compte la pluralité des enjeux dans l’analyse du contexte de la demande."),
        (N_S_P, "Ne se prononce pas"),
        )

    B2_C2= models.CharField(max_length=20, choices = B2_C2_CHOICES, default = Degre_1)


class PostB2_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B2_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les éléments constitutifs d’une étude de faisabilité."),
        (Degre_2, "Degré 2 Je recueille les données nécessaires à l’étude de faisabilité du projet."),
        (Degre_3, "Degré 3 Je produis une étude de faisabilité à partir de l’analyse des éléments financiers, humains, pédagogiques et techniques."),
        (Degre_4, "Degré 4 J’adapte mon étude de faisabilité à différents contextes, projets et acteurs."),
        (N_S_P, "Ne se prononce pas"),
        )

    B2_C3= models.CharField(max_length=20, choices = B2_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)



class PostB3_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B3_C1_CHOICES =(
        (Degre_1, "Degré 1 A partir de la demande client, je prends connaissance des ressources utiles."),
        (Degre_2, "Degré 2 A partir de la demande client, je participe à une réunion avec les acteurs internes et/ou externes."),
        (Degre_3, "Degré 3 Je planifie et je coordonne le travail de conception avec les acteurs concernés."),
        (Degre_4, "Degré 4 Je suis acteur ressource du réseau pour prendre en charge l’organisation d’un travail de conception d’une réponse."),
        (N_S_P, "Ne se prononce pas"),
        )

    B3_C1= models.CharField(max_length=20, choices = B3_C1_CHOICES, default = Degre_1)


class PostB3_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B3_C2_CHOICES =(
        (Degre_1, "Degré 1 Je connais les approches innovantes dans les dispositifs de développement des compétences."),
        (Degre_2, "Degré 2 J’étudie les options méthodologiques, pédagogiques, techniques et financières adaptées au projet."),
        (Degre_3, "Degré 3 J’identifie les acteurs internes et externes disposant des savoir-faire pour innover."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité de conseiller sur le choix des options méthodologiques."),
        (N_S_P, "Ne se prononce pas"),
        )

    B3_C2= models.CharField(max_length=20, choices = B3_C2_CHOICES, default = Degre_1)


class PostB3_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B3_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les étapes de l’ingénierie de formation et les déterminants d’un dispositif de développement des compétences."),
        (Degre_2, "Degré 2 Je m’appuie sur des ingénieries existantes et des parcours ressources."),
        (Degre_3, "Degré 3 Je construis le dispositif à partir des options choisies en m’assurant de répondre aux exigences."),
        (Degre_4, "Degré 4 Je modélise ma méthode d’élaboration de dispositifs innovants."),
        (N_S_P, "Ne se prononce pas"),
        )

    B3_C3= models.CharField(max_length=20, choices = B3_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)


class PostB4_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B4_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais les trames de réponse du client ou du commanditaire."),
        (Degre_2, "Degré 2 Je contribue à définir les règles et conditions de présentation d’une offre de prestation."),
        (Degre_3, "Degré 3 J’intègre les standards et les exigences réglementaires de présentation de l’offre de prestation."),
        (Degre_4, "Degré 4 Je suis un acteur ressource du réseau en capacité de valider la conformité du respect des règles."),
        (N_S_P, "Ne se prononce pas"),
        )

    B4_C1= models.CharField(max_length=20, choices = B4_C1_CHOICES, default = Degre_1)


class PostB4_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B4_C2_CHOICES =(
        (Degre_1, "Degré 1 J’identifie les savoir-faire de ma structure, du réseau pour valoriser l’offre de prestation à formaliser."),
        (Degre_2, "Degré 2 Je repère les éléments à valoriser pour la rédaction de l’offre."),
        (Degre_3, "Degré 3 Je maitrise les techniques rédactionnelles pour rendre l’offre de prestation lisible et attractive."),
        (Degre_4, "Degré 4 J’organise et j’anime un comité de lecture pour valider l’attractivité de l’offre au regard des exigences."),
        (N_S_P, "Ne se prononce pas"),
        )

    B4_C2= models.CharField(max_length=20, choices = B4_C2_CHOICES, default = Degre_1)

class PostB4_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    B4_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les intérêts de l’organisation en matière de stratégie de développement."),
        (Degre_2, "Degré 2 Au sein d’un collectif de travail, je contribue à la construction d’un argumentaire pour la négociation."),
        (Degre_3, "Degré 3 Je construis un argumentaire pour préparer la phase de négociation."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité de modéliser les process de négociation."),
        (N_S_P, "Ne se prononce pas"),
        )

    B4_C3= models.CharField(max_length=20, choices = B4_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)

###########################Pole C#########################################################
class PostC1_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C1_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais la démarche de projet."),
        (Degre_2, "Degré 2 Je participe à l’élaboration d’un projet dans toutes ses composantes."),
        (Degre_3, "Degré 3 Je pilote des projets à l’échelle de ma structure."),
        (Degre_4, "Degré 4 Je pilote des projets complexes d’envergure académique, nationale sur des secteurs particuliers."),
        (N_S_P, "Ne se prononce pas"),
        )

    C1_C1= models.CharField(max_length=20, choices = C1_C1_CHOICES, default = Degre_1)

class PostC1_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C1_C2_CHOICES =(
        (Degre_1, "Degré 1 Je connais les acteurs et les moyens existants de mon organisation."),
        (Degre_2, "Degré 2 Je repère les acteurs de mon organisation et les partenaires externes mobilisables pour le projet."),
        (Degre_3, "Degré 3 J’estime les moyens humains et matériels nécessaires au projet en sollicitant les acteurs experts de ma structure et du réseau académique."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour ma structure."),
        (N_S_P, "Ne se prononce pas"),
        )

    C1_C2 = models.CharField(max_length=20, choices = C1_C2_CHOICES, default = Degre_1)

class PostC1_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C1_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les modalités et les indicateurs d’évaluation de projets déjà mis en œuvre."),
        (Degre_2, "Degré 2 J’utilise les outils d’évaluation et de suivi mis à disposition par ma structure, le réseau académique."),
        (Degre_3, "Degré 3 J’anime des points d’étape de réalisation du projet afin de mesurer l’état d’avancement, les écarts éventuels et les actions correctives."),
        (Degre_4, "Degré 4 Je suis un acteur ressources pour le réseau en capacité de suivre et d’évaluer des projets d’envergure régionale, nationale, européenne, des projets impliquant des partenaires."),
        (N_S_P, "Ne se prononce pas"),
        )

    C1_C3 = models.CharField(max_length=20, choices = C1_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)

##################################################


class PostC2_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C2_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais l’organigramme, les fonctions et les missions de chacun dans ma structure."),
        (Degre_2, "Degré 2 Je mobilise une équipe sur la durée du projet jusqu’à l’atteinte des objectifs"),
        (Degre_3, "Degré 3 Je fédère les équipes autour d’un sens partagé en expliquant les enjeux et l’ingénierie du projet."),
        (Degre_4, "Degré 4 Je suis un acteur ressource pour le réseau en capacité de mobiliser des équipes"),
        (N_S_P, "Ne se prononce pas"),
        )

    C2_C1 = models.CharField(max_length=20, choices = C2_C1_CHOICES, default = Degre_1)

class PostC2_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C2_C2_CHOICES =(
        (Degre_1, "Degré 1 Je me familiarise aux techniques et aux outils d’animation et de management variés."),
        (Degre_2, "Degré 2 J’applique les techniques d’animation facilitant l’engagement coopératif des équipes."),
        (Degre_3, "Degré 3 J’utilise les techniques de management en adoptant une posture bienveillante."),
        (Degre_4, "Degré 4 J’évalue les méthodes et techniques mises en œuvre et propose des améliorations."),
        (N_S_P, "Ne se prononce pas"),
        )

    C2_C2= models.CharField(max_length=20, choices = C2_C2_CHOICES, default = Degre_1)


class PostC2_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C2_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais -	les ressources mises à disposition par le service RH."),
        (Degre_2, "Degré 2 J’identifie les compétences acquises des collaborateurs administratifs et pédagogiques."),
        (Degre_3, "Degré 3 J’anticipe les besoins en compétences et j’identifie celles manquantes, au regard de l’évolution de mon offre."),
        (Degre_4, "Degré 4 Je contribue à l’évolution de la cartographie des compétences des acteurs de ma structure et du réseau."),
        (N_S_P, "Ne se prononce pas"),
        )

    C2_C3= models.CharField(max_length=20, choices = C2_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)



class PostC3_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C3_C1_CHOICES =(
        (Degre_1, "Degré 1 J’identifie les partenaires potentiels de mon territoire : concurrents, prescripteurs, OPCO, certificateurs, entreprises, collectivités territoriales."),
        (Degre_2, "Degré 2 Je rencontre les partenaires de mon territoire pour me présenter et partager nos offres de service respectives."),
        (Degre_3, "Degré 3 J’active mon réseau pour répondre aux problématiques du territoire."),
        (Degre_4, "Degré 4 Je valorise les complémentarités pour un projet d’envergure régionale, nationale nécessitant une réponse partenariale."),
        (N_S_P, "Ne se prononce pas"),
        )

    C3_C1= models.CharField(max_length=20, choices = C3_C1_CHOICES, default = Degre_1)


class PostC3_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C3_C2_CHOICES =(
        (Degre_1, "Degré 1 Je connais les différentes formes juridiques des partenariats."),
        (Degre_2, "Degré 2 Je participe à un premier temps d’échanges sur l’objet du partenariat à construire."),
        (Degre_3, "Degré 3 Je participe à la détection des complémentarités et des économies d’échelle que je présente aux décideurs de ma structure, du réseau."),
        (Degre_4, "Degré 4 Sur sollicitation du DRAFPIC, je propose des accords de groupement de consortium."),
        (N_S_P, "Ne se prononce pas"),
        )

    C3_C2= models.CharField(max_length=20, choices = C3_C2_CHOICES, default = Degre_1)


class PostC3_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C3_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais les techniques d’animation et de coopération."),
        (Degre_2, "Degré 2 Je participe aux instances du partenariat et je contribue à leur animation."),
        (Degre_3, "Degré 3 Je pilote en responsabilité des instances, j’anime des groupes de travail conformément aux engagements mutuels."),
        (Degre_4, "Degré 4 Je suis un interlocuteur repéré au niveau de ma structure, du réseau pour l’animation de partenariats d’envergure régionale, nationale et européenne."),
        (N_S_P, "Ne se prononce pas"),
        )

    C3_C3= models.CharField(max_length=20, choices = C3_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)


class PostC4_C1(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C4_C1_CHOICES =(
        (Degre_1, "Degré 1 Je connais la règlementation relative aux certifications des organisations qui s’impose à tous les prestataires."),
        (Degre_2, "Degré 2 J’identifie l’application et le respect des exigences et indicateurs de performances de l’organisation."),
        (Degre_3, "Degré 3 Je peux présenter à mes collaborateurs et à mes partenaires les engagements du label et leur déclinaison au niveau de la structure."),
        (Degre_4, "Degré 4 Je conseille sur l’évolution de la politique qualité mise en place au niveau de ma structure, au niveau du réseau académique."),
        (N_S_P, "Ne se prononce pas"),
        )

    C4_C1= models.CharField(max_length=20, choices = C4_C1_CHOICES, default = Degre_1)


class PostC4_C2(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C4_C2_CHOICES =(
        (Degre_1, "Degré 1 Je peux décrire le management de la qualité mis en place dans mon organisation."),
        (Degre_2, "Degré 2 J’utilise les bons documents du système qualité et je suis capable de les rapprocher d’un processus."),
        (Degre_3, "Degré 3 Je participe au processus de veille et de respect des engagements de qualité en utilisant les moyens de pilotage de ma structure, du réseau."),
        (Degre_4, "Degré 4 Je suis un acteur ressource du réseau pour relayer les engagements qualité de l’académie."),
        (N_S_P, "Ne se prononce pas"),
        )

    C4_C2= models.CharField(max_length=20, choices = C4_C2_CHOICES, default = Degre_1)

class PostC4_C3(models.Model):
    created_by = CurrentUserField()
    Degre_1 = "Degre_1"
    Degre_2 = "Degre_2"
    Degre_3 = "Degre_3"
    Degre_4 = "Degre_4"
    N_S_P = "N_S_P"
    C4_C3_CHOICES =(
        (Degre_1, "Degré 1 Je connais le cycle d’amélioration et je peux le décrire."),
        (Degre_2, "Degré 2 J’évalue la qualité des prestations au regard du cahier des charges pour identifier les écarts et alerter sur les risques potentiels."),
        (Degre_3, "Degré 3 J’analyse le résultat des indicateurs au sein d’un collectif et j’assure le reporting auprès du service qualité et de la direction de ma structure."),
        (Degre_4, "Degré 4 Je suis pilote du processus d’amélioration continue de ma structure."),
        (N_S_P, "Ne se prononce pas"),
        )

    C4_C3= models.CharField(max_length=20, choices = C4_C3_CHOICES, default = Degre_1)
    time = models.DateTimeField(auto_now_add=True)















