# Introduction. Pourquoi et comment utiliser une ontologie dans la conception d'une base de données pour la musicologie ?

## Caractérisation d'une base de données pour la musicologie

Avant de montrer en quoi les technologies et méthodologies du Web sémantique et de l'ontologie CIDOC CRM peuvent être fécondes pour la conception de bases de données pour la musicologie, nous présentons un certain nombre de caractéristiques importantes de ces dernières, qui les différencient d'autres types de bases de données.

### Hétérogénéité des sources documentaires et adressabilité interne

La musicologie est une discipline qui étudie le contenu et le contexte de sources de natures très diverses : musique notée, textes théoriques, contenus iconographiques, informations consignées dans des registres, documents administratifs textuels, enregistrements sonores, vidéos, etc. Ces pratiques se prolongent naturellement en milieu numérique, et se conduisent actuellement autour d'objets tels que les fichier [XML MEI](https://music-encoding.org/), [XML TEI](https://tei-c.org/), fichier [images matricielles](https://fr.wikipedia.org/wiki/Image_matricielle), fichiers audio et/ou vidéo, données textuelles structurées (aux formats [XML](https://fr.wikipedia.org/wiki/Extensible_Markup_Language), [SQL](https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_relationnelle), [RDF](https://fr.wikipedia.org/wiki/Resource_Description_Framework), [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation), etc.).

Ainsi les bases de données de la musicologie contiennent-elles bien souvent des connaissances produites à propos des sources. Afin que ces données puissent faire sens, il faut que leur articulation aux sources soit précise. Pour exemples, une donnée d'analyse musicale devra renvoyer avec précision à l'observable qu'elle qualifie sur la partition (une note, un accord, une phrase, une cadence…), des données transcrivant et annotant une entrée dans un registre devront pointer précisément l'exemplaire, la page et la section auxquels elles se rapportent, une annotation portant sur un détail d'une image devrait pouvoir circonscrire précisément le fragment visuel concerné, etc. Nous nommons adressabilité la capacité technique d'un système d'information permettant d'identifier, de désigner sans ambiguïté et de rendre accessible (« adresser ») un fragment au sein d'un contenu. La possibilité de rendre adressable les fragments afin d'y articuler un commentaire critique constitue une des clef de voûte technique des mondes lettrés, et cette préoccupation cheville l'histoire des supports d'écriture :

> *« Alors que le haut Moyen Âge ne connaissait que de modestes subdivisions du texte, reposant moins sur des signes spécifiques que sur des ornements (rehaussement des lettres initiales par la couleur, changements d’écriture, décorations diverses), on passe à un véritable système de techniques auxiliaires de la lecture et de la consultation du livre, destinées à identifier rapidement le passage que l’on recherche : rubrication, découpage en paragraphes, titres de chapitre, séparation du texte et du commentaire, sommaires, tables des concordances des termes, index et tables analytiques alphabétiques. »* (Guglielmo Cavallo & Roger Chartier, *Histoire de la lecture dans le monde occidental*, Points Histoire, 2001)

Dans le champ des systèmes d'information Web, et notamment, comme nous allons le voir, des bases de données scientifiques publiées sur le Web, les enjeux techniques autour de l'adressabilité des sources se traduisent par des questions de mise à disposition en masse des sources numérisées accompagnées de la capacité à générer une [URL](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) pour chaque fragment qu'un chercheur ou qu'une chercheuse pourrait vouloir pointer ou annoter. Dans le périmètre technique des sources musicales ou textuelles encodées en XML (MEI et TEI), l'enjeu est de rendre les fragments XML [identifiés de manière unique de manière interne au sein des fichiers](https://www.w3.org/TR/2005/REC-xml-id-20050909/) adressables sur le Web via des URL. Pour ce qui concerne les images matricielles, le standard [IIIF](https://iiif.biblissima.fr/) réalise une adressabilité totale de n'importe quel fragment rectangulaire sous la forme d'URL.

Ce sont l'accessibilité et l'adressabilité conjointe des fragments des sources et des données critiques qui s'y rapportent qui constituent la base d'un système d'information scientifique sur le Web.

### Captation du travail critique sur les sources



### Structuration des connaissances utilisées pour analyser les sources


### Captation du contexte interprétatif

<!--
corpus, critères interprétatifs, structure des projets collaboratifs, cahier de laboratoire
-->

### Pérennisation des données

<!--
nouveau contexte socio-technique
https://www.economie.gouv.fr/files/files/PDF/DP_LoiNumerique.pdf

-->

## Le Web sémantique comme milieu idéal pour la publication des données de la recherche

<!--
Notion de triplet.

Promesse d’une base de données à l’échelle du Web. Le Web initial (Tim Berners
Lee, 1991) était un Web de documents liés (hypertexte), le Web sémantique est
un Web de données liées, chacune étant identifiée par une URI.
▪ Toute information s’exprime sous la forme d’un triplet (sujet/prédicat/objet) dans
un langage de description qui est le RDF.
▪ La connexion de ces triplets RDF forme un graphe.
▪ Chaque prédicat est également identifié par une URL.
▪ C’est le milieu technique idéal pour des données FAIR, pour l’expression et la
diffusion des données de la recherche (publication + nouveaux usages).


DIfficultés à exprimer le contexte d'une assertion du fait de la réification. Donc peut adapté, pris tel quel, à exprimer des énoncés scientifiques.

Un sens partagé à l’échelle mondiale ? Origines néopositivistes du Web
sémantique à questionner (F. Rastier). Paradigme inadéquat aux sciences de
l’interprétation.

« Wo aber Gefahr ist, wächst Das Rettende auch. »
-->

## Problèmes identifiés lors de la conception d'une base de données pour la musicologie

<!--
 L’époque est au FAIR et au LOD. Afin que l’ouverture des données de la
recherche, leur interopérabilité et leur mise en relation avec des sources de
données tierces soient correctement traitées, il faut que ces questions soient
pensées très en amont des projets de recherche, et finement articulées aux
questions méthodologiques, voire scientifique.
▪ Il faut alors des ingénieurs et ingénieures qui « pensent » les données
conjointement avec les chercheurs et chercheuses, dans des situations de
travail où la technique ne joue pas un rôle ancillaire :
▪ Ces ingénieurs et ingénieures doivent jouer un rôle maïeutique (savoir poser
les questions, confronter le chercheur ou la chercheuse à des cas limites pour
l’amener à mieux comprendre ses objets d’étude).
▪ Le travail d’explicitation, de modélisation, des données doit avoir une fonction
heuristique : aider à révéler la structure interne des sources et des phénomènes
étudiés.
▪
🚨Les ressources d’ingénierie sont trop maigres, ce niveau dialogue est rare.


La FAIRisation des données musicologiques suppose une dynamique
informationnelle intellectuelle et technique entre les projets de BDD.
▪ Pour la bâtir, un réseau d’acteurs et d’actrices est nécessaire, mais :
▪ Il faut une complémentarité recherche/ingénierie/SIB car ces connaissances sont
très abstraites et difficiles à saisir.
▪ Les musicologues devant piloter de tels projet manquent d’informations claires
sur les enjeux scientifiques des méthodes et technologies disponibles pour
correctement modéliser les informations scientifiques. Ceci peut conduire à des
choix techniques inadaptés qui obèrent les possibilités scientifiques.
▪ Les profils techniques sont recrutés sur des contrats courts.
▪ Les prestataires n
’ont pas d’intérêt à s’inscrire dans les réseaux HN.
▪
🚨 Conséquemment, les connaissances d’ingénierie spécifiques à la
modélisation des données de la discipline sont peu capitalisées ; chaque
nouveau développement peine à bénéficier de l’expérience méthodologique
et conceptuelle acquise informellement au fil des projets passés.
-->

## Pourquoi utiliser une ontologie sémantique ?

<!--
▪ Formalisation d’un modèle conceptuel pour un domaine identifié proposant
des :
▪ Classes : types d’entités peuplant le domaine, possiblement organisées selon
des relations d’héritage (spécificité). On appelle individu une ressource qui est
du type d’une classe.
▪ Propriétés : aspects, caractéristiques, attributs possibles de ces classes, qui
peuvent soit pointer vers une valeur, soit vers un individu.
▪ Utiliser les classes et les propriétés d’une ontologie confère ainsi une
sémantique partagée aux données RDF (les individus identifiés par des
URL seront des sujets ou des objets, les propriétés des classes seront des
prédicats).
▪ Vous connaissez peut-être déjà une ontologie : SKOS (pour construire des
thésauri).
Permet de capitaliser des connaissances de modélisation d’un projet à l’autre
(démarche KM).
Permet de capitaliser des connaissances de modélisation d’un projet à l’autre
(démarche KM).
-->

## Qu'est ce que le CIDOC CRM et pourquoi l'utiliser ?

<!--
▪ Le CIDOC-CRM est une ontologie qui documente le patrimoine matériel et
immatériel ainsi que les processus de production de connaissances à son
propos.
▪ https://www.cidoc-crm.org/
▪ Venant du monde des musées, elle est désormais utilisée dans tous les
domaines des HN.
▪ Elle est extrêmement abstraite et générique.
▪ Ontologie centrée événement (nous y reviendrons dans les exemples…)
▪ Classes et propriétés : https://cidoc-crm.org/html/cidoc_crm_v7.1.2.html

Opinion : En dépit du nombre de classes centrées sur les usages de musées, le
CIDOC-CRM propose des classes génériques permettant de rendre compte de
l’ensemble des problématiques de modélisation de la structure et du contenu des
sources, ainsi que des processus analytiques qui les prennent pour cible.
-->

## Motifs de conception fondamentaux du CIDOC CRM

<!--
Nommer
Typer
Structurer les sources étudiées
Structurer les actions sous forme d'événements inscrits dans le temps. Le CRM encourage à ne pas penser les choses telles qu'elles sont mais plutôt les processus qui les ont amenées à être ce qu'elles sont. Ainsi, on ne dit pas

"For Philip Guston" dcterme:creator "Morton Feldman"

mais :

En cas de doute, il y a les E13 (knowledge creation process), toute production de connaissance est un événement, il devient donc possible de signer, dater, documenter les contributions, les rattacher à un contexte organisationnel plus vaste.

Ce qui est invisibilisé dans une base de données classique est ainsi explicité (le contexte de la cellule)

Ce pattern rend le Web sémantique plus conforme à l'expression de savoirs scientifiques (au prix d'une complexification du modèle)

Remarquez la finesse de
l’adressage…
Chaque élément constituant
le phénomène a son URL et
son identité.
-->

## Quelques mots sur des ontologies enfants du CIDOC CRM

<!--
LRMoo et la fleur
DOREMUS et les effectifs et programmes de concerts
-->

## Trois manières concrètes d'utiliser le CIDOC CRM dans votre projet

<!--
Un graphe de données ouvert est plus difficile à éditer que des données
relationnelles (données tabulaires s’éditant naturellement avec des formulaires
contraints).
▪ Le CRM est expressif, mais :
▪ Il existe parfois plusieurs manières de modéliser une situation avec les classes de base.
▪ Ses patterns fondamentaux (pour nommer, type, dater, annoter…) induisent beaucoup
de des sous-entités.
▪ Son caractère abstrait et générique fait écran avec la compréhension naturelle que l’on
pourrait avoir de nos données.
▪ En conséquence, une interface d’édition générique de données CRM n’a pas de
sens, car chaque collectif construit sa manière d’utiliser l’ontologie. Mais pourquoi
pas des outils de saisie paramétrés suivant des situations/pratiques spécifiques ?
-->

<!--
The Departure :
940 un peu plus que A#
810 entre G et G#
670 un peu plus que E
730 un peu moins que F#
-->