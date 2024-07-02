## 1. Présentation générale de l'approche méthodologique

Ce document vise à proposer un protocole détaillé de renseignements des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques. Notre objectif visera à améliorer la précision et l'interopérabilité des données par le recours au modèle FRBR. 

Les besoins de l'édition critique textuelle se sont historiquement structurés à partir de deux modèles philologiques historiquement importants. Le premier d'entre eux, que l'on doit à l'allemand Karl Lachmann (1793 - 1851), s'articule en cinq points, en débutant par la première étape de la _recensio_, soit l'identification des sources, l'étude de la tradition. À ce stade, il s'agit de différencier les sources de _tradition directe_ - les manuscrits autographes, à défaut - et les sources de _tradition indirecte_, les traductions, citations, commentaires et parodies. Une fois cette première étape terminée, la seconde partie de la _recensio_ peut s'effectuer afin de compléter l'identification des sources. La troisième partie de la méthode est la _collatio_, qui consiste en un recensement complet des sources, avant de démarer une étape plus critique, l'_eliminatio codicum descriptorum_, qui consiste à éliminer les copies ou sources trop semblables, afin de constituer un corpus cohérent et propice au _stemma codicum_, la dernière étape du processus qui consiste à déterminer la relation entre les sources.




   
--> besoins de l'édition critique structurés à partir de deux modèles philologiques "historiquement importants" : méthode Karl Lachmann et méthode Joseph Bedier. Les deux méthodo convergent sur certains points ; cette partie commune constitue un socle qui peut être renseigné en utilisant les éléments du header MEI représentant des entités FRBR

### Présentation des méthodes, leurs liens et différences

Il faut un petit paragraphe qui présente les deux méthodes : https://prezi.com/p/eu1rfx3wtwyp/?present=1
- Pour Lachmann, le résultat final est la comparaison de toutes les sources à dispostion en les rapprochant au plus près d'Omega (uniquement binaire avec oui/non, pas théorisé mais interne à la méthode)
- Bédier critique fondamentalement la méthode de Lachmann : omega ou l'autographe se divise systématiquement en deux branches et Bédier trouve que le résultat est ainsi toujours banalisé, au contraire de la réalité où on aurait plus de branches ; chez Lachmann, quand on fait la comparaison des sources on arrive à un document qui n'a jamais existé dans l'histoire
- Bédier est uniquement d'accord pour le premier point ("recensio") qui doit être complet pour pouvoir faire une édition critique : les sources de tradition directe et indirecte (exercice infini...) : état de l'art, exercice provisoire. Pour Bédier il faut ensuite étudier toutes les sources : renseigner toutes les méta-données, etc afin d'établir ce qu'il nomme le "bon manuscrit". Choix d'une source (la plus complète et juste) après toutes ces études qui doit être justifié par les comparaisons précédentes, la moins dégradée et corrompue ; forcément dissensus entre les philologues...
- Bédier dit qu'il faut corriger les erreurs éventuellement présentes dans le "bon manuscrit" par la déduction
- En FR on applique la méthode de Bédier sans savoir qui est Bédier, en s'en éloignant parfois sans vraiment le vouloir. La méthode Bédier est bonne lorsque l'on a très peu de sources. Dans l'Opéra par exemple on situe la première représentation puis on travaille ensuite à partir de cela. Exemple de _Don Giovanni_ entre la version de Prague (première) ou la version de Vienne qui connait de nombreux ajouts, parfois on fait une version hybride entre les deux, comme à Venise.

### D'autres méthodes ?
  
- Également troisième méthode autour de Barbi, Contini et Pasquali qui est moins critique avec Lachmann, hybride entre les deux, continue à maintenir la version de Lachmann en prenant en compte les critiques de Bédier.
- Une école intéressante pour nos questions serait le _Copy-text_ (au labo c'est Damien Colas qui maitrise cela) : https://www.jstor.org/stable/40371494 (méthode utilisée par Philippe Gossett, édition des opéras de Rossini)

## 2. Approche des GT1 et GT2 pour la complétion des header MEI

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
