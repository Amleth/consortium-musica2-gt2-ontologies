## 1. Présentation générale de l'approche méthodologique

Ce document vise à proposer un protocole détaillé de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques. Notre objectif visera à améliorer la précision et l'interopérabilité des données par le recours au modèle FRBR. 

Les besoins de l'édition critique textuelle se sont historiquement structurés à partir de deux modèles philologiques historiquement importants. Le premier d'entre eux, que l'on doit à l'allemand Karl Lachmann (1793 - 1851), s'articule en cinq points, en débutant par la première étape de la _recensio_, soit l'identification des sources, l'étude de la tradition. À ce stade, il s'agit de différencier les sources de _tradition directe_ - le manuscrit autographe, aussi nommé _omega_- et les sources de _tradition indirecte_, les traductions, citations, commentaires et parodies. Une fois cette première étape terminée, la seconde partie de la _recensio_ peut s'effectuer afin de compléter l'identification des sources. La troisième partie de la méthode est la _collatio_, qui consiste en un recensement complet des sources, avant de démarer une étape plus critique, l'_eliminatio codicum descriptorum_, qui consiste à éliminer les copies ou sources trop semblables, afin de constituer un corpus cohérent et propice au _stemma codicum_, la dernière étape du processus consistant en la détermination de la relation entre les sources. Cette dernière étape permet l'établissement d'un tableau généalogique des sources constituant une même œuvre.

La seconde méthode établie par Joseph Bédier (1864-1938) critique fondamentalement la méthode de Lachmann : le _stemma codicum_ aboutit dans la majorité des cas à une division systématique de l'_omega_ (autographe) en deux branches. Ce résultat est dû à la binarité inhérente à la logie formelle de la méthode de Lachmann, aisément visibile dans les liens tracés entre deux exemplaires : si une erreur est commune à deux exemplaires, ces derniers sont forcément mis en relation d'une manière binaire (oui ou non) et éliminent la possibilité d'une analyse plus détaillée. Selon Bédier, le résultat du _stemma codicum_ est alors toujours banalisé, au contraire d'une vision plus fine et complexe du phénomène réel où l'on aurait plus de branches. Le second problème soulevé par Bédier est lié au document résultant de la comparaison des sources : il en ressort un document n'ayant jamais eu une quelconque existence réelle, issus de conjectures établies autour d'archétypes et de sources fantasmées, et concaténant diverses sources en une production philologique, plutôt que de se pencher vers une source véritable. Pour Bédier, le seul bon outil développé par Lachman est lié aux deux premiers points - les deux étapes de la _recensio_ - qui doivent être réalisés afin d'imaginer correctement effectuer un travail d'édition critique. Cette méthode, également dite du _bon manuscrit_ vise à choisir d'emblée la source la moins corrompue afin qu'elle constitue la base de l'édition critique ; les éventuelles erreurs seront corrigées au fur et à mesure du processus par les déductions du philologue. Cette méthode est particluièrement pertinente dans le cas d'un nombre réduit de sources. Par exemple, dans le cas d'un Opéra le _bon manuscrit_ est celui utilisé lors de la première représentation, à partir duquel on travaille ensuite. Prenons comme exemple le _Don Giovanni_ de Mozart : entre la version de Prague (création) et la version de Vienne qui connait, l'œuvre connait  de nombreux ajouts. La version de Venise est quant à elle hybride... D'où la nécessité d'un point de départ clair.

Bien que ces deux modèles soient les plus importants, il existe également une troisième méthode "synthétiste" imaginée par Giorgio Pasquali (1885-1952) ; moins critique avec Lachmann, sa méthode  hybride les apports des deux précédentes en maintenant la version de Lachmann, tout en prenant en compte les critiques de Bédier. Une dernière école est celle du _Copy-text_, notamment utilisée par Philip Gossett (1941-2017) dans le cadre de l'édition critique des opéras de Rossini.

Dans le cadre de la présentation de notre protocole de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques, nous prenons donc comme point d'appui les deux modèles philologiques "historiquement importants" que sont la méthode Karl Lachmann et méthode Joseph Bédier. La convergence des deux méthodes nous offre ainsi un socle pour entrevoir les éléments à renseigner en utilisant les éléments du header MEI représentant des entités FRBR.

## 2. Approche des GT1 et GT2 pour la complétion des header MEI

L'appui sur les normes FRBR nous parait central, afin de combler une lacune dans l'interopérabilité des données de fichiers encodés en MEI. Dans le cadre de l'usage des normes FRBR en MEI, il est ainsi primordial que la liste des œuvres, des expressions, des manifestations puis des items corresponde de manière fine à la _recensio_ ; le header doit être rempli de la manière la plus complète et rigoureuse possible. Notre protocole étant orienté vers la redondance, il est ainsi probable que des métadonnées soient régulièrement répétées, par exemple le nom du compositeur que nous renseignerons une dizaine de fois.

Nous détaillons ci-dessous notre protocole en prenant appui sur le modèle des _guidelines_ MEI, afin d'en faciliter l'approche. Notons que des exemples concrets sont joints au sein du _repository_, ainsi qu'un modèle vierge qui pourra être copié et rempli au sein des headers des utilisateurs, pour une interopérabilité maximale. 

- _meiHead_
   - Tittle stat etc
- _fileDesc_
   - Tous les éléments
- _sourceDesc_ Ce module est l'élément central de notre protocole, puisque qu'il s'agit de la partie où nous décrivons de manière exacte le contenu scientifique. Selon les _guidelines_ MEI, il n'y a pas de renvoi au modèle FRBR au sein de _workList_. Il faut donc déployer le modèle FRBR à cet endroit.
   - _expressionList_ : il s'agit de nommer et détailler les différentes expressions. Nous avons fait le choix de nommer l'expression de tradition directe _expression 0_. Les expressions indirectes se déploient ensuite avec des chiffres (1,2 _etc_) ou bien des noms en toutes lettres.
   - _manifestationList_ : de manière similaire à _expressionList_, nous nommons le manuscrit autographe (ou l'_omega_ issu du _stemma codicum_ si l'on ne possède pas l'autographe) _manifestation 0_. Pour chaque expression il convient d'utiliser une isntance de _manifestationList_ et pour chaque manifestation un _itemList_. Dans le cadre de manuscrits, la manifestation et l'item ne font qu'un. 
   - Le fichier MEI que nous sommes en train de renseigner est par ailleurs une autre manifestation de l'œuvre, et doit par conséquent faire partie de la _manifestation_list_.
- Mettre des xmlID pour manifestation et item, cf manif 0 ; il faut que l'on trouve une manière de nommer les choses / un item ne peut pas être 0
- Nomenclature ? Chacun s'organise, mais on essaie de respecter la tradition et la nomenclature








L'important pour notre protocole est **l'interopérabilité** / faire communauté et permettre la vérification, par exemple dans le cas d'éditions critiques
**L'expression dans notre protocole correspond à la _recensio_ : discours commun aux deux théories**
- Expression origniale : tradition directe
- Parodies, transcriptions, citations etc : tradition indirecte


- Paragraphe final pour maintenir la section _source_desc_ auprès de la communauté MEI car il permet d'exprimer au mieux, document considéré comme un "manifeste méthodologique".

- Trouver un cas où on a pas l'autographe mais où on l'a reconstitué, ce serait intéressant

**Documents fils**

1. Document qui éclaire les deux approches de la _recensio_ : tradition directe (tous les exemplaires liés directement au texte, cad tous les exemplaires qui transmettent le texte tel qu'il est) ou indirecte (exemplaires qui témoignent d'une tradition en parallèle : les traductions, des textes qui font référence et qui citent, les commentaires, les parodies, etc... / utile lorsqu'un texte est corrompu, car fenêtre sur un moment historique précis où le texte n'était pas corrompu) ? La tradition inderecte correspond à notre _expression_list_
--> exemple de Sophie : une expression, deux manifestations, deux items.

   Il s'agira donc de rentrer dans le détail de l'organisation MEI/FRBR de expressionList, manifestationList et itemList => un document fils pour chaque de ce trois 'chapitres'.

 - - -

Faire valider par Kévin pour la place du modèle FRBR, pour nous c'est dans <workList>
Marco a donné des gens à contacter pour partager tout ça : Laurent Pugin, Johannes Kepper (va s'opposer ; attention on tient aux protocoles pour l'interopérabilité) 
