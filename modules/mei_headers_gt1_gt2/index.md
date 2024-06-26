## 1. Présentation générale de l'approche méthodologique

Ce document vise à proposer un protocole détaillé de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques. Notre objectif visera à améliorer la précision et l'interopérabilité des données par le recours au modèle FRBR. 

Les besoins de l'édition critique textuelle se sont historiquement structurés à partir de deux modèles philologiques historiquement importants. Le premier d'entre eux, que l'on doit à l'allemand Karl Lachmann (1793 - 1851), s'articule en cinq points, en débutant par la première étape de la _recensio_, soit l'identification des sources, l'étude de la tradition. À ce stade, il s'agit de différencier les sources de _tradition directe_ - le manuscrit autographe, aussi nommé _omega_- et les sources de _tradition indirecte_, les traductions, citations, commentaires et parodies. Une fois cette première étape terminée, la seconde partie de la _recensio_ peut s'effectuer afin de compléter l'identification des sources. La troisième partie de la méthode est la _collatio_, qui consiste en un recensement complet des sources, avant de démarer une étape plus critique, l'_eliminatio codicum descriptorum_, qui consiste à éliminer les copies ou sources trop semblables, afin de constituer un corpus cohérent et propice au _stemma codicum_, la dernière étape du processus consistant en la détermination de la relation entre les sources. Cette dernière étape permet l'établissement d'un tableau généalogique des sources constituant une même œuvre.

La seconde méthode établie par Joseph Bédier (1864-1938) critique fondamentalement la méthode de Lachmann : le _stemma codicum_ aboutit dans la majorité des cas à une division systématique de l'_omega_ (autographe) en deux branches. Ce résultat est dû à la binarité inhérente à la logie formelle de la méthode de Lachmann, aisément visibile dans les liens tracés entre deux exemplaires : si une erreur est commune à deux exemplaires, ces derniers sont forcément mis en relation d'une manière binaire (oui ou non) et éliminent la possibilité d'une analyse plus détaillée. Selon Bédier, le résultat du _stemma codicum_ est alors toujours banalisé, au contraire d'une vision plus fine et complexe du phénomène réel où l'on aurait plus de branches. Le second problème soulevé par Bédier est lié au document résultant de la comparaison des sources : il en ressort un document n'ayant jamais eu une quelconque existence réelle, issus de conjectures établies autour d'archétypes et de sources fantasmées, et concaténant diverses sources en une production philologique, plutôt que de se pencher vers une source véritable. Pour Bédier, le seul bon outil développé par Lachman est lié aux deux premiers points - les deux étapes de la _recensio_ - qui doivent être réalisés afin d'imaginer correctement effectuer un travail d'édition critique. Cette méthode, également dite du _bon manuscrit_ vise à choisir d'emblée la source la moins corrompue afin qu'elle constitue la base de l'édition critique ; les éventuelles erreurs seront corrigées au fur et à mesure du processus par les déductions du philologue. Cette méthode est particluièrement pertinente dans le cas d'un nombre réduit de sources. Par exemple, dans le cas d'un Opéra le _bon manuscrit_ est celui utilisé lors de la première représentation, à partir duquel on travaille ensuite. Prenons comme exemple le _Don Giovanni_ de Mozart : entre la version de Prague (création) et la version de Vienne qui connait, l'œuvre connait  de nombreux ajouts. La version de Venise est quant à elle hyrbide... D'où la nécessité d'un point de départ clair.

Bien que ces deux modèles soient les plus importants, il existe également une troisième méthode "synthétiste" imaginée par Giorgio Pasquali (1885-1952) ; moins critique avec Lachmann, sa méthode  hybride les apports des deux précédentes en maintenant la version de Lachmann, tout en prenant en compte les critiques de Bédier. Une dernière école est celle du _Copy-text_, notamment utilisée par Philip Gossett (1941-2017) dans le cadre de l'édition critique des opéras de Rossini.

Dans le cadre de la présentation de notre protocole de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques, nous prenons donc comme point d'appui les deux modèles philologiques "historiquement importants" que sont la méthode Karl Lachmann et méthode Joseph Bédier. La convergence des deux méthodes nous offre ainsi un socle pour entrevoir les éléments à renseigner en utilisant les éléments du header MEI représentant des entités FRBR.

## 2. Approche des GT1 et GT2 pour la complétion des header MEI

L'appui sur les normes FRBR nous parait central et permet de combler une lacune dans l'interopérabilité des données de fichiers encodés en MEI.

- **Ce qui est important pour nous pour le header MEI en FRBR c'est que la liste des oeuvres / expressions / manifestations / items corresponde à la _recensio_ et ensuite préciser quel type de méthode on a adopté ; 1ère partie de header la liste complète, puis dans _source_desc_ la liste après la _collatio_ et insérer un texte explicatif**

- Remplir le MEIheader de la manière la plus complète possible ; notre protocole est orienté vers la **redondance** : remplir toutes les cases possibles, le compositeur est donc répété une dizaine de fois. L'important pour notre protocole est **l'interopérabilité** / faire communauté et permettre la vérification, par exemple dans le cas d'éditions critiques

- <meiHead>
   - Tittle stat etc
- <fileDesc>
   - Tous les éléments
   - <sourceDesc> très important pour nous / question de la place des <statement>, pour Marco indispensable dans <sourceDesc>, c'est la partie   
      de <fileDesc> dans laquelle on donne exactement le contenu scientifique (cf 3.6.11)
- <workList> : pas de renvoi au modèle FRBR, ce qui ne nous arrange pas... **il faut donc déployer le modèle FRBR à cet endroit**
   - <expressionList> on peut nommer les différentes expressions : il y aura **_une expression 0_** qui sera le point de départ (expression            directe) tandis que l'expression indirecte se déploie avec des chiffres (1,2 etc)
   - <manifestationList> dans <workList> ? Ainsi que les <itemList> / **_manifestation 0 est l'autographe_** si on a pas l'autographe on parle       **d'omega** issu de _stemma caudicum_ (arbre généalogique qui décrit la tradition) ; si on a pas l'autographe on laisse manifestation 0          vide, idéalement le fichier MEI devrait remplacer manifestation 0 (omega)
   - Pour chaque expression un <manifestationList>, pour chaque manifestation un <itemList>
      - Préciser que pour des manuscrits manifestation = item
   - Le fichier MEI que l'on créé est une autre manifestation de l'œuvre ; il faut aussi renseigner ce fichier en tant que MEI

- Mettre des xmlID pour manifestation et item, cf manif 0 ; il faut que l'on trouve une manière de nommer les choses / un item ne peut pas être 0

- Nomenclature ? Chacun s'organise, mais on essaie de respecter la tradition et la nomenclature

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
