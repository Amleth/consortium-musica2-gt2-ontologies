# Modélisation d'une institution

## a. Besoins musicologiques

De toutes époques, les institutions sont au cœur de la vie musicale. Elles peuvent tout autant accueillir des concerts que passer commande aux compositeurs, tout en insufflant des directives artistiques. Il est alors nécessaire de pouvoir les modéliser dans toute leur complexité, en indiquant leurs coordonnées géographiques - dépendent-elles d'un lieu bien spécifique ? -, la date de leur création ou bien l'arrivée d'une nouvelle direction, etc... 

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E74_group) -->|crm:P2_has_type| B(crm:E55_type<br>institution<br>aat:300026004)
A(crm:E74_group) -->|crm:P55_has_current_location| C(crm:E53_place)
C(crm:E53_place) -->|crm:P140_assigned_attribute_to| D(crm:E13_attribute_assignement<br>geonames)
A(crm:E74_group) -->|crm:P4_has_time_span| E(crm:E52_time_span)
E(crm:E52_time_span) -->|crm:P2_has_type| G(crm:E55_type<br>création)
E(crm:E52_time_span) -->|crm:P82a_begin_of_begin| F(Date_ISO_8601)
E(crm:E52_time_span) -->|crm:P82b_end_of_the_end| F(Date_ISO_8601)

```

