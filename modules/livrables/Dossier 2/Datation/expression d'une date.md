# Expression d'une date

## a. Besoins musicologiques

Le chercheur en sciences humaines doit pouvoir exprimer une date afin de transmettre avec justesse l'information scientifique, tout en étant conscient de la nécessité informatique d'une date précise exprimée dans un format référence. 

Les implications de la définition du temps ont été clairement soulignés par la mise en exergue de divers cas particuliers complexes, voire douteux. Dans le cas de _L’Heure espagnole_ de Ravel, la partition chant et piano a été publiée en 1908 mais l'orchestration réalisée en 1910. La première interprétation publique de l’opéra a eu lieu en 1911, la même année que la publication de la partition pour orchestre. Ce cas souligne donc la possibilité de multiplier les champs "date" correspondant aux diverses versions de l'œuvre.  

## b. Problématisation

Comment exprimer une date, dans un référentiel normé et informatiquement précis ? On constate par exemple que le terme _circa_ est régulièrement employé, malgré son manque de précision. Nous devons également présenter une date calculable par la machine (c'est-à-dire exprimable en ISO 8601)afin de l'intégrer dans une représentation chronologique calculée des données. 

## c. Contextualisation technique

La meilleure manière d'exprimer une date est de la définir par le biais de deux intervalles, l'un exprimant l'incertitude sur son début, l'autre sur sa fin. Chacun est constitué de deux dates exprimées en ISO 8601 et peuvent être définis de quatre manières principales : 
 - Strictement contenu dans la période de recherche
 - Couvre la période de recherche
 - Commence avant la période de recherche et se termine en son sein
 - Commence pendant la période de recherche et se termine après

Dans le cas d'une date n'apparaîssant pas dans la source, les intervalles saisis par les chercheurs sont des reconstructions qui doivent être argumentées par un champ permettant d'exprimer un degré de certitude. Un vocabulaire contrôlé proposant des paliers d'expression de la certitude doit être proposé, et partagé au sein du Consortium Musica2.

Le système doit enregistrer chaque date soumise par les chercheurs comme des valeurs signées et datées, en ne considérant pas la valeur d'un champ date comme une donnée monolithique, mais comme un succession de contributions contextualisées, un peu à la manière d'un cahier de laboratoire.

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E2_temporal_entity) --> |crm:p4_has_time_span| B(crm:E52_time_span)
B(crm:E52_time_span) --> |crm:p82a_begin_of_the_begin| C("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p81a_end_of_the_begin| D("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p81b_begin_of_the_end| E("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p82b_end_of_the_end| F("Date ISO 8601")
```
