# Indexation d'une thématique

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

Nous faisons usage du terme _Subject headings_, issu du Getty AAT. Celui-ci permet d'exprimer des thématiques complexes, puisqu'il "combine ensemble plusieurs concepts uniques en une seule séquence de mots". 

## d. Proposition Cidoc-CRM


```mermaid
graph TD;

A(crm:E28_conceptual_object) --> |crm:P3_has_note| B(crm:E62_string<br>Symphonie)
B(crm:E62_string<br>Symphonie) --> |crm:P2_has_type| C(crm:E55_type<br>Subject headings<br>300265269)

D(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| A(crm:E28_conceptual_object)
D(crm:E13_attribute_assignement) --> |crm:P141_assigned| B(crm:E62_string<br>Symphonie)
D(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| C(crm:E55_type<br>Subject headings<br>300265269)
D(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| F(crm:E21_person<br>John Doe)

```
