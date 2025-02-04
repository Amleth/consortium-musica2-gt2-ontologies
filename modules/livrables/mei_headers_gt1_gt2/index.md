## MEI Headers

### 1. Présentation générale de l'approche méthodologique

Ce document didactique, élaboré dans le cadre du consortium Huma-Num Musica2, vise à proposer un protocole détaillé de renseignement des métadonnées au sein des headers MEI dans le cadre des éditions critiques sous format numérique. L’objectif est d'établir un guide dédié aux éditions critiques encodées en MEI (Music Encoding Initiative) et de préciser où disposer les informations éditoriales et philologiques nécessaires, en proposant des choix réfléchis au détriment de la liberté habituellement accordée à l'encodeur par les guidelines MEI. Fixer des paramètres partagés et reconnus par la communauté musicologique permettra de créer des fichiers MEI qui pourront être contrôlés, vérifiés et échangés au profit de la transparence scientifique et de l'interopérabilité. Pour ce faire, le modèle FRBR appliqué à l'encodage MEI sera privilégié et suivi à l’occasion.

### Partie plus tardive

Les besoins de l'édition critique textuelle se sont historiquement structurés à partir de deux modèles philologiques principaux. Le premier d'entre eux, que l'on doit à l'allemand Karl Lachmann (1793 - 1851), s'articule en cinq points, en débutant par la _recensio_, soit l'identification des sources et l'étude de la tradition. La _recensio_ consiste en deux étapes, la première desquelles s'occupe de différencier les sources de la « tradition directe » - tous les exemplaires qui transmettent l'œuvre en question - et les sources de la « tradition indirecte » – les traductions, citations, commentaires et parodies. Une fois cette première étape terminée, la seconde étape de la _recensio_ peut s'effectuer afin de procéder au dépouillement des toutes les sources recoltées et au recensement détaillé proprement dit. Le troisième point de la méthode est la _collatio_, qui consiste en la compairaison systématique des variantes et des erreurs attestés dans les sources, avant de démarer une étape plus critique, l'_eliminatio codicum descriptorum_, qui consiste à éliminer les exemplaires qui sont la copie exacte d'autres exemplaires conservés, afin de constituer un corpus cohérent et propice au _stemma codicum_, la dernière étape du processus consistant en la détermination de la relation entre les sources. Cette dernière étape permet l'établissement d'un arbre généalogique des sources représentant la tradition d'une œuvre.

La seconde méthode, établie par Joseph Bédier (1864-1938), critique fondamentalement la méthode de Lachmann : le _stemma codicum_ aboutit dans la majorité des cas à une représentation de la tradition articulée en deux branches. La critique de Bédier va en effet porter sur la difficulté de retrouver avec certitude les branches hautes du _stemma_, et sur ce qui lui semble l’indice du vice fondamental d’une telle ambition : l’abondance suspecte, dans les éditions critiques, des _stemmas_ bifides menant au blocage, par impossibilité de choisir laquelle des deux branches est la plus proche de l’original. Ce scepticisme va mener Bédier à suspendre l’activité reconstructive pour privilégier le texte d’un « bon » manuscrit en le retouchant le moins possible. De la méthode Lachman, Bédier sauve les deux premiers points - les deux étapes de la _recensio_ - qui restent l'outil scientifique indispensable du travail d'un éditeur afin d'effectuer une étude approfondie et complète de la tradition d'une œuvre. Cette méthode, également dite du « bon manuscrit » vise à choisir d'emblée la source la moins corrompue afin qu'elle constitue la base de l'édition critique ; les éventuelles erreurs contenues dans cette source seront corrigées au fur et à mesure du processus par les déductions du philologue (_ope ingenii_).

Bien que ces deux modèles soient les plus importants, il existe également une troisième méthode "synthétiste", ou mieux "néolachmanienne", de l'école philologique italienne [Michele Barbi (1867-1941), Giorgio Pasquali (1885-1952), Gianfranco Contini (1912-1990)], qui reprend la méthode de Lachmann, en gardant ses cinq points fondamentaux et en introduisant plusieurs correctifs méthodologiques visant à répondre aux critiques de Bédier. Un autre positionnement méthodologique en matière de philologie musicale est celle du _Copy-text_, notamment utilisé par Philip Gossett (1941-2017) dans le cadre de l'édition critique des opéras de Rossini et de Verdi.

Dans le cadre de la présentation de notre protocole de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques, nous prenons donc comme point d'appui la partie sur laquelle toutes les méthodes semblent converger : celle de la _recensio_, qui nous offre ainsi un socle pour entrevoir les éléments à renseigner dans le header MEI, en suivant les entités FRBR.

### 2. Approche des GT1 et GT2 pour la complétion des headers MEI

L’interopérabilité des éditions critiques encodées en MEI repose sur l’adoption de normes partagées qui garantissent la cohérence et la compatibilité des fichiers produits. Actuellement, la grande liberté laissée aux encodeurs pour le renseignement des métadonnées dans le header MEI nuit à cette interopérabilité, en raison des choix individuels et des interprétations subjectives qui en résultent. Une telle hétérogénéité complique non seulement l’échange et l’exploitation des données, mais compromet également la transparence scientifique, un impératif fondamental des éditions critiques. C'est pourquoi nous proposons ici de proposer des alternatives d'encodage en FRBR ainsi que, le cas échéants, des alignements avec les clés de métadonnées HUMDRUM. 

### Pareil ici, trop philologique, à voir plus tard
La création de fichiers MEI hétéroclites empêche également la trasparence scientifique qui se doit à une édition critique, dont la précision du travail fait en amont de la _restitutio textus_ doit toujours être vérifiable et immédiatement repérable. D'où l'urgence de fixer un protocole de saisie partagé par la communauté scientifique. Dans ce cadre, les normes FRBR proposées par le biais de la MEI, qui à partir de l‘œuvre s'articulent en listes des expressions, des manifestations puis des items, correspondent précisement à la _recensio_ la plus complète possible, ce qui est la premesse méthodologique de chaque édition critique : le header MEI doit donc suivre l'arborescence FRBR et être renseigné de la manière la plus rigoureuse possible. Dans notre protocole, il est fortement recommandé de se tenir au principe de la redondance : toutes les informations nécessaires doivent être renseignées à chaque niveau du modèle FRBR. Il est ainsi probable que des métadonnées soient régulièrement répétées, par exemple le nom du compositeur ou le titre de l’œuvre.

Nous détaillons ci-dessous notre protocole en nous appuyant sur les guidelines MEI afin d’en faciliter l’adoption et la mise en œuvre. Pour illustrer concrètement ces recommandations, des exemples détaillés sont intégrés au repository, accompagnés d’un modèle vierge prêt à l’emploi. 

### Je propose de ne pas introduire le meiHead, on perfectionne les choses mais on ne traduit pas les guidelines
- _meiHead_
   - Le Mei Header est le lieu approprié pour accueillir toutes les métadonnées concernant les sources sur lesquels se base l'édition critique. D'un point de vue technique il s'agit de procéder avec une _recensio_ complète, qui regroupe toutes les sources de la tradition directe (celle de la "expression" principale de l'œuvre) et tradition indirecte (celle qui prend en compte toute autre "expression" : traductions, parodies, commentaires/gloses, _scholiae_, citations, etc.)

## Common Metadata Concepts (3.3) - Concepts sur les métadonnées communes - (optionnel finalement, un peu redondant) 

## Information about an MEI file (3.4) - Informations sur un fichier MEI

### File description 

### Edition Statement

### Revision Description

## Functional Requirements for Bibliographic Records (3.5) - FRBR

## Work Description (3.6) - Description de l'oeuvre

### Work Identification

#### Renseignement d'un ou plusieurs compositeurs

Clé HUMDRUM : COM

Définition : Indique le nom du compositeur de l'œuvre.

Chapitre des Guidelines : 3.6 Work Description

Balise : `<composer>`

Autre option : `<persName role="creator">`

Recommandations : Le ou les compositeurs renseignés ici ne concernent que l'oeuvre encodée dans le fichier MEI et non une oeuvre tierce. À noter également que la valeur de rôle est libre. Toutefois, il est conseillé de suivre un thesaurus ou un vocabulaire contrôlé dans un souci de standardisation. (Citer ici des exemples). Pour finir, nous préconisons de renseigner un URI identifiant l'individu concerné sur le web afin d'améliorer l'interopérabilité des métadonnées (ici aussi, préciser). 

Exemple : 
```
<workList xml:id=""..."">
   <work xml:id=""..."">
      <composer xml:id=""..."">
          <persName role=""creator"" (""composer"") auth.uri=""http://..."">...</persName>
      </composer>
   </work>
</workList>
```

Dans le cas de plusieurs compositeurs, recourir à une numération dans le cadre de role ou de l'xml id. Ex :

`<persName role="creator1">`

#### Compositeur attribué

Clé HUMDRUM : COA 

Définition : Désigne un compositeur attribué sur la base de preuves internes, externes ou par conjecture.  

Chapitre des Guidelines : 3.6 Work Description  

Balise : `<composer evidence="...">` 

Autre option : `<persName>`

Recommandations : La provenance de l’attribution doit être précisée à l'aide de l'attribut @evidence et des valeurs suivantes="internal, external, conjecture".  

Exemple :
```
<workList xml:id=""..."">
   <work xml:id=""..."">
      <composer xml:id=""..."" evidence=""..."" (internal, external or conjecture)>
          <persName auth.uri=""http://..."">...</persName>
      </composer>
   </work>
</workList>
```

#### Compositeur soupçonné

Clé : COS

Définition : Désigne un compositeur soupçonné avec un niveau de certitude.

Chapitre des Guidelines : 3.6 Work Description

Balise : `<composer>`

Autre option : `<persName>`

Recommandations : Il est conseillé d’utiliser l’attribut @cert pour indiquer le degré de certitude. Les valeurs autorisées sont : high, 
medium, low ou unknown.

Exemple:
```
<workList xml:id="...">
   <work xml:id="...">
      <composer xml:id="..." cert="low">
          <persName role="suspected creator" auth.uri="http://...">Nom soupçonné</persName>
      </composer>
   </work>
</workList>
```

### Alias ou pseudonyme du compositeur

Clé : COL

Définition : Indique un alias ou pseudonyme d’un compositeur.

Chapitre des Guidelines : 3.6 Work Description

Balise : `<persName>` et `<foreName>`

Autre option : `<foreName>` et `<famName>`

Recommandations : Peut être utilisé pour les noms d’emprunt, les noms de plume ou les pseudonymes historiques. Il est à noter que d'autres balises peuvent couvrir des sens de nomination plus fins : famName, genName, addName, genName, nameLink, et roleName. Leur gestion est sensiblement identique à celle de <foreName>.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <composer xml:id="...">
          <persName role="creator" auth.uri="http://...">Nom réel</persName>
          <persName>
            <foreName>Alias</foreName>
          </persName>  
      </composer>
   </work>
</workList>
```

### Dates de naissance et de décès du compositeur

Clé HUMDRUM : CDT

Définition : Indique les dates de naissance et de décès du compositeur.

Chapitre des Guidelines : -

Balise : `<persName>` avec les attributs @startdate et @enddate.

Recommandations : Peut être omis si le compositeur est référencé avec une URI externe.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <composer xml:id="...">
          <persName startdate="1685" enddate="1750" auth.uri="http://...">Nom du compositeur</persName>
      </composer>
   </work>
</workList>
```

### Nationalité du compositeur

Clé HUMDRUM : CNT

Définition : Indique la nationalité du compositeur.

Chapitre des Guidelines : 3.6 Work Description

Balise : `<annot>` 

Recommandations : Peut être omis si le compositeur est référencé avec une URI externe.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <composer xml:id="...">
          <persName auth.uri="http://...">Nom du compositeur</persName>
          <annot label="nationality">Français</annot>
      </composer>
   </work>
</workList>
```

### Lieu de naissance et de décès d'un compositeur

Clé HUMDRUM : CBL et CDL

Définition : Indique le lieu de naissance et de décès d'un compositeur.

Chapitre des Guidelines : -

Balise : `<persName>` et `<date>` avec les attributs @startdate et @enddate.

Recommandations : Peut être omis si le compositeur est référencé avec un URI externe. Il est conseillé d'utiliser un URI, via @auth.uri, pour préciser le lieu. Nous préconisons l'usage d'un URI GeoNames.  

Exemple :
```
<workList xml:id=""..."">
   <work xml:id=""..."">
      <composer xml:id=""..."">
          <persName auth.uri=""http://..."">...</persName>
          <date stardate=""..."">
             <country auth.uri="...">XXX</country>
          </date>
          <date enddate=""..."">
             <country>XXX</country>
         </date>     
      </composer>
   </work>
</workList>
```
### Nom du librettiste

Clé HUMDRUM : LIB

Définition : Indique le nom du librettiste de l'oeuvre. 

Chapitre des Guidelines : -

Balise : `<librettist>`

Autre option : `<persName role="librettist">`

Exemple :
```
<workList xml:id=""..."">
   <work xml:id=""..."">
      <librettist>
         <persName auth.uri=""...""></persName>
      </librettist>   
   </work>
</workList>
```

### Nom de l'arrangeur 



#### Encoding Sources in MEI (3.7) - Encodage des sources en MEI



**On utilise 0 lorsque l'on est en presence de la source originale (normalement l'autographe de l'œuvre) et oméga "⍵" lorsque la source originale de l'œuvre ne nous est pas parvenue**

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

**Faire un diagramme / en reparler avec Thomas et Marco**

### 3. Pour conclure

Paragraphe final pour maintenir la section _source_desc_ auprès de la communauté MEI car il permet d'exprimer au mieux, document considéré comme un "manifeste méthodologique"

### 4. Modules

_4. 1. Éclairer les approches de la _recensio__
  
tradition directe (tous les exemplaires liés directement au texte, cad tous les exemplaires qui transmettent le texte tel qu'il est) ou indirecte (exemplaires qui témoignent d'une tradition en parallèle : les traductions, des textes qui font référence et qui citent, les commentaires, les parodies, etc... / utile lorsqu'un texte est corrompu, car fenêtre sur un moment historique précis où le texte n'était pas corrompu) ? La tradition inderecte correspond à notre _expression_list_
--> exemple de Sophie : une expression, deux manifestations, deux items.

  Il s'agira donc de rentrer dans le détail de l'organisation MEI/FRBR de expressionList, manifestationList et itemList => un document fils pour chaque de ce trois 'chapitres'.

   - Trouver un cas où on a pas l'autographe mais où on l'a reconstitué, ce serait intéressant

_4. 2. Usage du CIDOC CRM_
   
choisir un thésaurus ?
**il nous est nécessaire de concevoir une batterie de types E55 pour typer les différents niveaux des sources d'après le modèle FRBR**

 






 - - -

Faire valider par Kévin pour la place du modèle FRBR, pour nous c'est dans <workList>
Marco a donné des gens à contacter pour partager tout ça : Laurent Pugin, Johannes Kepper (va s'opposer ; attention on tient aux protocoles pour l'interopérabilité) 
