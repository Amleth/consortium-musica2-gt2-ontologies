# Indexation d'un lieu

## a. Besoins musicologiques

Lors du processus d'indexation conceptuelle, il est nécessaire de distinguer les lieux à l'aide de divers critères remarquables, tout en prenant soin - si besoin est - de relier chaque lieu à l'institution qu'il incarne. Il est également important de fournir des coordonnées GPS afin de pouvoir saisir la position géographique réelle du lieu. 

## b. Problématisation 

Comment modéliser un lieu tout en faisant apparaître l'institution à laquelle il se rattache, mais aussi son adresse, voire ses différentes adresses ?

## c. Contextualisation technique

Afin d'exprimer les coordonnées géographiques en Cidoc-CRM, l'usage de l'entité E94_space_primitive est conseillé, directement complété par l'indication des données GPS. Le thésaurus Getty AAT est utilisé pour identifier le concept d'institution.

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E53_place<br>Bibliothèque_Nationale_de_France) --> |crm:P168_is_defined_by| B(crm:E94_space_primitive<br>48.8339111, 2.3750405)
C(crm:E74_group<br>Institution<br>aat:300026004) --> |crm:P74_has_current_or_former_residence| A(crm:E53_place<br>Bibliothèque_Nationale_de_France)
D(crm:P190_has_symbolic_content<br>Quai François Mauriac, 75706, Paris) --> |crm:P2_has_type| E(crm:E55_type<br>adresse<br>aat:300386983)

H(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| A(crm:E53_place<br>Bibliothèque_Nationale_de_France) 
H(crm:E13_attribute_assignement) --> |crm:P141_assigned| D(crm:P190_has_symbolic_content<br>Quai François Mauriac, 75706, Paris)
H(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| K(crm:E55_type<br>adresse<br>aat:300386983)
H(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| J(crm:E21_person<br>John Doe) J(crm:P74_has_current_or_former_residence)

```
