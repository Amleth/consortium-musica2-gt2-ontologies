Livrables GT2

Guide : liste de cas de modélisation organisée en grandes thématiques (plus ou moins thématiques des ateliers) 

**1. Besoin musicologique** (ou méthodologique) de modélisation exprimé sous la forme d’une questions (le guide répond à des questions concrètes) 

Dans le cadre du Consortium Musica2, le groupe de travail n°2 "Ontologies et thésaurii" a souhaité instaurer une dynamique collective durant l'année 2023-2024 en organisant des ateliers dédiés à différentes problématiques musicologiques traitées au prisme des outils ontologiques. Ces ateliers ont permis de fédérer avec régularité une communauté scientifique nationale autour de questions communes à tout musicologue : expression des dates, _thesaurii_, indexaction conceptuelle, _etc_. De ces points de focus ont rejailli des besoins, des doutes, mais aussi des consensus nous permettant de formaliser des pratiques musicologiques correctes par le croisement d'expériences variées. Nous avons alors fait le choix de présenter ce livrable en axes plus ou moins similaires à ceux de nos ateliers, tout en gardant à l'esprit l'aspect _work-in-progress_ d'un tel travail. 

Bien que nous abordions diverses ontologies durant ces ateliers, telles LRMoo ou bien DoRéMus, une extension du modèle FRBRoo permettant la description étendue de catalogue musicaux, celles-ci sont toutes issues du socle Cidoc-CRM. Du fait de l'universalité de ses objets et de l'expressivité avec lesquels elle les définit, cette ontologie est particulièrement adaptée aux sciences humaines. Les concepts et les relations implicites et explicites peuvent être modélisées de manière variées pour s'approcher au plus du sens réel que l'utilisateur souhaite y instiller. Un besoin primordial émerge alors rapidement de l'assemblée : développer une meilleure connaissance et compréhension des outils de modélisation conceptuelle. En effet, bien que la grande majorité des chercheur·euse·s soit familière avec les bases de données, l'étape de modélisation des données est la plupart du temps négligée et fait ainsi face aux écueils suivants :
- faire l'impasse sur un terreau de connaissances existantes
- un manque de clarté dans la relations sémantiques entre les données
- l'impossibilité d'alignement avec d'autres systèmes 
- etc

Ces ateliers ont malgré tout démontré la nécessité de l'usage d'outils ontologiques dans la bonne gestion de dates et de 



Ce document abordera dans un premier temps des questions liées à la **datation** et plus particulièrement à l'adéquation recherchée entre la nécessité informatique d'une date précise et la souplesse nécessaire à la juste transmission de l'information scientifique. Faisant logiquement suite à ces problématiques, nous nous questionnerons sur les enjeux soulevés lors d'un travail de **prosopographie**, s'intéressant aux dates et lieux mais aussi aux personnes et institutions, ajoutant ainsi un niveau supplémentaire de complexité à notre travail de modélisation. Après avoir abordé ces points, nous pourrons nous consacrer à l'**indexation conceptuelle** et l'usage des _thesaurii_, nous permettant à nouveau d'aborder un champ d'abstraction supplémentaire dans notre travail de modélisation. 
Nous avons également souhaité valoriser les ressources du Consortium Musica2 à travers deux ateliers démontrant l'intérêt du croisement d'outils ontologiques avec d'autres approches. Nous avons ainsi collaboré avec le GT1 "MEI" pour un atelier dédié à la question des métadonnées MEI dans divers projets éditoriaux, et pourrons ainsi aborder le croisement des outils issus de la MEI et du Cidoc-CRM dans le travail sur les **éditions critiques**.

**Parler de modules de base**


Pour un objet : la datation de L’Heure espagnole de Ravel porte par exemple à confusion. La partition chant et piano a été publiée en 1908 mais l'orchestration réalisée en 1910. La première interprétation de l’opéra a eu lieu en 1911, la même année que la publication de la partition pour orchestre. Ce cas souligne donc la possibilité de multiplier les champs "date".
Pour une personne : une incertitude se présente pour une personne née la dernière décennie de février 1766, pouvant également être exprimé le 2?/02/1766. Idem pour une date présentant une incertitude plus ou moins toléré, comme un décès survenu le 7 ou 15/12/1654. Lors de l'usage du Cidoc CRM, plusieurs instances de E13 viendront justifier les choix de datation.
Pour une institution : le terme circa est régulièrement utilisé ; quid de sa désignation scientifique ? Par exemple, une institution fondée circa 1540.
Pour un événement.



**2. Problématisation :** lister ce qui n’est pas trivial, les écueils, les choses qui ne se perçoivent pas immédiatement (apport analytique et mise en contexte)






**3. Contextualisation technique :** expérience problématique puis analyse technique de la question

**Dates**
Directions retenues
Si la possibilité d'exprimer le temps de manière souple est importante pour le chercheur en SHS, le fait qu'un événement ne dispose pas de date calculable par la machine (c'est-à-dire exprimable en ISO 8601) l'exclu de fait de toute représentation chronologique calculée des données. En conséquence, il faudrait que toute date « souple » soit flanquée d'un intervalle défini par deux dates calculables. Ces dates devraient pouvoir être définies par le chercheur, car il est le seul à savoir comment doit être raisonablement résolue une approximation comme « 3ème quart du 4ème siècle » (350—375 ? Autre chose ?). Les intervalles peuvent alors être définis de quatre manières principales :

**



Nous envisageons en effet de laisser cette archive GitHub ouverte et la mettre à jour de manière régulière, en conséquence de nos réfléxions tout autant que d'avancées dans les solutions de modélisation.

**

4. Proposition Cidoc-CRM : a) bout de graphe qui illustre la proposition b) alternatives CRM commentées c) identifier les limitations, les problèmes potentiels

· Faire des liens entre les cas
· Montrer les liens avec le GT1 et GT4 



