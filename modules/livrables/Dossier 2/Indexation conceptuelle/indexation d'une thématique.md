# Indexation d'une thématique

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

Nous faisons usage du terme _Subject headings_, issu du Getty AAT. Celui-ci permet d'exprimer des thématiques complexes, puisqu'il "combine ensemble plusieurs concepts uniques en une seule séquence de mots". 

## d. Proposition Cidoc-CRM


```mermaid
graph TD;

C(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| A(crm:E28_conceptual_object)
C(crm:E13_attribute_assignement) --> |crm:P141_assigned| E(crm:E64_inscription)
C(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| B(crm:E55_type<br>Subject headings<br>300265269)
C(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| D(crm:E21_person<br>John Doe)

```
