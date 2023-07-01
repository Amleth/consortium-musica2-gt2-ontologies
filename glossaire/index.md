# Glossaire technique

## 📕 Environnements socio-techniques

### 🏷️ Internet & le Web

- https://fr.wikipedia.org/wiki/Internet
- https://fr.wikipedia.org/wiki/World_Wide_Web

### 🏷️ hypertexte

Ted Nelson (inventeur de l'hypertexte) : *« HTML is precisely what we were trying to PREVENT— ever-breaking links, links going outward only, quotes you can't follow to their origins, no version management, no rights management. »*

### 🏷️ Adressabilité

- De quoi est-il question ?
  - Le premier vers de la deuxième strophe de « Tombeau » de Mallarmé
  - *سورة الأعراف, verset 13*, *apocalypse de saint jean chapitre 13 verset 18*
  - La troisième note de « J'ai du bon tabac »
  - Le bonhomme qui tient une balance coincé dans une vielle à roue dans [*Le Jardin des délices*](https://fr.wikipedia.org/wiki/Le_Jardin_des_d%C3%A9lices#/media/Fichier:The_Garden_of_earthly_delights.jpg) de Bosch
- Le Web est le « milieu informationnel » dans laquelle la recherche se fait et met en visibilité ses productions en vue de les diffuser et de les ouvrir au commentaire. L'adressabilité des données et des documents est un enjeu clef.

La lecture scolastique :

*« Alors que le haut Moyen Âge ne connaissait que de modestes subdivisions du texte, reposant moins sur des signes spécifiques que sur des ornements (rehaussement des lettres initiales par la couleur, changements d'écriture, décorations diverses), on passe à un véritable système de techniques auxiliaires de la lecture et de la consultation du livre, destinées à identifier rapidement le passage que l'on recherche : rubrication, découpage en paragraphes, titres de chapitre, séparation du texte et du commentaire, sommaires, tables des concordances des termes, index et tables analytiques alphabétiques. »*

(Cavallo & Chartier, *Histoire de la lecture dans le monde occidental*)

### 🏷️ Web sémantique

#### Un projet insensé

- Constatation : le Web, c'est le bazar ; notamment du fait de l'homonymie : mais de quoi parle t-on au juste quand on tape « Doors » sur Google ?
- On ne peut jamais préciser le sens de ce sur quoi portent nos requêtes, qui sont exprimées en texte.
- Pour désambiguïser le recours à un terme, il faudrait pouvoir l'identifier (et non pas seulement s'appuyer sur sa dénomination en langage naturel), c'est-à-dire, pouvoir s'y référer selon une URL (car on est sur le Web).
- Le projet du Web sémantique est en premier lieu de donner une URL à chaque chose.
- Préciser le sens de chaque chose à l'échelle du Web est discutable (relents positivistes, cela fait abstraction de la culture, les humains ne sont pas des ordinateurs).

#### Un peu plus précisément…

- Le Web sémantique est basé sur les mêmes principes que les Web « 1.0 » (de documents) & « 2.0 » (social) :
  - même structure informationnelle (l'hypertexte)
  - même protocole (HTTP)
  - même mécanisme d'identification (les URL)
- …mais au bout d'une URL, on ne trouve pas de l'HTML destiné à être lu par un humain, mais des données au format RDF.

### 🏷️ RDF

- Représente toute information sous forme d'un triplet sujet-prédicat-objet.
- *« Jean-Sébastien Bach est né à Eisenach » :*
  - Sujet : [http://data.doremus.org/artist/269cec9d-5025-3a8a-b2ef-4f7acb088f2b](http://data.doremus.org/artist/269cec9d-5025-3a8a-b2ef-4f7acb088f2b)
  - Prédicat : [http://dbpedia.org/property/birthPlace](http://dbpedia.org/property/birthPlace)
  - Objet : [http://data.doremus.org/describe/?url=http://dbpedia.org/resource/Eisenach](http://data.doremus.org/describe/?url=http%3A%2F%2Fdbpedia.org%2Fresource%2FEisenach)

<img src="example-graph-iris.jpg" style="width: 50%;"/>

- Connectés entre eux, les triplets forment un graphe.

### 🏷️ API (REST)

- https://fr.wikipedia.org/wiki/Interface_de_programmation

---

## 📕 Données & documents

### 🏷️ Donnée (base de données) / Document (corpus documentaire)

### 🏷️ Modèle conceptuel de données

- Formalise l'analyse de la structure de l'information contenue dans une base de données (les types d'informations qui doivent être enregistrés dans la base de donnée, avec leur propriétés et les relations qu'ils entretiennent).
- Utilisé pendant la phase d'élaboration du cahier des charges.
- Enjeu scientifique.

### 🏷️ XML

### 🏷️ TEI

### 🏷️ MEI

- https://music-encoding.org/
- https://music-encoding.org/guidelines/v4/content/
- https://mei-friend.mdw.ac.at/
- https://editor.verovio.org/

### 🏷️ IIIF

- https://iiif.biblissima.fr/
- Adressabilité d'une zone au sein d'une image via une URL : [https://gallica.bnf.fr/iiif/ark:/12148/btv1b8446958b/f39/423,1322,1365,1135/,800/0/native.jpg](https://gallica.bnf.fr/iiif/ark:/12148/btv1b8446958b/f39/423,1322,1365,1135/,800/0/native.jpg)
- Retour au contexte : [https://gallica.bnf.fr/iiif/ark:/12148/btv1b8446958b/f39/full/max/0/native.jpg](https://gallica.bnf.fr/iiif/ark:/12148/btv1b8446958b/f39/full/max/0/native.jpg)
- Image entière, hauteur de 800 pixels, sans rotation, format JPG : [http://gallica.bnf.fr/iiif/ark:/12148/btv1b8451103b/f9/full/,800/0/native.jpg](http://gallica.bnf.fr/iiif/ark:/12148/btv1b8451103b/f9/full/,800/0/native.jpg)
- Une cantate redressée : [https://gallica.bnf.fr/iiif/ark:/12148/btv1b9010251k/f9/full/max/358/default.jpg]
- Région d'image, à 90% de sa taille, rotation de 325°, niveau de gris, format PNG : [http://gallica.bnf.fr/iiif/ark:/12148/btv1b8451103b/full/max/0/gray.png](http://gallica.bnf.fr/iiif/ark:/12148/btv1b8451103b/f9/1200,1300,620,580/pct:90/325/gray.png)
- Tester l'API Image : [https://tomcrane.github.io/the-long-iiif/image-api.html](https://tomcrane.github.io/the-long-iiif/image-api.html)
- Requête d'informations sur l'image : [http://www.e-codices.unifr.ch/loris/sbb/sbb-C0005-2/sbb-C0005-2_0000_002r.jp2/info.json](http://www.e-codices.unifr.ch/loris/sbb/sbb-C0005-2/sbb-C0005-2_0000_002r.jp2/info.json)

---

## 📕 Web sémantique

### 🏷️ Thésauri

- Liste organisée de termes contrôlés et normalisés représentant les concepts d'un domaine de la connaissance. ([Wikipedia](https://fr.wikipedia.org/wiki/Th%C3%A9saurus_documentaire))
- Désambiguïsation : https://iconclass.org/24C37 vs https://iconclass.org/91B111
- Un exemple utile à la musique : https://data.doremus.org/vocabularies/ + https://github.com/DOREMUS-ANR/knowledge-base/tree/master/vocabularies

### 🏷️ SKOS

- Ontologie pour représenter des thésauri.
- https://www.w3.org/TR/skos-primer/

### 🏷️ Ontologie

- [Wikipedia](https://fr.wikipedia.org/wiki/Ontologie_(informatique)) :
  - Modèle de données contenant des concepts et relations permettant de modéliser un ensemble de connaissances dans un domaine donné.
  - Spécification formelle et explicite d’une conceptualisation partagée.

### 🏷️ CIDOC-CRM

- Émanation de l'ICOM (International Council of Museums)
- Ontologie pour la représentation du patrimoine matériel et immatériel de l'humanité, et des connaissances produites à son endroit.
- Opinion : L'infrastructure technique et informationnelle du Web sémantique conjuguée à la communauté internationale CIDOC-CRM constituent une des meilleures réponses socio-techniques possibles en 2023 pour s'assurer que les données scientifiques et patrimoniales seront encore lisibles dans 10 ou 20 ans.

### 🏷️ SPARQL, SPARQL endpoint

- Langage d'interrogation de graphes de données RDF.
- Il est possible de publier l'intégralité d'une base de données RDF via un SPARQL endpoint.

---

## 📕 Parlons langages de programmation ?