# Consortium Musica2, GT2

## Atelier du jeudi 12/10/2023 : Indexation conceptuelle et _Thesaurii_

Présent·e·s :

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

Durant cette séance d'atelier, nous avons fait émerger un ensemble d'opérations mentales et techniques sur lequel s'appuie le travail scientifique, qui convoquent la notion d'indexation :

- Indexer pour décrire. La ressource d'indexation revêtent ici le rôle de caractériser la ressource indexée, par exemple à des fins de synthèse ou de représentation synoptique des thématiques d'un corpus.
- Indexer pour rendre fouillable. Les ressources d'indexation constituent ici des éléments d'interface avec lesquels l'utilisateur peut interagir pour effectuer une recherche au sein des corpus.
- Indexer pour défricher un corpus, à l'occasion du premier contact. Les ressources d'indexation permettent d'asseoir une progression dans la découverte d'un corpus en fournissant une unification de ce qui a déjà été rencontrée (activité synthétique au fil de l'eau).
- Indexer pour se repérer. Les ressources d'indexation sont des petits cailloux blancs permettant au lecteur-Petit Poucet de ne pas se perdre dans son corpus. Elles constituent des marque-page sémantiques.
- Indexer pour analyser. Les ressources d'indexation 


L'indexation doit cibler une liste de données indexables factuellement descriptible pour "défricher un terrain" et organiser une grande quantité d’informations concernant leurs sources :

- les personnes
- les lieux
- les mots-clés & mots-matières
- les thématiques
- informations liées à la notice, la conservation, à l’exemplaire exact, _etc_.

Il est également important de souligner que chaque point est indexé par une personne et que cela doit être explicite ; dans le cas d'usage de l'ontologie Cidoc-CRM, on systématisera l'usage d'un E13. Ces précisions sont tout particulièrement utiles compte-tenu de la circulation au sein du corpus-même de concepts, d'un réseau d'index et des textes dense qui porte de nombreux renvois internes.

Comme abordé en préambule, on observe une vrai nécéssité de contrôler pour des corpus limités ; l'assemblée propose un consensus humainement possible pour un maximum de 2000 sources. Le travail d’identification requiert en effet une véritable expertise. En exemple, les personnes ne sont pas toujours citées par leurs noms et leur identification requiert une identification historiographique fine, par exemple : le Duc, le Marquis, _etc_... Ces titres changent très régulièrement. La nécéssité d’offrir un outil cumulatif où chacun peut consulter les ressources issuees des recherches précédentes est également mentionnée.

### **_Définition de termes importants :_**  

#### _Thesaurii :_  

Les _thesaurii_ portent soit des mots, soit des concepts. Il se pose alors notamment la question de la polysémie, où l'on fait souvent face au fait que deux auteurs utilisent des termes similaires pour deux choses très différentes (l'exemple de « cadence » est cité); le contexte permet de déterminer le sens. Le mot n’est ainsi jamais univoque. Les _thesaurii_ présentent de manière intrinsèque un aspect arborescent. Un terme peut avoir plusieurs parents et apparaître à différents endroits, un noeud peut avoir plusieurs parents ; un _thesaurus_ n’a donc de sens que pour ce que pour quoi il a été conçu.

Faut-il ainsi faire appel à plusieurs _thesaurii_ pour un meme mot ou bien intégrer plusieurs définitions dans un seul _thesaurus_? L'expression du doute étant fondamentale dans notre travail, nous avons besoin de E13 pour informer des choix et de leur nature. 

Le principal problème des _thesaurii_ est le fait qu'ils ne soulignent pas clairement les aspects génétiques et diachroniques. Un enjeu pour la constitution de futurs _thesaurii_ est leur publication avec les usages leur correspondant, en considérant la possibilité d'une cartographie de la transmission, avec à nouveau l'usage de E13. La tradition orale (acceptation de l'attribution d'une source, _etc_) empêche parfois l'information d'être traitée de la bonne manière et peut même mener jusqu'à l'anachronisme, en utilisant des outils récents pour commenter le passé.

En ce qui concerne les informations de localisation, on s'entend sur trois critères importants, la provenance, l'usage et l'origine. 

#### _Vocabulaire contrôlé :_  

Il s'agit d'une circonscription du vocable indiquant à l’utilisateur des termes définis au sein de l’outil au contraire d'un champ de texte libre. 

#### _Ontologie :_  

L'ontologie permet de se doter d’une définition formelle des concepts, et d'exprimer ce qui est irréductible à la teneur conceptuelle. Par l'usage de l'analyse et  modélisation ontologique, on peut décrire l'intérieur-même des concepts et viser une perception fine de la teneur des choses.

#### _Référentiel :_   

Organisation devant être reconnue par un nombre suffisant de membres de la communauté scientifique pour attester de son statut de référence. Ceci est atteint par une confiance donnée à l’institution qui porte le référentiel, un nombre suffisant d'alignements, _etc_. Il est par ailleurs possible pour un même objet de s'inscrire dans plusieurs référentiels qui ne correspondent pas forcément ; le choix de l'outil est absolument situationnel.

## Quels outils pour indexer ?

Nous présentons ici divers référentiels intéressants, ayant été expertisés par un ingénieur et/ou développeur et présentant une pérennité prouvée sur les plans techniques tout autant que scientifiques. 
- ISNI pour les personnes.
- En ce qui concerne les instruments, Mimo semble incontournable et est utilisé par la Philharmonie de Paris.
- Pour les lieux il existe un grand nombre de possibilités : Cassini, Geonames, Google...
- Il est fait état du manque d'un référentiel pour le recueil d’œuvres 

L'assemblée souligne que la part de subjectivité mise en œuvre va jouer sur la profondeur de l’analyse et du détail ; il faut donc accepter de devoir s’arrêter à un moment lors du processus analytique. L‘indexation est définie par le cadre méthodologique dans lequel elle s'inscrit.





