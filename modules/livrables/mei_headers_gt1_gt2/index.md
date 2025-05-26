## MEI Headers

### 1. Présentation générale de l'approche méthodologique

Ce document didactique, élaboré dans le cadre du consortium Huma-Num Musica2, vise à proposer un protocole détaillé de renseignement des métadonnées au sein des headers MEI, plus particulièrement dans le cadre d'éditions critiques numériques. L’objectif est d'établir un guide dédié aux éditions encodées en MEI (Music Encoding Initiative) et de préciser où disposer les informations éditoriales et philologiques nécessaires, en proposant des choix raisonnés palliant diverses ambiguïtés des guidelines MEI. Fixer des paramètres partagés et reconnus par la communauté musicologique permettra de créer des fichiers MEI qui pourront être contrôlés, vérifiés et échangés au profit de la transparence scientifique et de l'interopérabilité. Pour ce faire, le modèle FRBR appliqué à l'encodage MEI sera privilégié et suivi à l’occasion.

### Partie plus tardive

Les besoins de l'édition critique textuelle se sont historiquement structurés à partir de deux modèles philologiques principaux. Le premier d'entre eux, que l'on doit à l'allemand Karl Lachmann (1793 - 1851), s'articule en cinq points, en débutant par la _recensio_, soit l'identification des sources et l'étude de la tradition. La _recensio_ consiste en deux étapes, la première desquelles s'occupe de différencier les sources de la « tradition directe » - tous les exemplaires qui transmettent l'œuvre en question - et les sources de la « tradition indirecte » – les traductions, citations, commentaires et parodies. Une fois cette première étape terminée, la seconde étape de la _recensio_ peut s'effectuer afin de procéder au dépouillement des toutes les sources recoltées et au recensement détaillé proprement dit. Le troisième point de la méthode est la _collatio_, qui consiste en la compairaison systématique des variantes et des erreurs attestés dans les sources, avant de démarer une étape plus critique, l'_eliminatio codicum descriptorum_, qui consiste à éliminer les exemplaires qui sont la copie exacte d'autres exemplaires conservés, afin de constituer un corpus cohérent et propice au _stemma codicum_, la dernière étape du processus consistant en la détermination de la relation entre les sources. Cette dernière étape permet l'établissement d'un arbre généalogique des sources représentant la tradition d'une œuvre.

La seconde méthode, établie par Joseph Bédier (1864-1938), critique fondamentalement la méthode de Lachmann : le _stemma codicum_ aboutit dans la majorité des cas à une représentation de la tradition articulée en deux branches. La critique de Bédier va en effet porter sur la difficulté de retrouver avec certitude les branches hautes du _stemma_, et sur ce qui lui semble l’indice du vice fondamental d’une telle ambition : l’abondance suspecte, dans les éditions critiques, des _stemmas_ bifides menant au blocage, par impossibilité de choisir laquelle des deux branches est la plus proche de l’original. Ce scepticisme va mener Bédier à suspendre l’activité reconstructive pour privilégier le texte d’un « bon » manuscrit en le retouchant le moins possible. De la méthode Lachman, Bédier sauve les deux premiers points - les deux étapes de la _recensio_ - qui restent l'outil scientifique indispensable du travail d'un éditeur afin d'effectuer une étude approfondie et complète de la tradition d'une œuvre. Cette méthode, également dite du « bon manuscrit » vise à choisir d'emblée la source la moins corrompue afin qu'elle constitue la base de l'édition critique ; les éventuelles erreurs contenues dans cette source seront corrigées au fur et à mesure du processus par les déductions du philologue (_ope ingenii_).

Bien que ces deux modèles soient les plus importants, il existe également une troisième méthode "synthétiste", ou mieux "néolachmanienne", de l'école philologique italienne [Michele Barbi (1867-1941), Giorgio Pasquali (1885-1952), Gianfranco Contini (1912-1990)], qui reprend la méthode de Lachmann, en gardant ses cinq points fondamentaux et en introduisant plusieurs correctifs méthodologiques visant à répondre aux critiques de Bédier. Un autre positionnement méthodologique en matière de philologie musicale est celle du _Copy-text_, notamment utilisé par Philip Gossett (1941-2017) dans le cadre de l'édition critique des opéras de Rossini et de Verdi.

Dans le cadre de la présentation de notre protocole de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques, nous prenons donc comme point d'appui la partie sur laquelle toutes les méthodes semblent converger : celle de la _recensio_, qui nous offre ainsi un socle pour entrevoir les éléments à renseigner dans le header MEI, en suivant les entités FRBR.

### 2. Approche des GT1 et GT2 pour la complétion des headers MEI

L’interopérabilité des éditions critiques encodées en MEI repose sur l’adoption de normes partagées qui garantissent la cohérence et la compatibilité des fichiers produits. Actuellement, la grande liberté laissée aux encodeurs pour le renseignement des métadonnées dans le header MEI nuit à cette interopérabilité, en raison des choix individuels et des interprétations subjectives qui en résultent. Une telle hétérogénéité complique non seulement l’échange et l’exploitation des données, mais compromet également la transparence scientifique, un impératif fondamental des éditions critiques. C'est pourquoi nous proposons ici de proposer des alternatives d'encodage en FRBR ainsi que, le cas échéants, des alignements avec les clés de métadonnées HUMDRUM. 

### Pareil ici, trop philologique, à voir plus tard
La création de fichiers MEI hétéroclites empêche également la transparence scientifique qui se doit à une édition critique, dont la précision du travail fait en amont de la _restitutio textus_ doit toujours être vérifiable et immédiatement repérable. D'où l'urgence de fixer un protocole de saisie partagé par la communauté scientifique. Dans ce cadre, les normes FRBR proposées par le biais de la MEI, qui à partir de l‘œuvre s'articulent en listes des expressions, des manifestations puis des items, correspondent précisement à la _recensio_ la plus complète possible, ce qui est la premesse méthodologique de chaque édition critique : le header MEI doit donc suivre l'arborescence FRBR et être renseigné de la manière la plus rigoureuse possible. Dans notre protocole, il est fortement recommandé de se tenir au principe de la redondance : toutes les informations nécessaires doivent être renseignées à chaque niveau du modèle FRBR. Il est ainsi probable que des métadonnées soient régulièrement répétées, par exemple le nom du compositeur ou le titre de l’œuvre.

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

#### Alias ou pseudonyme du compositeur

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

Clé HUMDRUM : LAR

Définition : Indique le nom de l'arrangeur de l'oeuvre. 

Chapitre des Guidelines : 3.6 Work Description

Balise : `<arranger>`

Autre option : `<persName role="arranger">`

Recommandations : Suivant les guidelines MEI pour <arranger>, il est uniquement question du sens "classique" de la fonction - celui qui transcrit la pièce pour une nomenclature musicale différente de l'originale. Pour "orchestrateur", voir ci-dessous.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <arranger>
         <persName auth.uri="..."></persName>
      </arranger>   
   </work>
</workList>
```

### Nom de l'orchestrateur 

Clé HUMDRUM : LOR

Définition : Indique le nom de l'orchestrateur de l'oeuvre. 

Chapitre des Guidelines : -

Balise : `<arranger role="orchestrator">`

Autre option : `<persName role="orchestrator">`

Recommandations : Comme dit ci-dessus, <arranger> représente uniquement le sens "classique" de la fonction : la personne qui transcrit la pièce pour une nomenclature musicale différente de l'originale. Il est donc nécessaire de préciser à l'aide de @role la qualité spécifique de l'arrangeur.  Dans la mesure où "orchestrator" n'est pas présent dans les Marc Relators, nous proposons de nous appuyer sur le vocabulaire Doremus des fonctions, comprenant "arranger" ainsi que de nombreuses sous-fonctions comme "orchestrator", "creator_of_musical_harmonization" ou encore "creator_of_musical_paraphrase" (https://github.com/DOREMUS-ANR/knowledge-base/blob/master/vocabularies/function.ttl).

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <arranger>
         <persName role="orchestrator" auth.uri="..."></persName>
      </arranger>   
   </work>
</workList>
```
### Langue originaire du texte

Clé HUMDRUM : TXO

Définition : Indique la langue originale de l'oeuvre encodée. 

Chapitre des Guidelines : 3.6.6 Language Usage

Balise : `<langUsage>/<language>`

Autre option : -

Recommandations : <langUsage> contient l'ensemble des langues devant être décrites dans le fichier MEI. Dans le cas d'une seule langue renseignée, ici la langue originale, il n'apparait pas nécessaire de s'encombrer d'un attribut le précisant (comme dans l'exemple ci-dessous). Pour la distinction de plusieurs langues dans le cas de traductions ou d'adaptations, voir ci-dessous. 

Il est cependant conseillé, pour des questions d'interopérabilité, d'ajouter l'identifiant ISO de la langue renseignée à l'aide des attributs @auth.uri et @uri.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <langUsage>
         <language xml:id="..." auth.uri="https://iso639-3.sil.org/code/fra" uri="ISO 639">French</language>
     </langUsage>         
   </work>
</workList>
```

### Langue originale de la pièce

Clé HUMDRUM : TXO

Définition : Indique la langue originale de l'oeuvre encodée. 

Chapitre des Guidelines : 3.6.6 Language Usage

Balise : `<langUsage>/<language>`

Autre option : -

Recommandations : <langUsage> contient l'ensemble des langues devant être décrites dans le fichier MEI. Dans le cas d'une seule langue renseignée, ici la langue originale, il n'apparait pas nécessaire de s'encombrer d'un attribut le précisant (comme dans l'exemple ci-dessous). Pour la distinction de plusieurs langues dans le cas de traductions ou d'adaptations, voir ci-dessous. 

Il est cependant conseillé, pour des questions d'interopérabilité, d'ajouter l'identifiant ISO de la langue renseignée à l'aide des attributs @auth.uri et @uri.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <langUsage>
         <language xml:id="..." auth.uri="https://iso639-3.sil.org/code/fra" uri="ISO 639">French</language>
     </langUsage>         
   </work>
</workList>
```

### Langue de la pièce encodée (si différente de la langue originale)

Clé HUMDRUM : TXL

Définition : Indique la langue de l'oeuvre encodée, si différente de la langue originale (traduction, adaptation, etc). 

Chapitre des Guidelines : 3.6.6 Language Usage

Balise : `<langUsage>/<language>`

Autre option : -

Recommandations : En cas de langue traduite utilisée au sein du fichier, il semble que la seule possibilité en MEI (en raison de l'absence du <ProfilDesc> de la TEI) est de préciser la nature des langues à l'aide d'un @type (type="original", type="translation"). C'est à ce niveau que la balise <langUsage> trouve véritablement son sens en permettant de lister plusieurs langues. 

En plus de l'identifiant ISO, il est conseillé de préciser un @xml:id propre à chaque langue afin de pouvoir renseigner ce même identifiant dans la partie <music>, dans <verse> ou <syl> à l'aide de @xml:lang - précisant ainsi la langue utilisée pour chaque entité textuelle présente dans l'édition numérique.  

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <langUsage>
         <language xml:id="Lat" auth.uri="https://iso639-3.sil.org/code/lat" uri="ISO 639-3" type="original">Latin</language>
         <language xml:id="Fr" auth.uri="https://iso639-3.sil.org/code/fra" uri="ISO 639-3" type="translation">French</language>
     </langUsage>          
   </work>
</workList>
```
### Traducteur du texte

Clé HUMDRUM : TRN

Définition : Indique, le cas échéant, l'identité de la personne responsable de la traduction de l'oeuvre. 

Chapitre des Guidelines : -

Balise (dans le cas d'un traducteur historique, propre à l'oeuvre encodée) : `<contributor>/<persName>`

Autre option (dans le cas d'un traducteur ad hoc, pour l'édition numérique ou l'édition moderne utilisée comme source) : '<respStmt>/<persName>`

Recommandations : Renseigner la personne responsable de la traduction d'une oeuvre dépend avant tout du statut de cette dernière. S'il s'agit d'un traducteur historique (dans le cas où la traduction est une manifestation de l'oeuvre), celui-ci est renseigné comme un <contributor> au sein de <workList>. Sa fonction précise est indiquée à l'aide de @role="translator" - le terme "translator" fait partie des Marc Relators ainsi que du vocabulaire des fonctions de Doremus. L'identifiant du traducteur (@xml:id) doit être ajouté dans la définition de la langue <language>.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <contributor>
         <persName xml:id="T1" role="translator" auth.uri="...">XXX</persName>
      </contributor>   
      <langUsage>
         <language xml:id="Lat" type="original">Latin</language>
         <language xml:id="Fr" resp="T1" type="translation">French</language>
     </langUsage>          
   </work>
</workList>
```
Recommandations : Si, à l'inverse, il s'agit d'un traducteur ad hoc dont la traduction n'a qu'une valeur éditoriale, il est préférable de renseigner son identité dans <fileDesc>, avec l'ensemble des personnes disposant d'une responsabilité éditoriale. Le fonctionnement reste cependant le même que précédemment, dans la mesure où l'identifiant du traducteur doit à nouveau être indiqué dans la définition de la langue concernée (dans <workList>), via @resp. 

Il est à noter que bien localiser la place du traducteur et de renseigner son identifiant dans <language> pallie l'absence de différence explicite en MEI entre un texte traduit constitutif de l'oeuvre (traduction historique) et un texte traduit pour les besoins de l'édition (traduction éditoriale). 

Exemple :
```
<fileDesc xml:id="...">
   <titleStmt xml:id="...">
       <respStmt xml:id="...">
          <persName xml:id="VV" role="translator" auth.uri="http://...">...</persName>
       </respStmt>
   </titleStmt>
</fileDesc>

-------# plus bas

<workList xml:id="...">
   <work xml:id="...">
      <langUsage>
         <language xml:id="..." type="original">...</language>
         <language xml:id="Fr" resp="VV" type="translation">...</language>
     </langUsage>          
   </work>
</workList>
```

#### Titre de l'oeuvre 

Clé HUMDRUM :  OTL

Définition : Titre de l'oeuvre encodée.

Chapitre des Guidelines : 3.6 Work Description

Balise :<title>

Autre option : -

Recommandations : Cette manière très simple de renseigner le titre convient surtout aux titres officiels et consensuels des oeuvres - des titres qui ne font pas l'objet d'ambiguité. Pour le renseignement de titres alternatifs ou populaires, voir plus bas.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <title xml:id="...">Pavane pour une infante défunte</title>
   </work>
</workList>
```

#### Titre courant de l'oeuvre

Clé : OTP

Définition : Titre populaire de l'oeuvre encodée.

Chapitre des Guidelines : -  

Balise : <title>

Autre option : -

Recommandations : Le titre courant peut facilement se confondre avec le titre alternatif (voir ci-dessous). Sur ce point, seuls les usages peuvent apporter des réponses. Dans le doute, il est préférable de privilégier le titre alternatif, moins restrictif que le sens sous-entendu par titre "courant". 

**Exemple :**
```
<workList xml:id="...">
   <work xml:id="...">
      <title type="main">Sonate pour piano no. 11</title>
      <title type="alternative">Marche turque</title>
   </work>
</workList>
```

#### Titre alternatif

**Clé :** OTA

**Définition :** Titre alternatif

**Chapitre des Guidelines :** 

**Balise :** <workList xml:id="...">
   <work xml:id="...">
      <title type="main">Sonate pour piano no. 11</title>
      <title type="alternative">Marche turque</title>
   </work>
</workList>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList xml:id="...">
   <work xml:id="...">
      <title type="main">Sonate pour piano no. 11</title>
      <title type="alternative">Marche turque</title>
   </work>
</workList>
```

#### Titre de l'œuvre d'appartenance

**Clé :** OPR

**Définition :** Titre de l'œuvre d'appartenance

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <title type="main">Missa Je suis déshéritée</title>
      <title type="part">Kyrie</title>
   </work>
</workList>  

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <title type="main">Missa Je suis déshéritée</title>
      <title type="part">Kyrie</title>
   </work>
</workList>  
```


#### Numéro d'acte

**Clé :** OAC

**Définition :** Numéro d'acte

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** <body>
   <mdiv label="act" n="1">
      <mdiv label="scene" n="1">
         <score></score>
      </mdiv>
      <mdiv label="scene" n="2">
         <score></score>
      </mdiv>
   </mdiv>
   <mdiv label="act" n="2">
      <mdiv label="scene" n="1">
         <score></score>
      </mdiv>
      <mdiv label="scene" n="2">
         <score></score>
      </mdiv>
   </mdiv>
</body>

**Recommandations :** S'il est bien question d'une précision au sein de <music> : "The score and parts elements are placed here and not directly within the body element because score and part characteristics may change from mdiv to mdiv. For example, the 2nd movement of a symphony may require different performing forces (and therefore different score and part layout) than the other movements. The mdiv element may be recursively nested in order to represent music which exhibits this kind of structure. For example, an opera is normally divided into acts, which are in turn divided into scenes." https://music-encoding.org/guidelines/v5/elements/mdiv.html

**Exemple :**
```

```


#### Numéro de scène

**Clé :** OSC

**Définition :** Numéro de scène

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** <body>
   <mdiv label="act" n="1">
      <mdiv label="scene" n="1">
         <score></score>
      </mdiv>
      <mdiv label="scene" n="2">
         <score></score>
      </mdiv>
   </mdiv>
   <mdiv label="act" n="2">
      <mdiv label="scene" n="1">
         <score></score>
      </mdiv>
      <mdiv label="scene" n="2">
         <score></score>
      </mdiv>
   </mdiv>
</body>

**Recommandations :** 

**Exemple :**
```

```


#### Numéro de mouvement

**Clé :** OMV

**Définition :** Numéro de mouvement

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** <body>
   <mdiv label="Allegro" n="1">
      <score></score>
   </mdiv>
   <mdiv label="Menuet" n="2">
      <score></score>
   </mdiv>
</body>

**Recommandations :** Même commentaire que ci-dessous. Pour le numéro, nous pourrions ajouter dans les différents éléments @n.

**Exemple :**
```

```


#### Désignation du mouvement ou nom du mouvement

**Clé :** OMD

**Définition :** Désignation du mouvement ou nom du mouvement

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** <body>
   <mdiv label="Allegro">
      <score></score>
   </mdiv>
   <mdiv label="Menuet">
      <score></score>
   </mdiv>
</body> 

**Recommandations :** S'il s'agit d'un seul mouvement encodé au sein du fichier MEI, alors il me semble que le renseignement est similaire à celui renseigné pour "titre de l'oeuvre d'appartenance". Sil s'agit de plusieurs mouvements encodés au sein d'un même fichier MEI (peu recommandé), dans ce cas il faudrait indiquer cette information dans <music> à l'aide de <mdiv>. 

**Exemple :**
```

```


#### Numéro d'opus

**Clé :** OPS

**Définition :** Numéro d'opus

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <title type="main">Prélude en do majeur</title>
      <title type="subordinate" label="opus">28</title>
   </work>
</worklist> 
____
<workList>
   <work>
      <title type="main">Sonate pour piano no. 11</title>
      <title type="subordinate" label="Köchel">331/300</title>
   </work>
</worklist>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <title type="main">Prélude en do majeur</title>
      <title type="subordinate" label="opus">28</title>
   </work>
</worklist> 
____
<workList>
   <work>
      <title type="main">Sonate pour piano no. 11</title>
      <title type="subordinate" label="Köchel">331/300</title>
   </work>
</worklist>
```


#### Numéro

**Clé :** ONM

**Définition :** Numéro

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Volume

**Clé :** OVM

**Définition :** Volume

**Chapitre des Guidelines :** 

**Balise :** <source>
  <bibl>
      <composer>
          <persName auth="VIAF" auth.uri="https://...">XXX</persName>
      </composer>
      <title type="main">XXX</title>
      <editor>
          <persName auth="VIAF" auth.uri="..."></persName>
      </editor>
      <biblScope label="volume">1</biblScope>
   </bibl>
</source>

**Autre option :** 

**Recommandations :** J'imagine que cela concerne essentiellement des données bibliographiques. J'emprunte cette manière à la TEI. La même est possible pour le numéro. 

**Exemple :**
```
<source>
  <bibl>
      <composer>
          <persName auth="VIAF" auth.uri="https://...">XXX</persName>
      </composer>
      <title type="main">XXX</title>
      <editor>
          <persName auth="VIAF" auth.uri="..."></persName>
      </editor>
      <biblScope label="volume">1</biblScope>
   </bibl>
</source>
```


#### Dédicace

**Clé :** ODE

**Définition :** Dédicace

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <creation>
         <dedicatee>
            <persName>...</persName>
         </dedicatee>
      </creation>
   </work>
<workList>  

**Autre option :** Ou si nous souhaitons ajouter plus d'informations sur la dédicace elle-même et son contexte:

<workList>
   <work>
      <creation>
         <dedication>
            <quote>...</quote>
            <eventList>...</eventList>
            <dedicatee>
               <persName>...</persName>
            </dedicatee>
         </dedication>
      </creation>
   </work>
<workList>   

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <creation>
         <dedicatee>
            <persName>...</persName>
         </dedicatee>
      </creation>
   </work>
<workList>  
```


#### Committant (commettant ?)

**Clé :** OCO

**Définition :** Committant (commettant ?)

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Collectionneur ?

**Clé :** OCL

**Définition :** Collectionneur ?

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Note de format libre / Nota bene

**Clé :** ONB

**Définition :** Note de format libre / Nota bene

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** Cela se trouverait dans <notesStmt> puis <annot> (pour le header).

**Exemple :**
```

```


#### Date de composition

**Clé :** ODT

**Définition :** Date de composition

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <creation>
         <date notbefore="1530" notafter="1550" cert="low">1540</date>
      </creation>
   </work>
</workList>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <creation>
         <date notbefore="1530" notafter="1550" cert="low">1540</date>
      </creation>
   </work>
</workList>
```


#### Pays de composition

**Clé :** OCY

**Définition :** Pays de composition

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <creation>
         <date notbefore="1530" notafter="1550" cert="low">1540</date>
         <country>France</country>
      </creation>
   </work>
</workList>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <creation>
         <date notbefore="1530" notafter="1550" cert="low">1540</date>
         <country>France</country>
      </creation>
   </work>
</workList>
```


#### Ville de composition

**Clé :** OPC

**Définition :** Ville de composition

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <creation>
         <date notbefore="1530" notafter="1550" cert="low">1540</date>
         <country>France</country>
         <settlement>Paris</settlement>
      </creation>
   </work>
</workList>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <creation>
         <date notbefore="1530" notafter="1550" cert="low">1540</date>
         <country>France</country>
         <settlement>Paris</settlement>
      </creation>
   </work>
</workList>
```


#### Nom du groupe des interprètes

**Clé :** MGN

**Définition :** Nom du groupe des interprètes

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <perfMedium>
         <castList>
            <castItem>Quatuor Voce</castItem>
         </castList>
      </perfMedium>
   </work>
</workList> 

**Autre option :** 

**Recommandations :** Je ne crois pas que cela soit nécessaire dans un header d'une édition critique.

**Exemple :**
```
<workList>
   <work>
      <perfMedium>
         <castList>
            <castItem>Quatuor Voce</castItem>
         </castList>
      </perfMedium>
   </work>
</workList> 
```


#### Nom de l'interprète

**Clé :** MPN

**Définition :** Nom de l'interprète

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <perfMedium>
         <castList>
            <castItem>Guillaume Becker</castItem>
         </castList>
      </perfMedium>
   </work>
</workList> 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <perfMedium>
         <castList>
            <castItem>Guillaume Becker</castItem>
         </castList>
      </perfMedium>
   </work>
</workList> 
```


#### Interprète soupçonné (?)

**Clé :** MPS

**Définition :** Interprète soupçonné (?)

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Date d'exécution/représentation

**Clé :** MRD

**Définition :** Date d'exécution/représentation

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Lieu d'exécution/représentation

**Clé :** MLC

**Définition :** Lieu d'exécution/représentation

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Nom du responsable de l'exécution/représentation (chef d'orchestre)

**Clé :** MCN

**Définition :** Nom du responsable de l'exécution/représentation (chef d'orchestre)

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Date de la première exécution/représentation

**Clé :** MPD

**Définition :** Date de la première exécution/représentation

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Titre de la collection

**Clé :** GTL

**Définition :** Titre de la collection

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Œuvre associée (ex. Stéphane Mallarmé, L’Après-midi d’un faune)

**Clé :** GAW

**Définition :** Œuvre associée (ex. Stéphane Mallarmé, L’Après-midi d’un faune)

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Désignation de la collection

**Clé :** GCO

**Définition :** Désignation de la collection

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### État de publication (ex. publié, pas encore publié, en cours de publication)

**Clé :** PUB

**Définition :** État de publication (ex. publié, pas encore publié, en cours de publication)

**Chapitre des Guidelines :** 

**Balise :** <sourceDesc>
   <source>
      <bibl>
         <unpub>En raison d'un manque de financement</unpub>
      </bibl>
   </source>

**Autre option :** 

**Recommandations :** En MEI, l'approche est à l'évidence très binaire : publié ou non. Nul besoin de le préciser si l'entité est bel et bien publiée (assez logique), mais par contre <unpub> est assez limité. Seul du texte est possible, expliquant les raisons de la non-publication. <unpub> peut d'ailleurs aussi aller dans <imprint> pour plus de précision sur le contexte de la non-publication (si celle-ci dépend de la maison d'édition).

**Exemple :**
```
<sourceDesc>
   <source>
      <bibl>
         <unpub>En raison d'un manque de financement</unpub>
      </bibl>
   </source>
```


#### Éditeur de la source utilisée pour l'édition digitale

**Clé :** PED

**Définition :** Éditeur de la source utilisée pour l'édition digitale

**Chapitre des Guidelines :** 

**Balise :** Si c'est une personne :
<sourceDesc>
   <source>
      <bibl>
         <editor>
           <persName auth="VIAF" auth.uri="https://viaf.org/viaf/12395760/">Paolo Fabri</persName>
         </editor>
      </bibl>
   </source>

**Autre option :** Si c'est une maison d'édition (cumulable) :
<sourceDesc>
     <source>
         <bibl>
            <imprint>
               <corpName>Edizioni Suvini Zerboni</corpName>
               <date>2000</date>
               <settlement auth="GeoNames" auth.uri="https://www.geonames.org/3173435/milan.html">Milano</settlement>
            </imprint>
         </bibl>
     </source>

**Recommandations :** 

**Exemple :**
```
Si c'est une personne :
<sourceDesc>
   <source>
      <bibl>
         <editor>
           <persName auth="VIAF" auth.uri="https://viaf.org/viaf/12395760/">Paolo Fabri</persName>
         </editor>
      </bibl>
   </source>
```


#### Premier éditeur

**Clé :** PPR

**Définition :** Premier éditeur

**Chapitre des Guidelines :** 

**Balise :** <sourceDesc>
   <source>
      <bibl>
         <editor xml:id="E1" n="1" precedes="#E2">
            <persName></persName>
         </editor>
         <editor xml:id="E2" n="2" follows="#E1">>
            <persName></persName>
         </editor>     
      </bibl>
   </source>

**Autre option :** Même logique s'il s'agit de la maison d'édition en utilisant <imprint>. Des dates peuvent également être ajoutées pour <editor> pour plus de précisions.

**Recommandations :** 

**Exemple :**
```
<sourceDesc>
   <source>
      <bibl>
         <editor xml:id="E1" n="1" precedes="#E2">
            <persName></persName>
         </editor>
         <editor xml:id="E2" n="2" follows="#E1">>
            <persName></persName>
         </editor>     
      </bibl>
   </source>
```


#### Date de la première publication

**Clé :** PDT

**Définition :** Date de la première publication

**Chapitre des Guidelines :** 

**Balise :** <sourceDesc>
   <source>
      <bibl>
         <edition xml:id="E1" n="1" precedes="#E2">
            <editor  n="1">
               <persName></persName>
            </editor>
            <date>1940</date>
         <edition xml:id="E2" n="2" follows="#E1">   
            <editor n="2">
               <persName></persName>
            </editor> 
            <date>1999</date> 
         </edition>     
      </bibl>
   </source>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<sourceDesc>
   <source>
      <bibl>
         <edition xml:id="E1" n="1" precedes="#E2">
            <editor  n="1">
               <persName></persName>
            </editor>
            <date>1940</date>
         <edition xml:id="E2" n="2" follows="#E1">   
            <editor n="2">
               <persName></persName>
            </editor> 
            <date>1999</date> 
         </edition>     
      </bibl>
   </source>
```


#### Titre de publication

**Clé :** PTL

**Définition :** Titre de publication

**Chapitre des Guidelines :** 

**Balise :** <sourceDesc>
   <source>
      <bibl>
         <title type="main"> Il nono libro de madrigali</title>
         <title type="subordinate">a cinque voci (1599)</title>  
      </bibl>
   </source>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<sourceDesc>
   <source>
      <bibl>
         <title type="main"> Il nono libro de madrigali</title>
         <title type="subordinate">a cinque voci (1599)</title>  
      </bibl>
   </source>
```


#### Lieu de publication

**Clé :** PPP

**Définition :** Lieu de publication

**Chapitre des Guidelines :** 

**Balise :** <sourceDesc>
   <source recordtype="c">
      <bibl>
         <composer>
           <persName auth="VIAF" auth.uri="https://viaf.org/viaf/2656905/">Luca Marenzio</persName>
         </composer>
         <title type="main"> Il nono libro de madrigali</title>
         <title type="subordinate">a cinque voci (1599)</title>
         <imprint>
            <corpName>Edizioni Suvini Zerboni</corpName>
            <date>2000</date>
            <settlement auth="GeoNames" auth.uri="https://www.geonames.org/3173435/milan.html">Milano</settlement>
         </imprint>
      </bibl>
   </source>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<sourceDesc>
   <source recordtype="c">
      <bibl>
         <composer>
           <persName auth="VIAF" auth.uri="https://viaf.org/viaf/2656905/">Luca Marenzio</persName>
         </composer>
         <title type="main"> Il nono libro de madrigali</title>
         <title type="subordinate">a cinque voci (1599)</title>
         <imprint>
            <corpName>Edizioni Suvini Zerboni</corpName>
            <date>2000</date>
            <settlement auth="GeoNames" auth.uri="https://www.geonames.org/3173435/milan.html">Milano</settlement>
         </imprint>
      </bibl>
   </source>
```


#### Numéro de catalogue de l'éditeur (ex. cotage)

**Clé :** PC#

**Définition :** Numéro de catalogue de l'éditeur (ex. cotage)

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Numéro de catalogue scientifique (abr.) [ex. BWV 551]

**Clé :** SCT

**Définition :** Numéro de catalogue scientifique (abr.) [ex. BWV 551]

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Numéro de catalogue scientifique (pas abr.) [ex. Koechel 117]

**Clé :** SCA

**Définition :** Numéro de catalogue scientifique (pas abr.) [ex. Koechel 117]

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Titre du manuscrit

**Clé :** SMS

**Définition :** Titre du manuscrit

**Chapitre des Guidelines :** 

**Balise :** <source recordtype="d">
  <bibl>
     <physLoc>
       <repository>
          <corpName>Bibliothèque nationale de France</corpName>
          <abbr>BnF</abbr>
       </repository>
     </physLoc>
     <relatedItem>
       <bibl>
          <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
          <abbr>Fr. 146</abbr>
          <title type="alternative">Roman de Fauvel</title>
          <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
       </bibl>
     </relatedItem>
  </bibl>
</source>

**Autre option :** <manifestation recordtype="d">
   <identifier>
      <title>Le Roman de Fauvel</title>
   </identifier>
   <langUsage>
      <language n="1">Français</language>
      <language n="2">Latin</language>
   </langUsage>   
   <itemList>
      <item recordtype="d">
         <physLoc>
            <repository>
               <corpName>Bibliothèque nationale de France</corpName>
               <abbr>BnF</abbr>
            </repository>
         </physLoc>
         <identifier>
            <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
            <abbr>Fr. 146</abbr>
            <title type="alternative">Roman de Fauvel</title>
            <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
         </identifier>  
         <availability>
            <accessRestrict>Non consultable en bibliothèque</accessRestrict>
         </availability> 
      </item>
   </itemList>

**Recommandations :** 

**Exemple :**
```
<source recordtype="d">
  <bibl>
     <physLoc>
       <repository>
          <corpName>Bibliothèque nationale de France</corpName>
          <abbr>BnF</abbr>
       </repository>
     </physLoc>
     <relatedItem>
       <bibl>
          <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
          <abbr>Fr. 146</abbr>
          <title type="alternative">Roman de Fauvel</title>
          <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
       </bibl>
     </relatedItem>
  </bibl>
</source>
```


#### Lieu de conservation du manuscrit

**Clé :** SML

**Définition :** Lieu de conservation du manuscrit

**Chapitre des Guidelines :** 

**Balise :** <source recordtype="d">
  <bibl>
     <physLoc>
       <repository>
          <corpName>Bibliothèque nationale de France</corpName>
          <abbr>BnF</abbr>
       </repository>
     </physLoc>
     <relatedItem>
       <bibl>
          <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
          <abbr>Fr. 146</abbr>
          <title type="alternative">Roman de Fauvel</title>
          <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
       </bibl>
     </relatedItem>
  </bibl>
</source>

**Autre option :** <manifestation recordtype="d">
   <identifier>
      <title>Le Roman de Fauvel</title>
   </identifier>
   <langUsage>
      <language n="1">Français</language>
      <language n="2">Latin</language>
   </langUsage>   
   <itemList>
      <item recordtype="d">
         <physLoc>
            <repository>
               <corpName>Bibliothèque nationale de France</corpName>
               <abbr>BnF</abbr>
            </repository>
         </physLoc>
         <identifier>
            <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
            <abbr>Fr. 146</abbr>
            <title type="alternative">Roman de Fauvel</title>
            <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
         </identifier>  
         <availability>
            <accessRestrict>Non consultable en bibliothèque</accessRestrict>
         </availability> 
      </item>
   </itemList>

**Recommandations :** 

**Exemple :**
```
<source recordtype="d">
  <bibl>
     <physLoc>
       <repository>
          <corpName>Bibliothèque nationale de France</corpName>
          <abbr>BnF</abbr>
       </repository>
     </physLoc>
     <relatedItem>
       <bibl>
          <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
          <abbr>Fr. 146</abbr>
          <title type="alternative">Roman de Fauvel</title>
          <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
       </bibl>
     </relatedItem>
  </bibl>
</source>
```


#### Info sur l'accès au manuscrit

**Clé :** SMA

**Définition :** Info sur l'accès au manuscrit

**Chapitre des Guidelines :** 

**Balise :** <source recordtype="d">
  <bibl>
     <physLoc>
       <repository>
          <corpName>Bibliothèque nationale de France</corpName>
          <abbr>BnF</abbr>
       </repository>
     </physLoc>
     <relatedItem>
       <bibl>
          <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
          <abbr>Fr. 146</abbr>
          <title type="alternative">Roman de Fauvel</title>
          <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
          <ref target="https://gallica.bnf.fr/ark:/12148/btv1b8454675g"/>
          <availability>
             <accessRestrict>Non consultable en bibliothèque</accessRestrict>
          </availability>
       </bibl>
     </relatedItem>     
  </bibl>
</source>

**Autre option :** <manifestation recordtype="d">
   <identifier>
      <title>Le Roman de Fauvel</title>
   </identifier>
   <langUsage>
      <language n="1">Français</language>
      <language n="2">Latin</language>
   </langUsage>   
   <itemList>
      <item recordtype="d">
         <physLoc>
            <repository>
               <corpName>Bibliothèque nationale de France</corpName>
               <abbr>BnF</abbr>
            </repository>
         </physLoc>
         <identifier>
            <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
            <abbr>Fr. 146</abbr>
            <title type="alternative">Roman de Fauvel</title>
            <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
         </identifier>  
         <availability>
            <accessRestrict>Non consultable en bibliothèque</accessRestrict>
         </availability> 
      </item>
   </itemList>

**Recommandations :** 

**Exemple :**
```
<source recordtype="d">
  <bibl>
     <physLoc>
       <repository>
          <corpName>Bibliothèque nationale de France</corpName>
          <abbr>BnF</abbr>
       </repository>
     </physLoc>
     <relatedItem>
       <bibl>
          <identifier auth="BnF" auth.uri="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc45158c">Français 146</identifier>
          <abbr>Fr. 146</abbr>
          <title type="alternative">Roman de Fauvel</title>
          <locus label="folio" from="1r" to="2r">ff. 1r-2r</locus>
          <ref target="https://gallica.bnf.fr/ark:/12148/btv1b8454675g"/>
          <availability>
             <accessRestrict>Non consultable en bibliothèque</accessRestrict>
          </availability>
       </bibl>
     </relatedItem>     
  </bibl>
</source>
```


#### Éditeur de l'édition électronique 

**Clé :** YEP

**Définition :** Éditeur de l'édition électronique 

**Chapitre des Guidelines :** 

**Balise :** <fileDesc>
  <titleStmt>
    <respStmt>
       <persName xml:id="VB" role="editor" auth="Orcid" auth.uri="...">XXX</persName>
    </respStmt>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<fileDesc>
  <titleStmt>
    <respStmt>
       <persName xml:id="VB" role="editor" auth="Orcid" auth.uri="...">XXX</persName>
    </respStmt>
```


#### Date et propriétaire du copyright de l'édition électronique

**Clé :** YEC

**Définition :** Date et propriétaire du copyright de l'édition électronique

**Chapitre des Guidelines :** 

**Balise :** <pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <date>2024</date>
     </useRestrict>
   </availability>
</pubStmt>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <date>2024</date>
     </useRestrict>
   </availability>
</pubStmt>
```


#### Date de mise à disposition de l'édition électronique

**Clé :** YER

**Définition :** Date de mise à disposition de l'édition électronique

**Chapitre des Guidelines :** 

**Balise :** <pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <date>2024</date>
     </useRestrict>
     <date isodate="2024-01-02">01/02/24</date>
   </availability>
</pubStmt>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <date>2024</date>
     </useRestrict>
     <date isodate="2024-01-02">01/02/24</date>
   </availability>
</pubStmt>
```


#### License

**Clé :** YEM

**Définition :** License

**Chapitre des Guidelines :** 3.4.1.3 Publication, Distribution, etc.

**Balise :** <pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <date>2024</date>
        <head>Licence</head>
        <p>CC-BY-NC</p>
     </useRestrict>
     <date isodate="2024-01-02">01/02/24</date>
   </availability>
</pubStmt>

**Autre option :** <pubStmt xml : id…>
    <availability xml : id…>
       <useRestrict xml : id…>Licence:... </useRestrict>
    </availability>
</pubStmt>

**Recommandations :** 

**Exemple :**
```
<pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <date>2024</date>
        <head>Licence</head>
        <p>CC-BY-NC</p>
     </useRestrict>
     <date isodate="2024-01-02">01/02/24</date>
   </availability>
</pubStmt>
```


#### Pays de copyright

**Clé :** YEN

**Définition :** Pays de copyright

**Chapitre des Guidelines :** 

**Balise :** <pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <country>France</country>
        <date>2024</date>
        <head>Licence</head>
        <p>CC-BY-NC</P>
     </useRestrict>
     <date isodate="2024-01-02">01/02/24</date>
   </availability>
</pubStmt>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <country>France</country>
        <date>2024</date>
        <head>Licence</head>
        <p>CC-BY-NC</P>
     </useRestrict>
     <date isodate="2024-01-02">01/02/24</date>
   </availability>
</pubStmt>
```


#### Document d'origine de l'édition électronique

**Clé :** YOR

**Définition :** Document d'origine de l'édition électronique

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** Donc une source ? <sourceDesc ?> 

**Exemple :**
```

```


#### Propriétaire du document d'origine

**Clé :** YOO

**Définition :** Propriétaire du document d'origine

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Année du copyright originaire

**Clé :** YOE

**Définition :** Année du copyright originaire

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Éditeur du document d'origine

**Clé :** EED

**Définition :** Éditeur du document d'origine

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Éditeur de l'édition électronique (encodeur?)

**Clé :** ENC

**Définition :** Éditeur de l'édition électronique (encodeur?)

**Chapitre des Guidelines :** 

**Balise :** <fileDesc>
  <titleStmt>
    <respStmt>
       <persName xml:id="VB" role="encoder" auth="Orcid" auth.uri="...">XXX</persName>
    </respStmt>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<fileDesc>
  <titleStmt>
    <respStmt>
       <persName xml:id="VB" role="encoder" auth="Orcid" auth.uri="...">XXX</persName>
    </respStmt>
```


#### Date d'encodage de l'édition électronique

**Clé :** END

**Définition :** Date d'encodage de l'édition électronique

**Chapitre des Guidelines :** 

**Balise :** <encodingDes>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<encodingDes>
```


#### Modification du document électronique

**Clé :** EMD

**Définition :** Modification du document électronique

**Chapitre des Guidelines :** 

**Balise :** <encodingDes>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<encodingDes>
```


#### Version de l'édition électronique

**Clé :** EEV

**Définition :** Version de l'édition électronique

**Chapitre des Guidelines :** 

**Balise :** <encodingDes>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<encodingDes>
```


#### Numéro du fichier électronique

**Clé :** EFL

**Définition :** Numéro du fichier électronique

**Chapitre des Guidelines :** 

**Balise :** <encodingDes>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<encodingDes>
```


#### État de l'encodage

**Clé :** EST

**Définition :** État de l'encodage

**Chapitre des Guidelines :** 

**Balise :** <encodingDes>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<encodingDes>
```


#### Désignation de la collection

**Clé :** ACO

**Définition :** Désignation de la collection

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Désignation de la forme

**Clé :** AFR

**Définition :** Désignation de la forme

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Désignation du genre musical

**Clé :** AGN

**Définition :** Désignation du genre musical

**Chapitre des Guidelines :** 3.4.1.5 Notes Statement

**Balise :** <workList>
   <work>
      <classification xml :id="…">
         <termList xml:id="…">
            <term label="music genre" xml:id="…">...</term>
         </termList>
      </classification>

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <classification xml :id="…">
         <termList xml:id="…">
            <term label="music genre" xml:id="…">...</term>
         </termList>
      </classification>
```


#### Désignation du style/période/typologie de l'œuvre

**Clé :** AST

**Définition :** Désignation du style/période/typologie de l'œuvre

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <creation xml:id="…">
         <periodName>Contemporary music</periodName>
         <styleName>Minimalist</styleName>
      </creation>
   </work>
</workList>   

**Autre option :** 

**Recommandations :** 

**Exemple :**
```
<workList>
   <work>
      <creation xml:id="…">
         <periodName>Contemporary music</periodName>
         <styleName>Minimalist</styleName>
      </creation>
   </work>
</workList>   
```


#### Classification du mode (Moyen âge et Renaissance)

**Clé :** AMD

**Définition :** Classification du mode (Moyen âge et Renaissance)

**Chapitre des Guidelines :** 

**Balise :** <workList>
   <work>
      <key mode="dorian">
      <creation xml:id="…">
         <periodName>Contemporary music</periodName>
         <styleName>Minimalist</styleName>
      </creation>
   </work>
</workList>  

**Autre option :** 

**Recommandations :** En MEI, cela semble être une donnée à renseigner dans <key>, donc dans <work> ou <expression>, avec @mode. L'information peut également se retrouver dans la définition des portées. Il y a trois vocabulaires contrôlés MEI pour les modes. Voir data.mode.

**Exemple :**
```
<workList>
   <work>
      <key mode="dorian">
      <creation xml:id="…">
         <periodName>Contemporary music</periodName>
         <styleName>Minimalist</styleName>
      </creation>
   </work>
</workList>  
```


#### Classification métrique

**Clé :** AMT

**Définition :** Classification métrique

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Effectif

**Clé :** AIN

**Définition :** Effectif

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Origine géographique de l'œuvre

**Clé :** ARE

**Définition :** Origine géographique de l'œuvre

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Localisation géographique de l'œuvre

**Clé :** ARL

**Définition :** Localisation géographique de l'œuvre

**Chapitre des Guidelines :** 

**Balise :** 

**Autre option :** 

**Recommandations :** 

**Exemple :**
```

```


#### Encoding Sources in MEI (3.7) - Encodage des sources en MEI



**On utilise 0 lorsque l'on est en presence de la source originale (normalement l'autographe de l'œuvre) et oméga "⍵" lorsque la source originale de l'œuvre ne nous est pas parvenue**

- _fileDesc_
   - **Idem**
- _sourceDesc_ Ce module est l'élément central de notre protocole, puisque qu'il s'agit de la partie où nous décrivons de manière exacte le contenu scientifique. Selon les _guidelines_ MEI, il n'y a pas de renvoi au modèle FRBR au sein de _workList_. Il faut donc déployer le modèle FRBR à cet endroit.
   - _expressionList_ : il s'agit de nommer et détailler les différentes expressions, cette étape correspondant à notre protocole à la _recesio_ et donc à un discours commun aux théories de Lachmann et Bédier. Nous avons fait le choix de nommer l'expression de tradition directe _expression 0_. Les expressions indirectes se déploient ensuite avec des chiffres (1,2 _etc_) ou bien des noms en toutes lettres.
   - _manifestationList_ : de manière similaire à _expressionList_, nous nommons le manuscrit autographe (ou l'_omega_ issu du _stemma codicum_ si l'on ne possède pas l'autographe) _manifestation 0_. Pour chaque expression il convient d'utiliser une instance de _manifestationList_ et pour chaque manifestation un _itemList_. Dans le cadre de manuscrits, la manifestation et l'item ne font qu'un. Par ailleurs, il n'y a pas, pour des raisons de catalogage évidentes, d'_item 0_ ; nous partons donc du principe que la dénomination des items fait appel au bon sens des chercheur·euse·s, de la tradition et des nomenclatures en usage.
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

ThB présentation générale de LRM + un paragraphe sur la réflexion entre BDD sémantique centralisée vs l’information sémantisée dans les headers MEI

 

 - - -

Faire valider par Kévin pour la place du modèle FRBR, pour nous c'est dans <workList>
Marco a donné des gens à contacter pour partager tout ça : Laurent Pugin, Johannes Kepper (va s'opposer ; attention on tient aux protocoles pour l'interopérabilité) 
