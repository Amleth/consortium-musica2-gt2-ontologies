## Modélisation d'une institution

### a. Besoins musicologiques

De toutes époques, les institutions sont au cœur de la vie musicale. Elles peuvent tout autant accueillir des concerts que passer commande aux compositeurs, tout en insufflant des directives artistiques. Il est alors nécessaire de pouvoir les modéliser dans toute leur complexité, en indiquant leurs coordonnées géographiques - dépendent-elles d'un lieu bien spécifique ? -, la date de leur création ou bien l'arrivée d'une nouvelle direction, _etc_... 

### b. Problématisation

Comment représenter l'existence d'une institution, son domaine de rattachement mais aussi des données plus empiriques telles que le lieu où elle est établie, sa date de création,_etc_ ?

### c. Contextualisation technique

Le thésaurus Getty AAT permet de caractériser la typologie "institution" à l'aide d'un vocabulaire contrôlé, dont la définition est la suivante : "[nous traduisons] Organisations, associations ou établissements formellement structurés afin de promouvoir un objectif public ou privé spécifique, généralement un objectif religieux, caritatif ou éducatif." En partant de ce postulat, nous exprimons ensuite les caractéristiques principales de l'institution d'après les protocoles auparavant présentés : lieu où elle se trouve, date de création, _etc_.

### d. Proposition CIDOC CRM

```mermaid
graph TD;

A(crm:E74_group) -->|crm:P2_has_type| B(crm:E55_type<br>institution<br>aat:300026004)
A(crm:E74_group) -->|crm:P74_has_current_or_former_residence| C(crm:E53_place<br>Opéra Comique)
C(crm:E53_place<br>Opéra Comique) --> |crm:P1_is_identified_by| M(crm:E42_identifier)
C(crm:E53_place<br>Opéra Comique) --> |crm:P1_is_identified_by| P(crm:E42_identifier)
P(crm:E42_identifier) -->|crm:P168_place_is_defined_by| S(crm:E94_space_primitive<br>48.8912963,2.3917211)
P(crm:E42_identifier) --> |crm:P2_has_type| Q(crm:E55_type<br>coordonnées géographiques<br>aat:300387569)
M(crm:E42_identifier) --> |crm:P2_has_type| N(crm:E55_type<br>adresse<br>aat:300386983)
M(crm:E42_identifier) --> |crm:P190_has_sympbolic_value| O(1 Pl. Boieldieu, 75002 Paris<br>geonames:11983711)

G(crm:E66_formation)  -->|crm:P95_has_formed| A(crm:E74_group)
G(crm:E66_formation) -->|crm:P4_has_time_span| E(crm:E52_time_span)
E(crm:E52_time_span) -->|crm:P82a_begin_of_begin| F(Date_ISO_8601)
E(crm:E52_time_span) -->|crm:P82b_end_of_the_end| F(Date_ISO_8601)

```

