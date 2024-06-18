**18/05/2024 avec Marco et Thomas**

Une fiche unique autour de la méthodologie pour l'édition critique / épouser la structure des guidelines en évoquant les grands chapitres
Mettre les exemples en fichiers séparés ; un fichier par exemple. 

1. Présentation générale de l'approche méthodologique
   
--> besoins de l'édition critique structurés à partir de deux modèles philologiques "historiquement importants" : méthode Karl Lachmann et méthode Joseph Bedier. Les deux méthodo convergent sur certains points ; cette partie commune constitue un socle qui peut être renseigné en utilisant les éléments du header MEI représentant des entités FRBR
Il faut un petit paragraphe qui présente les deux méthodes : https://prezi.com/p/eu1rfx3wtwyp/?present=1
- Pour Lachmann, le résultat final est la comparaison de toutes les sources à dispostion en les rapprochant au plus près d'Omega (uniquement binaire avec oui/non, pas théorisé mais interne à la méthode)
- Bédier critique fondamentalement la méthode de Lachmann : omega ou l'autographe se divise systématiquement en deux branches et Bédier trouve que le résultat est ainsi toujours banalisé, au contraire de la réalité où on aurait plus de branches ; chez Lachmann, quand on fait la comparaison des sources on arrive à un document qui n'a jamais existé dans l'histoire
- Bédier est uniquement d'accord pour le premier point ("recensio") qui doit être complet pour pouvoir faire une édition critique : les sources de tradition directe et indirecte (exercice infini...) : état de l'art, exercice provisoire. Pour Bédier il faut ensuite étudier toutes les sources : renseigner toutes les méta-données, etc afin d'établir ce qu'il nomme le "bon manuscrit". Choix d'une source (la plus complète et juste) après toutes ces études qui doit être justifié par les comparaisons précédentes, la moins dégradée et corrompue ; forcément dissensus entre les philologues...
- Bédier dit qu'il faut corriger les erreurs éventuellement présentes dans le "bon manuscrit" par la déduction
- Également troisième méthode autour de Barbi, Contini et Pasquali qui est moins critique avec Lachmann, hybride entre les deux, continue à maintenir la version de Lachmann en prenant en compte les critiques de Bédier.
- En FR on applique la méthode de Bédier sans savoir qui est Bédier, en s'en éloignant parfois sans vraiment le vouloir. La méthode Bédier est bonne lorsque l'on a très peu de sources. Dans l'Opéra par exemple on situe la première représentation puis on travaille ensuite à partir de cela. Exemple de _Don Giovanni_ entre la version de Prague (première) ou la version de Vienne qui connait de nombreux ajouts, parfois on fait une version hybride entre les deux, comme à Venise.

- **Ce qui est important pour nous pour le header MEI en FRBR c'est que la liste des oeuvres / expressions / manifestations / items corresponde à la _recensio_ et ensuite préciser quel type de méthode on a adopté ; 1ère partie de header la liste complète, puis dans _source_desc_ la liste après la _collatio_ et insérer un texte explicatif**
  
Trouver un cas où on a pas l'autographe mais où on l'a reconstitué, ce serait intéressant

- Une école intéressante pour nos questions serait le _Copy-text_ (au labo c'est Damien Colas qui maitrise cela) : https://www.jstor.org/stable/40371494 (méthode utilisée par Philippe Gossett, édition des opéras de Rossini)
  
- Paragraphe final pour maintenir la section _source_desc_ auprès de la communauté MEI car il permet d'exprimer au mieux, document considéré comme un "manifeste méthodologique".

**Documents fils**

1. Document qui éclaire les deux approches de la _recensio_ : tradition directe (tous les exemplaires liés directement au texte, cad tous les exemplaires qui transmettent le texte tel qu'il est) ou indirecte (exemplaires qui témoignent d'une tradition en parallèle : les traductions, des textes qui font référence et qui citent, les commentaires, les parodies, etc... / utile lorsqu'un texte est corrompu, car fenêtre sur un moment historique précis où le texte n'était pas corrompu) ? La tradition inderecte correspond à notre _expression_list_
--> exemple de Sophie : une expression, deux manifestations, deux items.

   Il s'agira donc de rentrer dans le détail de l'organisation MEI/FRBR de expressionList, manifestationList et itemList => un document fils pour chaque de ce trois 'chapitres'.
