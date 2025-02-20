# Introduction. Pourquoi et comment utiliser une ontologie dans la conception d'une base de données pour la musicologie ?

## Caractérisation d'une base de données pour la musicologie

Avant de montrer en quoi les technologies et méthodologies du Web sémantique et de l'ontologie CIDOC CRM peuvent être fécondes pour la conception de bases de données pour la musicologie, nous présentons un certain nombre de caractéristiques importantes de ces dernières, qui les différencient d'autres types de bases de données.

### Hétérogénéité des sources documentaires et adressabilité interne

La musicologie est une discipline qui étudie le contenu et le contexte de sources de natures très diverses : musique notée, textes théoriques, contenus iconographiques, informations consignées dans des registres, documents administratifs textuels, enregistrements sonores, vidéos, etc. Ces pratiques se prolongent naturellement en milieu numérique, et se conduisent actuellement autour d'objets tels que les fichier [XML MEI](https://music-encoding.org/), [XML TEI](https://tei-c.org/), fichier [images matricielles](https://fr.wikipedia.org/wiki/Image_matricielle), fichiers audio et/ou vidéo, données textuelles structurées (aux formats [XML](https://fr.wikipedia.org/wiki/Extensible_Markup_Language), [SQL](https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_relationnelle), [RDF](https://fr.wikipedia.org/wiki/Resource_Description_Framework), [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation), etc.).

Ainsi les bases de données de la musicologie contiennent-elles bien souvent des connaissances produites à propos des sources. Afin que ces données puissent faire sens, il faut que leur articulation aux sources soit précise. Pour exemples, une donnée d'analyse musicale devra renvoyer avec précision à l'observable qu'elle qualifie sur la partition (une note, un accord, une phrase, une cadence, etc.), des données transcrivant et annotant une entrée dans un registre devront pointer précisément l'exemplaire, la page et la section auxquels elles se rapportent, une annotation portant sur un détail d'une image devrait pouvoir circonscrire précisément le fragment visuel concerné, etc. Nous nommons adressabilité la capacité technique d'un système d'information permettant d'identifier, de désigner sans ambiguïté et de rendre accessible (« adresser ») un fragment au sein d'un contenu. La possibilité de rendre adressable les fragments afin d'y articuler un commentaire critique constitue une des clef de voûte technique des mondes lettrés, et cette préoccupation cheville l'histoire des supports d'écriture :

> *« Alors que le haut Moyen Âge ne connaissait que de modestes subdivisions du texte, reposant moins sur des signes spécifiques que sur des ornements (rehaussement des lettres initiales par la couleur, changements d’écriture, décorations diverses), on passe à un véritable système de techniques auxiliaires de la lecture et de la consultation du livre, destinées à identifier rapidement le passage que l’on recherche : rubrication, découpage en paragraphes, titres de chapitre, séparation du texte et du commentaire, sommaires, tables des concordances des termes, index et tables analytiques alphabétiques. »*
> 
> (Guglielmo Cavallo & Roger Chartier, *Histoire de la lecture dans le monde occidental*, Points Histoire, 2001)

Dans le champ des systèmes d'information Web, et notamment, comme nous allons le voir, des bases de données scientifiques publiées sur le Web, les enjeux techniques autour de l'adressabilité des sources se traduisent par des questions de mise à disposition en masse des sources numérisées accompagnées de la capacité à générer une [URL](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) pour chaque fragment qu'un chercheur pourrait vouloir pointer ou annoter. Dans le périmètre technique des sources musicales ou textuelles encodées en XML (MEI et TEI), l'enjeu est de rendre les fragments XML [identifiés de manière unique de manière interne au sein des fichiers](https://www.w3.org/TR/2005/REC-xml-id-20050909/) adressables sur le Web via des URL. Pour ce qui concerne les images matricielles, le standard [IIIF](https://iiif.biblissima.fr/) réalise une adressabilité totale de n'importe quel fragment rectangulaire sous la forme d'URL.

Ce sont l'accessibilité et l'adressabilité conjointe des fragments des sources et des données critiques qui s'y rapportent qui constituent la base d'un système d'information scientifique sur le Web.

### Captation du travail critique sur les sources et du contexte scientifique

Un des critères que l'on peut donner pour fonder le caractère scientifique d'une donnée — entendue ici comme le supplément critique qu'apporte le chercheur ou la chercheuse à la source — est que celle-ci doit être accompagnée d'informations qui contextualisent sa production, telles que :

- **L'auteur et la date.** À l'instar d'une entrée dans un cahier de laboratoire, toute contribution scientifique doit être *signée* et *datée*.
- **La teneur de l'opération critique exécutée.** Lorsqu'un organologue identifie un instrument de musique sur une peinture, il ne s'agit pas pour le concepteur de la base de données de stocker uniquement un lien entre le fragment d'image et l'identifiant du concept dénotant le type de l'instrument repéré, il faut également stocker le type du geste analytique réalisé, ici, « Identification visuelle d'instrument de musique » (par exemple). C'est la sémantique de l'opération critique qui donne du sens au lien existant entre le fragment de source annoté et le contenu de l'annotation ; autrement dit, quand deux éléments sont connectés (ici, un fragment de source et une annotation), encore faut-il spécifier à quel titre ils le sont.
- **L'explicitation du contexte interprétatif.** Un travail de production de connaissances s'effectue dans un contexte scientifique explicite. Ainsi, il s'effectue dans la perspective de répondre à une question de recherche, le corpus sur lequel il porte a été constitué selon des critères explicites, il convoque des éléments théoriques et se réfère à des sources identifiables pour construire son argumentation, il s'accomplit dans un cadre socio-scientifique (projet, équipe, institution, etc.), etc.
- Et bien entendu, l'adressage fin du fragment de la source sur lequel elle porte (cf. *supra*).

L'ensemble de ces éléments définissant le contexte interprétatif contribuent à rendre compréhensibles et réutilisables *ailleurs et plus tard* des données produites *ici et maintenant*.

### Structuration et partage des connaissances utilisées pour analyser les sources

Les données avec lesquelles sont annotées les sources peuvent être soit créées *ad-hoc* (par exemple, la transcription d'un passage lu sur une source ancienne) soit être piochées dans des [référentiels](https://fr.wikipedia.org/wiki/R%C3%A9f%C3%A9rentiel) existants (par exemple, un compositeur attribué à une partition manuscrite). Un référentiel « constitu[e] (…) un ensemble d’informations structurées (…) liée[s] à un champ de connaissance spécifique, en vue d'une application systématique ». Il peut s'agir de termes et de concepts réunis dans un [thésaurus](https://fr.wikipedia.org/wiki/Th%C3%A9saurus_documentaire), dont la fonction première est d'organiser le lexique d'un domaine via des relations de type « terme générique/terme spécifique » afin de fournir des ressources pour l'indexation thématique ou l'annotation conceptuelle de documents (tels que le [Getty AAT](https://www.getty.edu/research/tools/vocabularies/aat/), les [vocabulaires du Ministère de la Culture et de la Communication](http://data.culture.fr/thesaurus/page/vocabulaires), [Iconclass](https://iconclass.org/), etc.). Dans le contexte du Web sémantique, on recourt à l'ontologie [SKOS](https://fr.wikipedia.org/wiki/Simple_Knowledge_Organization_System) pour exprimer les thésaurus et à des outils de gestion tels qu'[Opentheso](https://opentheso.huma-num.fr/). Il peut également s'agir de bases de données de personnes, lieux, œuvres, institutions, etc. (telles ques [VIAF](https://viaf.org/), [data.bnf.fr](https://data.bnf.fr/), [ISNI](https://isni.org/), [Geonames](https://www.geonames.org/), [Wikidata](https://www.wikidata.org/), [RISM](https://rism.online/)).

Recourir à des référentiels établis, les enrichir, ou constituer de nouveaux référentiels sont des ressorts majeurs dans le partage et l'évolution des données scientifiques sur le Web. Concrètement, pointer vers des URL telles que [data.bnf.fr/fr/ark:/12148/cb13899342r](https://data.bnf.fr/fr/ark:/12148/cb13899342r), [catalogue.bnf.fr/ark:/12148/cb13899342r](https://catalogue.bnf.fr/ark:/12148/cb13899342r), [viaf.org/en/viaf/7575200](https://viaf.org/en/viaf/7575200) ou [www.wikidata.org/wiki/Q150445](https://www.wikidata.org/wiki/Q150445) plutôt que d'écrire *« Camille Saint-Saëns »* dans la base de données offre un certain nombre d'avantages pratiques et méthodologiques : désambiguïsation, possibilité d'une automatisation de la récupération des données déjà collectées par les institutions (catalogue des œuvres, formes rejetées du nom, dates, éléments biographiques, etc.) si une [API](https://fr.wikipedia.org/wiki/Interface_de_programmation) publique existe, alignement entre les bases scientifiques, etc. Chacun de ces apports repose sur la mise en œuvre technique de la notion d'adressabilité des données des référentiels via des URL publiques.

## Le Web sémantique comme milieu idéal pour la publication des données de la recherche

Le paysage « juridico-scientifio-socio-technique » a évolué depuis les premières heures des bases de données en musicologie. La [loi du 7 octobre 2016 pour une  République numérique](https://www.economie.gouv.fr/files/files/PDF/DP_LoiNumerique.pdf) établit le *« [l]ibre accès aux résultats des travaux de recherche publique »* afin de *« [l]ibérer l'innovation en faisant circuler les informations et les savoirs »*. Cette loi place les [principes FAIR](https://www.ccsd.cnrs.fr/principes-fair/) et les notion d'[Open Data](https://5stardata.info/fr/) et de [données ouvertes et liées](https://fr.wikipedia.org/wiki/Linked_open_data) au cœur des impératifs pratiques des projets de recherche (voir aussi la notion de [plan de gestion des données](https://doranum.fr/plan-gestion-donnees-dmp/)).

Le milieu technique le plus efficient pour fonder techniquement ces objectifs est le *Web sémantique*. Le Web initial, [inventé par Tim Berners-Lee en 1991](https://fr.wikipedia.org/wiki/Histoire_d%27Internet), est un Web de documents liés obéissant au paradigme de la bibliothèque : chaque document — ou page Web — est accessible à une adresse (URL) donnée et est destiné à être lu par un humain (sa structure typodispositionnelle étant décrite en [HTML](https://fr.wikipedia.org/wiki/Hypertext_Markup_Language)), l'ensemble des pages Web formant un réseau [hypertexte](https://fr.wikipedia.org/wiki/Hypertexte) (terme qui prédate le Web de 26 ans). Complémentairement, le Web sémantique obéit au paradigme de la base de données, et peut être vu comme la promesse d'une base de données à l'échelle du Web. L'unité informationnelle n'est plus la page Web, mais la donnée, exprimée sous la forme d'un triplet sujet/prédicat/objet. Le sujet est ce sur quoi porte l'information, l'objet est l'information liée, et le prédicat établit la teneur du lien entre la donnée enrichie (le sujet) et l'enrichissement (l'objet). Par exemple, la connaissance « Camille Saint-Saëns est le créateur de l'œuvre pour piano *Feuillet d'album, opus 169* » peut se traduire par le triplet :

    sujet    : https://data.bnf.fr/fr/ark:/12148/cb139515641
    prédicat : http://purl.org/dc/terms/creator
    objet    : https://data.bnf.fr/fr/ark:/12148/cb13899342r

L'URL qui constitue le sujet de ce triplet représente l'œuvre intitulée *Feuillet d'album, opus 169* telle qu'elle est cataloguée sur [data.bnf.fr](https://data.bnf.fr/). L'URL qui constitue l'objet représente Camille Saint-Saëns tel qu'il est référencé sur le même site. L'URL qui constitue le prédicat dénote le concept de créateur au sens du vocabulaire générique [Dublin Core](https://fr.wikipedia.org/wiki/Dublin_Core), très commun dans le monde du Web sémantique (mais dont la simplicité n'en fait pas un bon candidat pour décrire des données scientifiques). Voici un autre exemple :

    sujet    : https://db.ridim.org/display.php?ridim_id=5193
    prédicat : http://www.cidoc-crm.org/cidoc-crm/P138_represents
    objet    : http://www.mimo-db.eu/InstrumentsKeywords/3668

Ce deuxième triplet exprime que la peinture dont le titre est *Potted pine tree and koto* telle qu'elle est cataloguée par le RIDIM *représente* un koto. Le concept de koto est ici pioché dans le thésaurus international des instruments de musique [MIMO](https://vocabulary.mimo-international.com/InstrumentsKeywords/). Remarquons également que la fixation du sens du verbe *représente* est confié à l'ontologie CIDOC CRM (ce sens est accessible en déréférençant sur l'URL représentant le prédicat).

Ainsi, l'acte de production de connaissance est entièrement explicité : on sait avec précision ce dont on parle, ce qu'on en dit, et sous quelle modalité. Remarquons également que la connexion des triplets forme un graphe. La levée des ambiguïtés est assurée par le recours à des URL qui identifient les objets sur le Web. C'est d'ailleurs en cela que le Web sémantique est sémantique : le *sens* est partagé (à la fois celui des données, mais également celui des modalités qui les connectent via les prédicats). Pour cette raison, le Web sémantique constitue le milieu socio-technique idéal pour exprimer des données FAIR (cf. *supra*) pour l’expression et la diffusion des données de la recherche. Les graphes créés avec les technologies du Web sémantiques sont couramment désignés comme étant des « graphes de connaissances » (*knowledge graphs*). L'expression des triplets du Web sémantique est confiée à un langage de description, le [RDF](https://fr.wikipedia.org/wiki/Resource_Description_Framework).

<!--
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
https://fr.wikipedia.org/wiki/Ontologie_(informatique)

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

<style>
    * {
        cursor: default;
        font-family: monospace;
        font-size: 95%;
    }

    a {
        color: aquamarine;
    }

    a:hover {
        color: deeppink;
        text-decoration: none;
    }

    h1, h2, h3, h4, h5, h6 {
        color: darkturquoise;
        font-weight: normal;
    }
</style>