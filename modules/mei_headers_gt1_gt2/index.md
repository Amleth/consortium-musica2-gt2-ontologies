## 1. Présentation générale de l'approche méthodologique

Ce document vise à proposer un protocole détaillé de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques. Notre objectif visera à améliorer la précision et l'interopérabilité des données par le recours au modèle FRBR. 

Les besoins de l'édition critique textuelle se sont historiquement structurés à partir de deux modèles philologiques principaux. Le premier d'entre eux, que l'on doit à l'allemand Karl Lachmann (1793 - 1851), s'articule en cinq points, en débutant par la _recensio_, soit l'identification des sources et l'étude de la tradition. La _recensio_ consiste en deux étapes, la première desquelles s'occupe de différencier les sources de la « tradition directe » - tous les exemplaires qui transmettent l'œuvre en question - et les sources de la « tradition indirecte » – les traductions, citations, commentaires et parodies. Une fois cette première étape terminée, la seconde étape de la _recensio_ peut s'effectuer afin de procéder au dépouillement des toutes les sources recoltées et au recensement détaillé proprement dit. Le troisième point de la méthode est la _collatio_, qui consiste en la compairaison systématique des variantes et des erreurs attestés dans les sources, avant de démarer une étape plus critique, l'_eliminatio codicum descriptorum_, qui consiste à éliminer les exemplaires qui sont la copie exacte d'autres exemplaires conservés, afin de constituer un corpus cohérent et propice au _stemma codicum_, la dernière étape du processus consistant en la détermination de la relation entre les sources. Cette dernière étape permet l'établissement d'un arbre généalogique des sources représentant la tradition d'une œuvre.

La seconde méthode, établie par Joseph Bédier (1864-1938), critique fondamentalement la méthode de Lachmann : le _stemma codicum_ aboutit dans la majorité des cas à une représentation de la tradition articulée en deux branches. La critique de Bédier va en effet porter sur la difficulté de retrouver avec certitude les branches hautes du _stemma_, et sur ce qui lui semble l’indice du vice fondamental d’une telle ambition : l’abondance suspecte, dans les éditions critiques, des _stemmas_ bifides menant au blocage, par impossibilité de choisir laquelle des deux branches est la plus proche de l’original. Ce scepticisme va mener Bédier à suspendre l’activité reconstructive pour privilégier le texte d’un « bon » manuscrit en le retouchant le moins possible. De la méthode Lachman, Bédier sauve les deux premiers points - les deux étapes de la _recensio_ - qui restent l'outil scientifique indispensable du travail d'un éditeur afin d'effectuer une étude approfondie et complète de la tradition d'une œuvre. Cette méthode, également dite du « bon manuscrit » vise à choisir d'emblée la source la moins corrompue afin qu'elle constitue la base de l'édition critique ; les éventuelles erreurs contenues dans cette source seront corrigées au fur et à mesure du processus par les déductions du philologue (_ope ingenii_).

Bien que ces deux modèles soient les plus importants, il existe également une troisième méthode "synthétiste" de l'école philologique italienne [Michele Barbi (1867-1941), Giorgio Pasquali (1885-1952), Gianfranco Contini (1912-1990)] ; moins critique avec Lachmann, l'approche italienne consiste en gardant les cinq points fondamentaux de la méthode Lachmann, en introduisant plusieurs correctifs méthodologiques visant à répondre aux critiques de Bédier. Un autre positionnement méthodologique en matière de philologie musicale est celle du _Copy-text_, notamment utilisé par Philip Gossett (1941-2017) dans le cadre de l'édition critique des opéras de Rossini et de Verdi.

Dans le cadre de la présentation de notre protocole de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques, nous prenons donc comme point d'appui les deux modèles philologiques "historiquement importants" qui sont la méthode Karl Lachmann et la méthode Joseph Bédier. La convergence des deux méthodes sur la partie de la _recensio_ nous offre ainsi un socle pour entrevoir les éléments à renseigner dans le header MEI, en suivant les entités FRBR.

## 2. Approche des GT1 et GT2 pour la complétion des header MEI

L'appui sur les normes FRBR nous parait central, afin de combler une lacune dans l'interopérabilité des données de fichiers encodés en MEI. Dans le cadre de l'usage des normes FRBR en MEI, il est ainsi primordial que la liste des œuvres, des expressions, des manifestations puis des items corresponde de manière fine à la _recensio_ ; le header doit être rempli de la manière la plus complète et rigoureuse possible. Notre protocole étant orienté vers la redondance, il est ainsi probable que des métadonnées soient régulièrement répétées, par exemple le nom du compositeur que nous conseillons de reinsegner à chaque niveau du modèle FRBR.

Nous détaillons ci-dessous notre protocole en prenant appui sur le modèle des _guidelines_ MEI, afin d'en faciliter l'approche. Notons que des exemples concrets sont joints au sein du _repository_, ainsi qu'un modèle vierge qui pourra être copié et rempli au sein des headers des utilisateurs, pour une interopérabilité maximale. 

- _meiHead_
   - Le Mei Header est le lieu approprié pour accueillir toutes les données concernant les sources sur lesquels se base l'édition critique. D'un point de vue technique il s'agit de renseigner les infos concernanat la _recensio_, autrement dit la description complète des sources recoltées. La _recensio_ s'articule normalement en tradition directe (celle de la "expression" principale de l'œuvre) et tradition indirecte (celle qui prend en compte toute autre "expression" : traductions, parodies, commentaires/gloses, _scholiae_, citations, etc.)

**On utilise 0 lorsque l'on a accès à la source originale et oméga "⍵"  lorsque l'on n'y a pas accès**

- _fileDesc_
   - **Idem**
- _sourceDesc_ Ce module est l'élément central de notre protocole, puisque qu'il s'agit de la partie où nous décrivons de manière exacte le contenu scientifique. Selon les _guidelines_ MEI, il n'y a pas de renvoi au modèle FRBR au sein de _workList_. Il faut donc déployer le modèle FRBR à cet endroit.
   - _expressionList_ : il s'agit de nommer et détailler les différentes expressions, cette étape correspondant à notre protocole à la _recesio_ et donc à un discours commun aux théories de Lachmann et Bédier. Nous avons fait le choix de nommer l'expression de tradition directe _expression 0_. Les expressions indirectes se déploient ensuite avec des chiffres (1,2 _etc_) ou bien des noms en toutes lettres.
   - _manifestationList_ : de manière similaire à _expressionList_, nous nommons le manuscrit autographe (ou l'_omega_ issu du _stemma codicum_ si l'on ne possède pas l'autographe) _manifestation 0_. Pour chaque expression il convient d'utiliser une isntance de _manifestationList_ et pour chaque manifestation un _itemList_. Dans le cadre de manuscrits, la manifestation et l'item ne font qu'un. Par ailleurs, il n'y a pas, pour des raisons de catalogage évidentes, d'_item 0_ ; nous partons donc du principe que la dénomination des items fait appel au bon sens des chercheur·euse·s, de la tradition et des nomenclatures en usage.
   - 
   - **_Manifestation R7_is_exemplified_by Item_**
   - 
   - Le fichier MEI que nous sommes en train de renseigner constitue d'ailleurs une autre manifestation de l'œuvre, et doit par conséquent faire partie de la _manifestation_list_. Des xmlID seront utilisés pour chaque manifestation et item, afin d'assurer une inter-opérabilité maximale.

Le principal atout de notre protocole est l'interopérabilité, couplé à une réelle exhaustivité. Bien que sa réalisation puisse être fastidieuse de par le nombre important d'éléments à renseigner, le protocole porte une réelle valeur philologique et ainsi parfaitement adapté dans le cadre de l'édition critique, mais aussi au partage de fichiers au sein de la communauté internationale MEI.

**Faire un diagramme / en reparler avec Thomas**

**- Paragraphe final pour maintenir la section _source_desc_ auprès de la communauté MEI car il permet d'exprimer au mieux, document considéré comme un "manifeste méthodologique".**

## 3. Modules

_3. 1. Éclairer les approches de la _recensio__
  
tradition directe (tous les exemplaires liés directement au texte, cad tous les exemplaires qui transmettent le texte tel qu'il est) ou indirecte (exemplaires qui témoignent d'une tradition en parallèle : les traductions, des textes qui font référence et qui citent, les commentaires, les parodies, etc... / utile lorsqu'un texte est corrompu, car fenêtre sur un moment historique précis où le texte n'était pas corrompu) ? La tradition inderecte correspond à notre _expression_list_
--> exemple de Sophie : une expression, deux manifestations, deux items.

  Il s'agira donc de rentrer dans le détail de l'organisation MEI/FRBR de expressionList, manifestationList et itemList => un document fils pour chaque de ce trois 'chapitres'.

   - Trouver un cas où on a pas l'autographe mais où on l'a reconstitué, ce serait intéressant

_3. 2. Usage du Cidoc-CRM_
   
choisir un thésaurus ?
**il nous est nécessaire de concevoir une batterie de types E55 pour typer les différents niveaux des sources d'après le modèle FRBR**

 






 - - -

Faire valider par Kévin pour la place du modèle FRBR, pour nous c'est dans <workList>
Marco a donné des gens à contacter pour partager tout ça : Laurent Pugin, Johannes Kepper (va s'opposer ; attention on tient aux protocoles pour l'interopérabilité) 
