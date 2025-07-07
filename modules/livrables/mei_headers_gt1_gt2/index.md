## Approches de la complétion des Headers MEI par les GT1&GT2 du Consortium-HN Musica2
Bottini, T. (CNRS, IReMus), Braud, A. (CNRS, RicercarLab), Gurrieri, M. (CNRS, IReMus), Roger, K. (ULorraine, CRULH)

### 1. Présentation générale de l'approche méthodologique

Ce document didactique élaboré dans le cadre du consortium Huma-Num Musica2 vise à proposer un protocole détaillé de renseignement des métadonnées au sein des headers MEI (Music Encoding Initiative), plus particulièrement dans le cadre d'éditions critiques numériques. L’objectif est d'établir un guide dédié aux éditions encodées en MEI et de préciser où disposer les informations éditoriales et philologiques nécessaires, en proposant des choix raisonnés palliant diverses ambiguïtés présentes dans les guidelines MEI. Fixer des paramètres partagés et reconnus par la communauté musicologique permettra de créer des fichiers MEI qui pourront être contrôlés, vérifiés et échangés au profit de la transparence scientifique et de l'interopérabilité. 

L'édition critique pose un nombre significatif de problèmes, notamment dans les cas où il est nécessaire de marquer la différence entre tradition directe (tous les exemplaires transmettant le texte sous sa forme originelle) ou indirecte (exemplaires qui témoignent d'une tradition en parallèle : les traductions, les commentaires, les parodies, etc...). Ces derniers sont particulièrement utiles lorsqu'un texte est corrompu, car ils donnent une fenêtre sur un moment historique précis où le texte était intouché. 

Dans le cas précis de l'édition musicale, les problématiques d'arrangement, de transcription d'une formation instrumentale à une autre ainsi que la reconstruction des voix posent des problèmes conséquents qui justifient une approche détaillée bien que parfois redondante.

### 2. Les possibilités supplémentaires du modèle FRBR 

L’interopérabilité des éditions critiques encodées en MEI repose sur l’adoption de normes partagées qui garantissent la cohérence et la compatibilité des fichiers produits. Actuellement, la grande liberté laissée aux encodeurs pour le renseignement des métadonnées dans le header MEI peut nuire à cette interopérabilité, en raison de choix individuels et des interprétations subjectives qui en résultent. Une telle hétérogénéité complique non seulement l’échange et l’exploitation des données, mais compromet également la transparence scientifique, un impératif fondamental des éditions critiques. Ce guide propose ainsi des exemples d'encodage standards ayant fait leurs preuves au sein de projets variés, mais également des alternatives s'inspirant de la norme FRBR ainsi que, le cas échéant, des alignements avec les clés de métadonnées HUMDRUM. Pour illustrer concrètement ces recommandations, des exemples détaillés sont intégrés au repository, accompagnés d’un modèle vierge prêt à l’emploi. 

Notre protocole de complétion des headers est présenté de manière logique en abordant dans un premier temps les informations liées au fichier MEI encodé, ensuite à la définition de l'œuvre en elle-même avant de détailler la source. Bien que cette information ne respecte pas l'ordre des Guidelines MEI, elle nous semble conceptuellement logique et permet de révéler l'intérêt du modèle FRBR dans certains cas complexes de l'édition critique musicale.

Historiquement, les besoins de l'édition critique textuelle se sont structurés à partir de deux modèles philologiques principaux : celui de Karl Lachmann dit méthode _stemmatique_, basé sur un processus d'élimination des erreurs communes entre les manuscrits, et celui de Bédier qui vise à l'usage d'un témoin unique. Ces méthodes et leurs dérivés convergent toutes vers la première étape nécessaire de la _recensio_, soit l'identification des sources et l'étude de la tradition. Dans le cadre de la présentation de notre protocole de renseignement des métadonnées au sein des headers MEI pour l'établissement d'éditions critiques, nous prenons donc appui sur la _recensio_, qui est renseignée soit de manière "classique" en MEI à travers _sourceDesc_, soit en suivant les différents états induits par le modèle FRBR. 

Les quatre états de l'œuvre en FRBR sont légérèment adaptés en MEI, puisque "manifestation" devient _source_, tandis que _work_, _expression_ et _item_ restent inchangés. Chacun de ces éléments possède des balises "enfants" permettant de lister les différentes instanciations :

   - _expressionList_ : il s'agit de nommer et détailler les différentes expressions, cette étape correspondant à notre protocole à la _recensio_ et donc à un discours commun aux théories de Lachmann et Bédier. Nous avons fait le choix de nommer l'expression de tradition directe _expression 0_. On utilise 0 lorsque l'on est en presence de la source originale (normalement l'autographe de l'œuvre) et oméga "⍵" lorsque la source originale de l'œuvre ne nous est pas parvenue Les expressions indirectes se déploient ensuite avec des chiffres (1,2 _etc_) ou bien des noms en toutes lettres. Pour chaque expression il convient d'utiliser une instance de _sourceList_ et pour chaque manifestation un _itemList_. Dans le cadre de manuscrits, la manifestation et l'item ne font qu'un.
   - _sourceList_ : de manière similaire à _expressionList_, nous nommons le manuscrit autographe (ou l'_omega_ issu du _stemma codicum_ si l'on ne possède pas l'autographe) _source 0_. 
   - _itemList_ : il n'y a pas, pour des raisons de catalogage évidentes, d'_item 0_ ; nous partons donc du principe que la dénomination des items fait appel au bon sens des chercheur·euse·s, de la tradition et des nomenclatures en usage.

Le fichier MEI que nous sommes en train de renseigner constitue d'ailleurs une autre manifestation de l'œuvre, et doit par conséquent faire partie de la _sourceList_. Des xmlID seront utilisés pour chaque manifestation et item, afin d'assurer une inter-opérabilité maximale. Les normes FRBR ainsi intégrées de la MEI correspondent précisement à la _recensio_ la plus complète possible, ce qui est la promesse méthodologique de chaque édition critique. L'emploi du modèle FRBR est ainsi particulièrement adapté à des œuvres éditées sous forme de conducteur d'orchestre puis de parties séparées, qui nécessitent par exemple de détailler les caractéristiques de chacune des éditions, ici qualifiées de "sources" (équivalent FRBR - MEI). Pour des éditions plus simples, il convient de faire preuve de bon sens et de privilégier les solutions natives à la MEI.

Il est également important de noter que notre protocole s'appuie sur un principe de redondance : toutes les informations nécessaires doivent être renseignées à chaque niveau du header et, le cas échéant, du modèle FRBR. Il est ainsi probable que des métadonnées soient régulièrement répétées, par exemple le nom du compositeur ou le titre de l’œuvre.

### 3. Description du fichier MEI encodé <fileDesc>

#### Titre de l'édition MEI

Clé HUMDRUM : ≈ OTL

Définition : Numéro

Chapitre des Guidelines : 3.3.1. Title Statement

Balise :`<title type=main>`/`<title type="subordinate">`

Autre option : `<title>`

Recommandations : Le titre est une information souvent ambiguë dans les éditions numériques en raison de la confusion qui règne entre le titre de l'oeuvre complète, le titre de la partie encodée ou encore le titre de l'édition. D'ailleurs, le vocabulaire Humdrum ne dispose pas de clé spécifique pour cette dernière valeur (OTL est le titre de l'oeuvre). En MEI, dans <fileDesc>, les usages sont nombreux et divergent. Pourtant, il est manifeste que <title> se réfère ici au titre de l'édition numérique qui peut être distinct du titre de l'oeuvre encodée. En pratique, ces deux niveaux de titres se superposent souvent. Ainsi, pour distinguer le titre de l'édition et celui de la pièce (proprement encodé dans <workList>), nous proposons d'observer l'un des conseils donnés dans les guidelines tout en en uniformisant l'encodage. Ainsi, le <title> principal est suivi d'un <title> subordonné précisant que l'objet est ici l'édition numérique et non l'oeuvre en elle-même.

Exemple :
```
<fileDesc xml:id="...">
   <titleStmt xml:id="...">
      <title type="main">Pavane</title>
      <title type="subordinate">A Digital Edition</title>
   </titleStmt>
</fileDesc>
```
Recommandations : Dans <fileDesc>, il n'est pas nécessaire que le titre dispose d'une granularité fine comparable au renseignement du titre de l'oeuvre dans <workList>. Il n'existe cependant aucune restriction. Le plus important est de rester vigilant quant à la hiérarchie des titres spécifiée à l'aide de l'attribut @title dont les valeurs sont contrôlées (pour plus d'information sur les niveaux de titres, voir "Titre alternatif de l'oeuvre"). 

#### Éditeur de l'édition électronique 

Clé HUMDRUM : YEP

Définition : Éditeur de l'édition électronique 

Chapitre des Guidelines : 

Balise : <fileDesc>
  <titleStmt>
    <respStmt>
       <persName xml:id="VB" role="editor" auth="Orcid" auth.uri="...">XXX</persName>
    </respStmt>

Autre option : 

Recommandations : 

Exemple :
```
<fileDesc>
  <titleStmt>
    <respStmt>
       <persName xml:id="VB" role="editor" auth="Orcid" auth.uri="...">XXX</persName>
    </respStmt>
```

#### Date et propriétaire du copyright de l'édition électronique

Clé HUMDRUM : YEC

Définition : Date et propriétaire du copyright de l'édition électronique

Chapitre des Guidelines : 

Balise : <pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <date>2024</date>
     </useRestrict>
   </availability>
</pubStmt>

Autre option : 

Recommandations : 

Exemple :
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

#### Éditeur de l'édition électronique (encodeur?)

Clé HUMDRUM : ENC

Définition : Éditeur de l'édition électronique (encodeur?)

Chapitre des Guidelines : 

Balise : <fileDesc>
  <titleStmt>
    <respStmt>
       <persName xml:id="VB" role="encoder" auth="Orcid" auth.uri="...">XXX</persName>
    </respStmt>

Autre option : 

Recommandations : 

Exemple :
```
<fileDesc>
  <titleStmt>
    <respStmt>
       <persName xml:id="VB" role="encoder" auth="Orcid" auth.uri="...">XXX</persName>
    </respStmt>
```

#### Date d'encodage de l'édition électronique

Clé HUMDRUM : END

Définition : Date d'encodage de l'édition électronique

Chapitre des Guidelines : 

Balise : <encodingDes>

Autre option : 

Recommandations : 

Exemple :
```
<encodingDes>
```

#### Modification du document électronique

Clé HUMDRUM : EMD

Définition : Modification du document électronique

Chapitre des Guidelines : 

Balise : <encodingDes>

Autre option : 

Recommandations : 

Exemple :
```
<encodingDes>
```

#### Version de l'édition électronique

Clé HUMDRUM : EEV

Définition : Version de l'édition électronique

Chapitre des Guidelines : 

Balise : <encodingDes>

Autre option : 

Recommandations : 

Exemple :
```
<encodingDes>
```

#### Numéro du fichier électronique

Clé HUMDRUM : EFL

Définition : Numéro du fichier électronique

Chapitre des Guidelines : 

Balise : <encodingDes>

Autre option : 

Recommandations : 

Exemple :
```
<encodingDes>
```

#### État de l'encodage

Clé HUMDRUM : EST

Définition : État de l'encodage

Chapitre des Guidelines : 

Balise : <encodingDes>

Autre option : 

Recommandations : 

Exemple :
```
<encodingDes>
```

#### Désignation de la collection

Clé HUMDRUM : ACO

Définition : Désignation de la collection

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :

#### Désignation de la forme

Clé HUMDRUM : AFR

Définition : Désignation de la forme

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :

#### Date de mise à disposition de l'édition électronique

Clé HUMDRUM : YER

Définition : Date de mise à disposition de l'édition électronique

Chapitre des Guidelines : 

Balise : <pubStmt>
   <availability>
     <useRestrict>
        <persName>...</persName>
        <corpName>...</corpName>
        <date>2024</date>
     </useRestrict>
     <date isodate="2024-01-02">01/02/24</date>
   </availability>
</pubStmt>

Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : YEM

Définition : License

Chapitre des Guidelines : 3.4.1.3 Publication, Distribution, etc.

Balise : <pubStmt>
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

Autre option : <pubStmt xml : id…>
    <availability xml : id…>
       <useRestrict xml : id…>Licence:... </useRestrict>
    </availability>
</pubStmt>

Recommandations : 

Exemple :
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

Clé HUMDRUM : YEN

Définition : Pays de copyright

Chapitre des Guidelines : 

Balise : <pubStmt>
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

Autre option : 

Recommandations : 

Exemple :
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

### Description de l'œuvre musicale <worklist

#### Titre de l'œuvre musicale

Clé HUMDRUM : ≈ OTL

Définition : Numéro

Chapitre des Guidelines : 3.3.1. Title Statement

Balise :`<title type=main>`/`<title type="subordinate">`

Autre option : `<title>`

Recommandations : Les deux exemples ci-dessous explicitent l'inscription du titre de l'œuvre dans un premier temps au niveau de l'œuvre elle-même, puis au niveau de son expression.

Exemples :
```
"<workList xml:id=""..."">
   <work xml:id=""..."">
      <title xml:id=""..."">...</title>
   </work>
</workList>"
```
```
"<workList xml:id=""..."">
   <work xml:id=""..."">
      <title xml:id=""..."">  
      <expressionList xml:id=""..."">  
        <expression xml:id=""..."">
        </expression>
      </expressionList>
      </title>
   </work>
</workList>"
```
#### Compositeur de l'offre musicale

Clé HUMDRUM : COM

Définition : Indique le nom du compositeur de l'œuvre.

Chapitre des Guidelines : 3.6 Work Description

Balise : `<composer>`

Autre option : `<persName role="creator">`

Recommandations : Le ou les compositeurs renseignés ici ne concernent que l'oeuvre encodée dans le fichier MEI et non une oeuvre tierce. À noter également que la valeur de rôle est libre. Toutefois, il est conseillé de suivre un thesaurus ou un vocabulaire contrôlé dans un souci de standardisation tels que VIAFF. Pour finir, nous préconisons de renseigner un URI identifiant l'individu concerné sur le web afin d'améliorer l'interopérabilité des métadonnées (ici aussi, préciser). 

Exemples :
```
<workList xml:id=""..."">
   <work xml:id=""..."">
      <composer xml:id=""..."">
          <persName role=""creator"" (""composer"") auth.uri=""http://..."">...</persName>
      </composer>
   </work>
</workList>
```
```
"<workList xml:id=""..."">
   <work xml:id=""..."">
      <expressionList xml:id=""..."">  
        <expression xml:id=""..."">
          <composer xml:id=""..."">
            <persName role=""creator"" (""composer""?) auth.uri=""http://..."">...</persName>
          </composer>
        </expression>
      </expressionList>
   </work>
</workList>"
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

Clé HUMDRUM : COS

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

Clé HUMDRUM : COL

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

Balise (dans le cas d'un traducteur historique, propre à l'oeuvre encodée) : `<contributor>`/`<persName>`

Autre option (dans le cas d'un traducteur ad hoc, pour l'édition numérique ou l'édition moderne utilisée comme source) : `<respStmt>`/`<persName>`

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

Balise :`<title>`

Autre option : -

Recommandations : Cette manière minimale de renseigner le titre convient surtout aux titres officiels et consensuels des oeuvres - des titres qui ne font pas l'objet d'ambiguité. Pour le renseignement de titres alternatifs ou populaires, voir plus bas.

Exemple :

Titre simple d'une oeuvre :
```
<workList xml:id="...">
   <work xml:id="...">
      <title xml:id="...">Pavane pour une infante défunte</title>
   </work>
</workList>
```

Recommandation : Dans le cas de sections ou de mouvements d'une oeuvre, il est nécessaire de faire une distinction entre le titre de la partie encodée et l'oeuvre globale. Pour cela, il est nécessaire d'utiliser l'attribut @type et la valeur "uniform". De même, afin de mieux catégoriser les différents niveaux de titres, il est conseillé d'employer <titlePart>. La valeur "subordinate" peut être pratique pour hiérarchiser les divers syntagmes d'un même niveau de titre, comme le mouvement ou numéro d'opus.

#### Titre d'un mouvement d'une oeuvre :

```
<workList xml:id="...">
   <work xml:id="...">
      <title type="main">Rondo alla Turca</title>
      <title type="subordinate" label="movement">Allegretto</title>
      <titlePart>
         <title type="uniform">Sonate pour piano no. 11 en la majeur</title>
         <title type="subordinate" label="Köchel">K. 331/300</title>
      </titlePart>
   </work>
</workList>
```
Recommandation : Il est à noter que le renseignement du titre, métadonnée de première importance, est paradoxalement négligé dans les guidelines MEI. Divers exemples suggèrent une distinction minimale des niveaux de titres et une certaine liberté dans leur troncation. La raison réside certainement dans l'ambiguïté qui dérive des différentes formes de titres et de leurs usages multiples. Bien que @type soit régi par les valeurs contrôlées listées ci-dessus, les guidelines illustrent à l'occasion l'usage non conventionnel de @type="subtitle" pour encoder un syntagme subordonné au titre principal. Nous nous limiterons ici aux seuls vocables contrôlés précisés précédemment.

#### Titre courant de l'oeuvre

Clé HUMDRUM : OTP

Définition : Titre populaire de l'oeuvre encodée.

Chapitre des Guidelines : -  

Balise : `<title type="alternative">`

Autre option : -

Recommandations : Le titre courant peut facilement se confondre avec le titre alternatif (voir ci-dessous). Sur ce point, seuls les usages peuvent apporter des réponses. Dans le doute, il est préférable de privilégier le titre alternatif, moins restrictif que le sens sous-entendu par titre "courant". Par ailleurs, @type dispose de valeurs contrôlées en MEI ("main", "subordinate", "abbreviated", "alternative", "translated", "uniform" et "desc") parmi lesquelles aucune ne couvre l'acception d'un titre "populaire". Pour l'usage de ces valeurs, voir ci-dessous dans "Titre alternatif de l'oeuvre"

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <title type="main">Rondo alla Turca</title>
      <title type="subordinate" label="movement">Allegretto</title>
      <title type="alternative">Marche Turque</title>
      <titlePart>
         <title type="uniform">Sonate pour piano no. 11 en la majeur</title>
         <title type="subordinate" label="Köchel">K. 331/300</title>
      </titlePart>
   </work>
</workList>
```

#### Titre alternatif de l'oeuvre

Clé HUMDRUM : OTA

Définition : Autre titre de l'oeuvre encodée, distinct du titre principal.

Chapitre des Guidelines : - 

Balise : `<title type="alternative">`

Autre option, en fonction du contexte : `<title type="subordinate">`; `<title type="abbreviated">`; `<title type="translated">`; `<title type="uniform">`; `<title type="desc">`

Recommandations : Comme dit plus haut, l'attribut "alternative" demeure le plus simple pour renseigner un titre différent du titre officiel de l'oeuvre encodée. Toutefois, l'attribut @type dispose d'autres valeurs contrôlées, listées précédemment, qui peuvent affiner la nature du titre renseigné. Ainsi, dans l'exemple ci-dessous, apparaissent deux niveaux de titres (titre du mouvement encodé et titre de l'oeuvre globale) ainsi que leurs diverses formes potentielles.

Exemple :
```
<workList xml:id="...">
   <work xml:id="...">
      <title type="main">Rondo alla Turca</title>
      <title type="subordinate" label="movement">Allegretto</title>
      <title type="abbreviated">Alla Turca</title>
      <title type="alternative">Marche Turque</title>
      <titlePart>
         <title type="uniform">Sonate pour piano no. 11 en la majeur</title>
         <title type="subordinate" label="Köchel">K. 331/300</title>
         <title type="translated" xml:lang="DE">Sonate Nr. 11 A-Dur</title>
         <title type="desc">Sonate pour piano très connue de Mozart</title>
      </titlePart>
   </work>
</workList>
```

#### Titre de l'œuvre d'appartenance

Clé HUMDRUM : OPR

Définition : Titre de l'œuvre globale dans le cas d'une section ou d'un mouvement.

Chapitre des Guidelines : 

Balise : `<title type="main">` ; `<title type="uniform">`

Autre option : 

Recommandations : Comme dit précédemment, si diverses formes de titre sont retenues dans l'édition, il est conseillé de structurer les différents niveaux à l'aide de <titlePart>, surtout si des valeurs semblables pour @type sont utilisées à la fois pour le titre du mouvement et pour le titre de l'oeuvre d'appartenance. Dans l'exemple ci-dessous, la description minimale ne nécessite pas une telle distinction.  

Exemple :
```
<workList>
   <work>
      <title type="main">Rondo alla Turca</title>
      <title type="abbreviated">Alla Turca</title>
      <title type="alternative">Marche Turque</title>
      <title type="uniform">Sonate pour piano no. 11 en la majeur</title>
   </work>
</workList>  
```

#### Numéro d'opus

Clé HUMDRUM : OPS

Définition : Numéro d'opus de l'oeuvre d'appartenance de l'oeuvre encodée.

Chapitre des Guidelines : 3.3.1 Title Statement

Balise : `<title type="uniform">`/`<title type="subordinate" label="opus">`

Autre option : `<identifier label="opus">`

Recommandations : Nous envisageons le numéro d'opus comme un syntagme du titre de l'oeuvre d'appartenance. Ainsi, nous recommandons de l'encoder à l'aide d'une balise <title> et du @type="subordinate", tout en précisant le @label pour plus de clarté. Toutefois, les guidelines MEI semblent privilégier <identifier>, utilisé comme élément enfant de <title>. Nous proposons cette possibilité comme une option alternative, bien que celle-ci apparaisse structurellement discutable, notamment au regard du sens particulièrement vague de l'élément <identifier> ("Examples include an International Standard Book/Music Number, Library of Congress Control Number, publisher’s number, a personal identification number, an entry in a bibliography or catalog, etc."). Nous conseillons a minima de bien préciser chaque fois @label="opus". 

Exemple :
```
<workList>
   <work>
      <title type="main">Prélude en do majeur</title>
      <titlePart>
         <title type="uniform">Vingt-quatre Préludes pour piano</title>
         <title type="subordinate" label="opus">28</title>
      <titlePart>
   </work>
</worklist> 
```

#### Dédicace

Clé HUMDRUM : ODE

Définition : Dédicace

Chapitre des Guidelines : 

Balise : <workList>
   <work>
      <creation>
         <dedicatee>
            <persName>...</persName>
         </dedicatee>
      </creation>
   </work>
<workList>  

Autre option : Ou si nous souhaitons ajouter plus d'informations sur la dédicace elle-même et son contexte:

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

Recommandations : 

Exemple :
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

Clé HUMDRUM : OCO

Définition : Committant (commettant ?)

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```

#### Collectionneur ?

Clé HUMDRUM : OCL

Définition : Collectionneur ?

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Note de format libre / Nota bene

Clé HUMDRUM : ONB

Définition : Note de format libre / Nota bene

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : Cela se trouverait dans <notesStmt> puis <annot> (pour le header).

Exemple :
```

```

#### Date de composition

Clé HUMDRUM : ODT

Définition : Date de composition de l'oeuvre encodée.

Chapitre des Guidelines : 3.5.6 Work History

Balise : <creation>/<date>

Autre option : 

Recommandations : La date de composition peut aussi être nuancée ou approchée à l'aide d'attributs, surtout dans le cas d'une date incertaine. En MEI, la date renseignée dans les attributs doit suivre la norme ISO 8601 (AAAA-MM-JJ). La valeur de la balise <date> est  libre pour sa part. Plusieurs usages se rencontrent d'ailleurs dans les guidelines ("June 1987"; "2011"). Nous conseillons toutefois de suivre au maximum la norme ISO (AAAA ; AAAA-MM ou AAAA-MM-JJ) pour assurer sa bonne compréhension. Par ailleurs, le niveau de certitude accordé à une date peut également être précisé à l'aide de l'attribut @cert dont les valeurs sont "high", "medium", "low" et "unknown".

Exemple :
```
<workList>
   <work>
      <creation>
         <date notbefore="1530-01-01" notafter="1550-01-01" cert="low">1540</date>
      </creation>
   </work>
</workList>
```


#### Pays de composition de l'oeuvre encodée

Clé HUMDRUM : OCY

Définition : Pays dans lequel l'oeuvre encodée à été composée. 

Chapitre des Guidelines : 

Balise : <creation>
         <date notbefore="1530" notafter="1550" cert="low">1540</date>
         <country>France</country>
      </creation>


Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : OPC

Définition : Ville de composition

Chapitre des Guidelines : 

Balise : <workList>
   <work>
      <creation>
         <date notbefore="1530" notafter="1550" cert="low">1540</date>
         <country>France</country>
         <settlement>Paris</settlement>
      </creation>
   </work>
</workList>

Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : MGN

Définition : Nom du groupe des interprètes

Chapitre des Guidelines : 

Balise : <workList>
   <work>
      <perfMedium>
         <castList>
            <castItem>Quatuor Voce</castItem>
         </castList>
      </perfMedium>
   </work>
</workList> 

Autre option : 

Recommandations : Je ne crois pas que cela soit nécessaire dans un header d'une édition critique.

Exemple :
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

Clé HUMDRUM : MPN

Définition : Nom de l'interprète

Chapitre des Guidelines : 

Balise : <workList>
   <work>
      <perfMedium>
         <castList>
            <castItem>Guillaume Becker</castItem>
         </castList>
      </perfMedium>
   </work>
</workList> 

Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : MPS

Définition : Interprète soupçonné (?)

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Date d'exécution/représentation

Clé HUMDRUM : MRD

Définition : Date d'exécution/représentation

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Lieu d'exécution/représentation

Clé HUMDRUM : MLC

Définition : Lieu d'exécution/représentation

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Nom du responsable de l'exécution/représentation (chef d'orchestre)

Clé HUMDRUM : MCN

Définition : Nom du responsable de l'exécution/représentation (chef d'orchestre)

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Date de la première exécution/représentation

Clé HUMDRUM : MPD

Définition : Date de la première exécution/représentation

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Titre de la collection

Clé HUMDRUM : GTL

Définition : Titre de la collection

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Œuvre associée (ex. Stéphane Mallarmé, L’Après-midi d’un faune)

Clé HUMDRUM : GAW

Définition : Œuvre associée (ex. Stéphane Mallarmé, L’Après-midi d’un faune)

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Désignation de la collection

Clé HUMDRUM : GCO

Définition : Désignation de la collection

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```
### Description de la source <SourceDesc>

Clé HUMDRUM :  OTL

Définition : Titre de la source.

Chapitre des Guidelines : 3.4.1.6 Source Description

Balise :`<title>`

Autre option : -

Recommandations : Cette manière minimale de renseigner le titre convient surtout aux titres officiels et consensuels des oeuvres - des titres qui ne font pas l'objet d'ambiguité. Pour le renseignement de titres alternatifs ou populaires, voir plus bas.

Exemple :


"<sourceDesc xml:id=""..."">
   <source xml:id=""..."">
      <bibl xml:id=""..."">
         <title xml:id=""..."">...</title>
      </bibl>
   </source>   
</sourceDesc>"

#### Éditeur de la source utilisée pour l'édition digitale

Clé HUMDRUM : PED

Définition : Éditeur de la source utilisée pour l'édition digitale

Chapitre des Guidelines : 
```
Balise : Si c'est une personne :
<sourceDesc>
   <source>
      <bibl>
         <editor>
           <persName auth="VIAF" auth.uri="https://viaf.org/viaf/12395760/">Paolo Fabri</persName>
         </editor>
      </bibl>
   </source>
```

Autre option : Si c'est une maison d'édition (cumulable) :

```
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
```

Recommandations : 

Exemple :
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

Clé HUMDRUM : PPR

Définition : Premier éditeur

Chapitre des Guidelines : 

Balise : <sourceDesc>
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

Autre option : Même logique s'il s'agit de la maison d'édition en utilisant <imprint>. Des dates peuvent également être ajoutées pour <editor> pour plus de précisions.

Recommandations : 

Exemple :
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

Clé HUMDRUM : PDT

Définition : Date de la première publication

Chapitre des Guidelines : 

Balise : <sourceDesc>
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

Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : PTL

Définition : Titre de publication

Chapitre des Guidelines : 

Balise : <sourceDesc>
   <source>
      <bibl>
         <title type="main"> Il nono libro de madrigali</title>
         <title type="subordinate">a cinque voci (1599)</title>  
      </bibl>
   </source>

Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : PPP

Définition : Lieu de publication

Chapitre des Guidelines : 

Balise : <sourceDesc>
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

Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : PC#

Définition : Numéro de catalogue de l'éditeur (ex. cotage)

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Numéro de catalogue scientifique (abr.) [ex. BWV 551]

Clé HUMDRUM : SCT

Définition : Numéro de catalogue scientifique (abr.) [ex. BWV 551]

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Numéro de catalogue scientifique (pas abr.) [ex. Koechel 117]

Clé HUMDRUM : SCA

Définition : Numéro de catalogue scientifique (pas abr.) [ex. Koechel 117]

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```

#### Numéro

Clé HUMDRUM : ONM

Définition : Numéro

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```
```
#### Volume

Clé HUMDRUM : OVM

Définition : Volume

Chapitre des Guidelines : 

Balise : <source>
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

Autre option : 

Recommandations : J'imagine que cela concerne essentiellement des données bibliographiques. J'emprunte cette manière à la TEI. La même est possible pour le numéro. 

Exemple :
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
#### Publication

Clé HUMDRUM : PUB

Définition : État de publication (ex. publié, pas encore publié, en cours de publication)

Chapitre des Guidelines : 

Balise : <sourceDesc>
   <source>
      <bibl>
         <unpub>En raison d'un manque de financement</unpub>
      </bibl>
   </source>

Autre option : 

Recommandations : En MEI, l'approche est à l'évidence très binaire : publié ou non. Nul besoin de le préciser si l'entité est bel et bien publiée (assez logique), mais par contre <unpub> est assez limité. Seul du texte est possible, expliquant les raisons de la non-publication. <unpub> peut d'ailleurs aussi aller dans <imprint> pour plus de précision sur le contexte de la non-publication (si celle-ci dépend de la maison d'édition).

Exemple :
```
<sourceDesc>
   <source>
      <bibl>
         <unpub>En raison d'un manque de financement</unpub>
      </bibl>
   </source>
```

#### Titre du manuscrit

Clé HUMDRUM : SMS

Définition : Titre du manuscrit

Chapitre des Guidelines : 

Balise : <source recordtype="d">
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

Autre option : <manifestation recordtype="d">
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

Recommandations : 

Exemple :
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

Clé HUMDRUM : SML

Définition : Lieu de conservation du manuscrit

Chapitre des Guidelines : 

Balise : <source recordtype="d">
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

Autre option : <manifestation recordtype="d">
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

Recommandations : 

Exemple :
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

Clé HUMDRUM : SMA

Définition : Info sur l'accès au manuscrit

Chapitre des Guidelines : 

Balise : <source recordtype="d">
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

Autre option : <manifestation recordtype="d">
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

Recommandations : 

Exemple :
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




#### Document d'origine de l'édition électronique

Clé HUMDRUM : YOR

Définition : Document d'origine de l'édition électronique

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : Donc une source ? <sourceDesc ?> 

Exemple :
```

```

#### Propriétaire du document d'origine

Clé HUMDRUM : YOO

Définition : Propriétaire du document d'origine

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Année du copyright originaire

Clé HUMDRUM : YOE

Définition : Année du copyright originaire

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Éditeur du document d'origine

Clé HUMDRUM : EED

Définition : Éditeur du document d'origine

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```

#### Désignation du genre musical

Clé HUMDRUM : AGN

Définition : Désignation du genre musical

Chapitre des Guidelines : 3.4.1.5 Notes Statement

Balise : <workList>
   <work>
      <classification xml :id="…">
         <termList xml:id="…">
            <term label="music genre" xml:id="…">...</term>
         </termList>
      </classification>

Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : AST

Définition : Désignation du style/période/typologie de l'œuvre

Chapitre des Guidelines : 

Balise : <workList>
   <work>
      <creation xml:id="…">
         <periodName>Contemporary music</periodName>
         <styleName>Minimalist</styleName>
      </creation>
   </work>
</workList>   

Autre option : 

Recommandations : 

Exemple :
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

Clé HUMDRUM : AMD

Définition : Classification du mode (Moyen âge et Renaissance)

Chapitre des Guidelines : 

Balise : <workList>
   <work>
      <key mode="dorian">
      <creation xml:id="…">
         <periodName>Contemporary music</periodName>
         <styleName>Minimalist</styleName>
      </creation>
   </work>
</workList>  

Autre option : 

Recommandations : En MEI, cela semble être une donnée à renseigner dans <key>, donc dans <work> ou <expression>, avec @mode. L'information peut également se retrouver dans la définition des portées. Il y a trois vocabulaires contrôlés MEI pour les modes. Voir data.mode.

Exemple :
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

Clé HUMDRUM : AMT

Définition : Classification métrique

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


#### Effectif

Clé HUMDRUM : AIN

Définition : Effectif

Chapitre des Guidelines : 

Balise : 

Autre option : 

Recommandations : 

Exemple :
```

```


### Dans la partie <music> (il faut dire que ce genre d'usage n'est pas recommandé) 

#### Numéro d'acte (<music?>)

Clé HUMDRUM : OAC

Définition : Numéro d'acte

Chapitre des Guidelines : 

Balise : 

Autre option : <body>
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

Recommandations : S'il est bien question d'une précision au sein de <music> : "The score and parts elements are placed here and not directly within the body element because score and part characteristics may change from mdiv to mdiv. For example, the 2nd movement of a symphony may require different performing forces (and therefore different score and part layout) than the other movements. The mdiv element may be recursively nested in order to represent music which exhibits this kind of structure. For example, an opera is normally divided into acts, which are in turn divided into scenes." https://music-encoding.org/guidelines/v5/elements/mdiv.html

Exemple :
```

```


#### Numéro de scène (<music?>)

Clé HUMDRUM : OSC

Définition : Numéro de scène

Chapitre des Guidelines : 

Balise : 

Autre option : <body>
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

Recommandations : 

Exemple :
```

```


#### Numéro de mouvement (<music?>)

Clé HUMDRUM : OMV

Définition : Numéro de mouvement

Chapitre des Guidelines : 

Balise : 

Autre option : <body>
   <mdiv label="Allegro" n="1">
      <score></score>
   </mdiv>
   <mdiv label="Menuet" n="2">
      <score></score>
   </mdiv>
</body>

Recommandations : Même commentaire que ci-dessous. Pour le numéro, nous pourrions ajouter dans les différents éléments @n.

Exemple :
```

```


#### Désignation du mouvement ou nom du mouvement

Clé HUMDRUM : OMD

Définition : Désignation du mouvement ou nom du mouvement

Chapitre des Guidelines : 

Balise : 

Autre option : <body>
   <mdiv label="Allegro">
      <score></score>
   </mdiv>
   <mdiv label="Menuet">
      <score></score>
   </mdiv>
</body> 

Recommandations : S'il s'agit d'un seul mouvement encodé au sein du fichier MEI, alors il me semble que le renseignement est similaire à celui renseigné pour "titre de l'oeuvre d'appartenance". Sil s'agit de plusieurs mouvements encodés au sein d'un même fichier MEI (peu recommandé), dans ce cas il faudrait indiquer cette information dans <music> à l'aide de <mdiv>. 

Exemple :
```

```

### 4. Quelques remarques 

En appui de ces éléments, il nous semble important de ne pas négliger quelques points importants pour favoriser l'interopérabilité des headers MEI. En particulier, le choix de thésaurus de référence est un enjeu important. Il nous semble désormais impensable de choisir un thésaurus n'étant défini selon l'ontologie SKOS, tant cette dernière favorise l'interopérabilité. Recourir aux identifiants du RISM pour les œuvres et leurs sources - ainsi qu'au DIAMM pour les manuscrits, ces derniers étant intégrés au RISM - est une bonne pratique pour l'encodage des œuvres musicales. 

_ThB présentation générale de LRM + un paragraphe sur la réflexion entre BDD sémantique centralisée vs l’information sémantisée dans les headers MEI
il nous est nécessaire de concevoir une batterie de types E55 pour typer les différents niveaux des sources d'après le modèle FRBR_

### 5. Pour conclure

Notre protocole se distingue par une interopérabilité maximale, couplée à une réelle exhaustivité. Bien que sa réalisation puisse être fastidieuse par le nombre important d'éléments à renseigner, le protocole porte une réelle valeur philologique et est ainsi parfaitement adapté à l'édition critique mais aussi au partage de fichiers au sein de la communauté internationale MEI.

En conclusion, il nous semble particulièrement important d'insister sur l'importance de _sourceDesc_ au sein du header MEI. Comme nous avons pu le démontrer à travers un nombre important d'exemples, il est le lieu le plus approprié pour l'expression de la source et les éventuelles opérations ayant permis la _recensio_.
