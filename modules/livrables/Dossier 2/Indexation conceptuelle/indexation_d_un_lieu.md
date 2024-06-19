# Indexation d'un lieu

## a. Besoins musicologiques

## b. Problématisation 

## c. Contextualisation technique

Quels sont les critères d'indexation nécessaires pour identifier un lieu ? 

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E53_place<br>Bibliothèque_Nationale_de_France) --> |crm:P168_is_defined_by| B(crm:E94_space_primitive<br>48.82978, 2.37708)
A(crm:E53_place<br>Bibliothèque_Nationale_de_France) --> |crm:P87_is_identified_by| C(crm:E44_place_appellation<br>Site François Mitterand)
D(crm:E45_adress<br>Quai François Mauriac 75706 Paris Cedex 13) --> C(crm:E44_place_appellation<br>Site François Mitterand)
C(crm:E44_place_appellation<br>Site François Mitterand) --> |crm:P140_assigned_attribute_to| E(crm:E13_attribute_assignement<br>geonames:8051139)

```

Faire un E74 connecté à un E53 avec un P74 et pas besoin de E13 / représenter le fait qu'une institution a plusieurs lieux
E44 et E45 n'existent plus
