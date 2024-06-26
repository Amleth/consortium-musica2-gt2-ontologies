# Indexation d'une thématique

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

Nous faisons usage du terme _Subject headings_, issu du Getty AAT. Celui-ci permet d'exprimer des thématiques complexes, puisqu'il "combine ensemble plusieurs concepts uniques en une seule séquence de mots". 

## d. Proposition Cidoc-CRM


```mermaid
graph TD;

A(crm:E28_conceptual_object) --> |crm:P2_has_type| B(crm:E55_type<br>Subject headings<br>300265269)
A(crm:E28_conceptual_object) --> |crm:P140_assigned_attribute_to| C(crm:E13)

```
