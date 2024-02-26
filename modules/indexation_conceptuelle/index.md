***NE PAS LIRE, WORK IN PROGRESS***

# Consortium Musica2, GT2 — Atelier du jeudi 12/10/2023 : Indexation conceptuelle et _Thesaurii_

## Présents

- Thomas Bottini, IE IReMus  
- Augustin Braud, IR Musica2 / IReMus  
- Théodora Psychoyou, MCF Sorbonne Université, Directrice de l'IReMus *(catalogage de manuscrits musicaux anciens à la BnF, catalogue de traités de musiques du XVIIe œuvres et sources, méta-index)*
- Nancy Hachem, Docteure en Musicologie  
- Nathalie Berthon-Blivet, IR IReMus *(a indexé une sélection d'articles parus dans le Mercure Galant avec le Référentiel de l'Ancien Régime qu'elle dirige)*
- Marco Gurrieri, IR IReMus  
- Jean-François Goudesenne, CR IRHT, depuis le 01/10 équipex Biblissima+ Cluster 6 patrimoins musical *(répertoire très spécifique, il peut y avoir des noms de compositeurs, des œuvres, de la transmission orale, thésauri, le concept d'œuvre est discuté)*
- Lucia Pasini, Post-doctorante Bern University of Applied Sciences *(histoire de la musique dodécaphonique suisse, refonte du répertoire de la mélodie française, importé dans Dezède)*
- Achille Davy-Rigaux, DR IReMus  
- Joann Elart, MCF Université de Rouen  
- Michela Berti, IR ERC PerformArt *(BDD 6000 transcriptions de documents et événements spectaculaires)*
- Louis Moreau-Gaudry, Ingénieur en éducation numérique, pôle ressource de la Philharmonie de Paris *(BDD documentaires physiques et numériques)*

## Préambule : la nécéssité de la désambiguïsation

Afin de lever le voile sur l'ambiguïté de certains termes au sein d'un _thesaurus_, la présence de musicologues responsables de corpus est nécessaire, bien qu'il s'agisse d'une activité chronophage par nature. On peut ensuite l'exploiter scientifiquement avec confiance.

La question des langues est également importante ; nous proposons d'annoter les références plus en détail en précisant la langue utilisée afin de pallier au manque implicite de connaissances des systèmes. Le format RDF gère nativement la localisation des données (les thésaurus implémentés en SKOS bénéficient donc de cette possibilité).

En ce qui concerne les personnes, il semble juste d'ajouter son ISNI à chaque personne citée (comme le fait Dezède, en imposant aux membres de sa communauté d'aller chercher les ISNI, ce qui implique des actions/documents de formation), afin d'éviter les problématiques liées aux différentes orthographes. On peut notamment évoquer l'exemple de Tchaïkovsky et les diverses écritures de son nom. Il faut également souligner la présence de l'ISNI sur Wiki EN, au contraire de Wiki FR.

## Enjeux scientifiques de l'indexation ?

### Fonctions possibles de l'indexation

Durant cette séance d'atelier, nous avons fait émerger un ensemble d'opérations mentales et techniques sur lequel s'appuie le travail scientifique, qui convoquent la notion d'indexation :

- ***Indexer pour décrire.*** La ressource d'indexation revêtent ici le rôle de caractériser la ressource indexée, par exemple à des fins de synthèse ou de représentation synoptique des thématiques d'un corpus.
- ***Indexer pour rendre fouillable.*** Les ressources d'indexation constituent ici des éléments d'interface avec lesquels l'utilisateur peut interagir pour effectuer une recherche au sein des corpus.
- ***Indexer pour défricher un corpus.*** Les ressources d'indexation permettent d'asseoir une progression dans la découverte d'un corpus à l'occasion du premier contact en fournissant une unification de ce qui a déjà été rencontrée (activité synthétique au fil de l'eau). Exemple d'un corpus vaste, impossible à appréhender, dans lequel une personne peut apparaître 25 fois mais sous des noms différents (ou sous des noms présentant des graphies différentes). Ici l'indexation fédère le divers, elle est indispensable pour pouvoir se repérer (logique du Petit-Poucet).
- ***Indexer pour se repérer.*** Les ressources d'indexation sont des petits cailloux blancs permettant au lecteur-Petit Poucet de ne pas se perdre dans son corpus. Elles constituent des marque-page sémantiques.
- ***Indexer pour analyser.*** Les ressources d'indexation constituent une réserve de concepts analytiques qui, distribués sur les sources, en explicitent le sens. L'activité d'indexation n'est pas qu'une activité de redocumentarisation, elle est également une activité scientifique convoquant des interprétant, un cadre théorique, une méthodologie. Les pratiques d'indexation relevant de cet aspect soulignent la nécessiter de signer les annotations d'indexation produites.
- ***Indexer pour faire des statistiques.*** Ceci est un usage plus spécifique de l'indexation à finalité synthétique.
- ***Indexer pour créer une circulation hypertextuelle à l'intérieur des corpus même.*** Ici, l'indexation se positionne comme pratique éditoriale, la ressource d'indexation jouant le rôle de point de passage d'un document à l'autre.
- ***Constituer des thésaurii/référentiels pour analyser.*** L'activité de conception d'un thésaurus ou d'un référentiel d'entités récurrentes est à considérer comme une pratique scientifique et non seulement documentaire, car le système d'organisation des connaissances qui en résulte est un point de vue sur la teneur des savoirs (conceptuels, lexicaux…) convoqués dans l'analyse des sources, c'est une méta-connaissance.
- ***Indexer pour décrire des sources ou des œuvres.*** (cf. exemple de l'indexation des airs du Mercure Galant).

### Fonctions importantes

- Signer une indexation pour exprimer la responsabilité scientifique. Une indexation ne doit pas être vue comme une simple opération de redocumentarisation anonyme, mais comme une opération interprétative située. Note d'implémentation : avec des E13 du CRM, chaque indexation étant vu comme un événement d'apport de connaissance signé/daté/contextualisé.

## Retours sur les pratiques

### Le cas du Mercure Galant

Deux cas de figure :

1) Pour le corpus d'airs : décrire la musique (compositeur, librettiste, réseaux d'attribution, retrouver l'œuvre : incipit musical et littéraire, éléments de description : tonalité, forme, genre).
2) Pour le corpus de textes : il s'agit d'une masse énorme de texte, qu'il faut pouvoir rendre fouillable. Pour savoir quoi en tirer, il a fallu indexer les personnes, les lieux, les mots-clefs (thématiques abordées par l'auteur de l'article). Chaque article est indexé par une personne et livre l'analyse de cette personne. l'indexation permet ici de créer une circulation à l'intérieur du corpus même.

L'indexation doit cibler une liste de données indexables factuellement descriptible pour "défricher un terrain" et organiser une grande quantité d’informations concernant leurs sources :

- les personnes
- les lieux
- les mots-clés & mots-matières
- les thématiques
- informations liées à la notice, la conservation, à l’exemplaire exact, _etc_.

Il est également important de souligner que chaque point est indexé par une personne et que cela doit être explicite ; dans le cas d'usage de l'ontologie Cidoc-CRM, on systématisera l'usage d'un E13. Ces précisions sont tout particulièrement utiles compte-tenu de la circulation au sein du corpus-même de concepts, d'un réseau d'index et des textes dense qui porte de nombreux renvois internes.

Comme abordé en préambule, on observe une vrai nécéssité de contrôler pour des corpus limités ; l'assemblée propose un consensus humainement possible pour un maximum de 2000 sources. Le travail d’identification requiert en effet une véritable expertise. En exemple, les personnes ne sont pas toujours citées par leurs noms et leur identification requiert une identification historiographique fine, par exemple : le Duc, le Marquis, _etc_... Ces titres changent très régulièrement. La nécéssité d’offrir un outil cumulatif où chacun peut consulter les ressources issuees des recherches précédentes est également mentionnée.

## **_Définition de termes importants :_**  

### _Thesaurii :_  

Les _thesaurii_ portent soit des mots, soit des concepts. Il se pose alors notamment la question de la polysémie, où l'on fait souvent face au fait que deux auteurs utilisent des termes similaires pour deux choses très différentes (l'exemple de « cadence » est cité); le contexte permet de déterminer le sens. Le mot n’est ainsi jamais univoque. Les _thesaurii_ présentent de manière intrinsèque un aspect arborescent. Un terme peut avoir plusieurs parents et apparaître à différents endroits, un noeud peut avoir plusieurs parents ; un _thesaurus_ n’a donc de sens que pour ce que pour quoi il a été conçu.

Faut-il ainsi faire appel à plusieurs _thesaurii_ pour un meme mot ou bien intégrer plusieurs définitions dans un seul _thesaurus_? Les _thesaurii_ possèdent par ailleurs un aspect arborescent ; un terme peut avoir plusieurs parents et apparaître à différents endroits, un noeud peut avoir plusieurs parents, etc... L'expression du doute étant fondamentale dans notre travail, nous avons besoin de E13 pour informer des choix et de leur nature. 

Le principal problème des _thesaurii_ est le fait qu'ils ne soulignent pas clairement les aspects génétiques et diachroniques. Il n'y a en effet pas de sens de constituer un thesaurus avant de mettre le nez dans les sources ; l'assemblée emploi l'expression d'un « couteau affuté au fur et à mesure de son usage », un parallélisme tempéré par l’expérience de la recherche. Un enjeu pour la constitution de futurs _thesaurii_ est leur publication avec les usages leur correspondant, en considérant la possibilité d'une cartographie de la transmission, avec à nouveau l'usage de E13. La tradition orale (acceptation de l'attribution d'une source, _etc_) empêche parfois l'information d'être traitée de la bonne manière et peut même mener jusqu'à l'anachronisme, en utilisant des outils récents pour commenter le passé.

### _Vocabulaire contrôlé :_  

Il s'agit d'une circonscription du vocable indiquant à l’utilisateur des termes définis au sein de l’outil au contraire d'un champ de texte libre. 

L'assemblée souligne le problème de cas limites présentant une non-correspondance entre mots et concepts, en prenant l'exemple de "partition" qui ne correspond pas au concept et peut donc soulever des problèmes d’attribution. Il est donc nécessaire de régulièrement remettre à jour ces vocables, en veillant à l’anachronisme de l'usage d'outils récents pour commenter le passé.

### _Ontologie :_  

L'ontologie permet de se doter d’une définition formelle des concepts, et d'exprimer ce qui est irréductible à la teneur conceptuelle. Par l'usage de l'analyse et  modélisation ontologique, on peut décrire l'intérieur-même des concepts et viser une perception fine de la teneur des choses.

### _Référentiel :_   

Organisation devant être reconnue par un nombre suffisant de membres de la communauté scientifique pour attester de son statut de référence. Ceci est atteint par une confiance donnée à l’institution qui porte le référentiel, un nombre suffisant d'alignements, _etc_. Il est par ailleurs possible pour un même objet de s'inscrire dans plusieurs référentiels qui ne correspondent pas forcément ; le choix de l'outil est absolument situationnel.

## Quels outils pour indexer ?

Nous présentons ici divers référentiels intéressants, ayant été expertisés par un ingénieur et/ou développeur et présentant une pérennité prouvée sur les plans techniques tout autant que scientifiques. 
- ISNI pour les personnes.
- En ce qui concerne les instruments, Mimo semble incontournable et est utilisé par la Philharmonie de Paris.
- Pour les lieux il existe un grand nombre de possibilités : Cassini, Geonames, Google...
- Il est fait état du manque d'un référentiel pour le recueil d’œuvres 

L'assemblée souligne que la part de subjectivité mise en œuvre va jouer sur la profondeur de l’analyse et du détail ; il faut donc accepter de devoir s’arrêter à un moment lors du processus analytique. L‘indexation est définie par le cadre méthodologique dans lequel elle s'inscrit.

- - - 




Base de données peut ne pas être rangée, rassemblement de données sans supposer le fait qu’elles soient écrites, etc. 

Référentiel doit être reconnu par suffisamment de personnes pour attester de son statut de référence ; question de confiance à l’institution qui la porte, question des alignements.
Pour un même objet on peut avoir plusieurs référentiels qui ne correspondent pas forcément : Cassini, Geonames, Google / savoir lequel choisir est difficile.

Expression du doute est fondamentale dans notre travail

Quels référentiels ?

Un bon référentiel a été expertisé par un ingénieur / développeur, la pérennité est nécessaire (plan technique)
CM2 pourrait soutenir Mimo pour les instruments ? ISNI pour les personnes
Il manque un référentiel pour le recueil d’œuvres 
Le référentiel s’impose quand un objet a différentes formes.

Mimo : deux référentiels etc : au-delà du référentiel principal, on relie un second thesaurus qui trie les familles par cordes/percus/claviers, trois niveaux de profondeur / 10/12 langues, sert de point d’entrée pour les musées qui veulent rajouter leur collection dans le catalogue et doivent s’aligner sur le thesaurus de Mimo

Theo ; la subjectivité va jouer sur la profondeur de l’analyse et du détail, il faut accepter de s’arrêter à un moment / penser aux index-matières du RILM 
une partie du périmètre peut être pensée en amont



Livrable conjoint entre GT2 et GTZZ ; personne référence pour faire des pivots et remplissage d’un graphe du consortium en ajoutant des données
Serveur Humanum pour Mimo, lien avec la Philharmonie, facade prouvant que plusieurs jeux de données peuvent être mis en commun conformité nécessaire avec data bnf
Livrable donnant des exemples d’usage des API des référentiels 

Christophe Corbier / Projet Perso : enregistrements grecs sur rouleaux ayant inspiré Ravel etc / question du sonore ? Gestion du corpus, re-documentation et volet analytique, il faut construire un thesaurus qui n’existe pas encore donc difficile. Pas de mise en ligne tant qu’un accord n’est pas trouvé


