# Indexation d'un lieu

## a. Besoins musicologiques

Lors du processus d'indexation conceptuelle, il est nécessaire de distinguer les lieux à l'aide de divers critères remarquables, tout en prenant soin - si besoin est - de relier chaque lieu à l'institution qu'il incarne. Il est également important de fournir des coordonnées GPS afin de pouvoir saisir la position géographique réelle du lieu. 

## b. Problématisation 

## c. Contextualisation technique

Quels sont les critères d'indexation nécessaires pour identifier un lieu ? 

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E53_place<br>Bibliothèque_Nationale_de_France) --> |crm:P168_is_defined_by| B(crm:E94_space_primitive<br>48.82978, 2.37708)
C(crm:E74_group<br>Institution<br>aat:300026004) --> |crm:P74_has_current_or_former_residence| A(crm:E53_place<br>Bibliothèque_Nationale_de_France)
A(crm:E53_place<br>Bibliothèque_Nationale_de_France) --> |crm:P1_is_identified_by| D(crm:P190_has_symbolic_content<br>Quai François Mauriac, 75706 Paris)
D(crm:P190_has_symbolic_content<br>Quai François Mauriac, 75706 Paris) --> |crm:P2_has_type| E(crm:E55_type<br>adresse)

```
