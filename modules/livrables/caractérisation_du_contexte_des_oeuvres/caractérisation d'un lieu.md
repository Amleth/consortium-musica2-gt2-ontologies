## Caractérisation d'un lieu 

### a. Besoins musicologiques

Lors du processus d'indexation conceptuelle, il est nécessaire de distinguer les lieux à l'aide de divers critères remarquables, tout en prenant soin - si besoin est - de relier chaque lieu à l'institution qu'il incarne. Il est également important de fournir des coordonnées GPS afin de pouvoir saisir la position géographique réelle du lieu, par exemple si l'institution a eu plusieurs sièges au fur et à mesure des années.

### b. Problématisation 

Comment modéliser un lieu tout en faisant apparaître l'institution à laquelle il se rattache, mais aussi son adresse ?

### c. Contextualisation technique

Cet exemple nous permet de présenter notre protocole complet d'identification des lieux, offrant une interopérabilité et une précision maximales. Nous faisons le choix de désigner le lieu tant par ses coordonnées géographiques que par son adresse :

Deux 'E42_identifier' sont reliés au 'E53_place'. Le premier d'entre eux signale ses coordonnées GPS ('E94_space_primitive')et le second son adresse, complétée par un identifiant geonames. Les deux concepts exprimés 'E42_identifier' sont typés par des entrées du thésaurus Getty AAT afin d'assurer une compréhension égale pour tous les usagers du protocole tout en assurant son interopérabilité. L'institution est également typé de manière similaire.

Les deux axes choisis se complètent et permettent de typer tout autant des lieux anciens, n'existant plus désormais ou bien ayant changé de localisation, qu'un site précis au sein d'un lieu en comportant plusieurs, comme c'est le cas pour la Bibliothèque Nationale de France.

### d. Proposition CIDOC CRM

```mermaid
graph TD;

A(crm:E53_place<br>Site Tolbiac) --> |crm:P1_is_identified_by| B(crm:E42_identifier)
A(crm:E53_place<br>Site Tolbiac) --> |crm:P1_is_identified_by| S(crm:E42_identifier)
S(crm:E42_identifier) --> |crm:P168_is_defined_by| Z(crm:E94_space_primitive<br>48.8493676,2.3366315,14)
S(crm:E42_identifier) --> |crm:P2_has_type| N(crm:E55_type<br>coordonnées géographiques<br>aat:300387569)

B(crm:E42_identifier) --> |crm:P2_has_type| X(crm:E55_type<br>adresse<br>aat:300386983)
B(crm:E42_identifier) --> |crm:P190_has_sympbolic_value| Y(«Quai François Mauriac, 75706 Paris»)


C(crm:E74_group<br>«Bibliothèque Nationale de France») --> |crm:P74_has_current_or_former_residence| A(crm:E53_place<br>Site Tolbiac)
C(crm:E74_group<br>«Bibliothèque Nationale de France») --> |crm:P2_has_type| H(crm:E55_type<br>Institution<br>aat:300026004)

```
