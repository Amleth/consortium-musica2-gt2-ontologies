# Indexation d'une source avec un mot-clé

## a. Besoins musicologiques

Les sources historiques musicologiques sont souvent identifiés à l'aide de critères spécialisés liés à des notions théoriques, esthétiques ou encore 

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E28_conceptual_object) --> |crm:P3_has_note| B(crm:E62_string<br>Symphonie)
B(crm:E62_string<br>Symphonie) --> |crm:P2_has_type| C(crm:E55_has_type<br>keyword<br>aat:300311841)

D(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| A(crm:E28_conceptual_object)
D(crm:E13_attribute_assignement) --> |crm:P141_assigned| B(crm:E62_string<br>Symphonie)
D(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| C(crm:E55_has_type<br>keyword<br>aat:300311841)
D(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| F(crm:E21_person<br>John Doe)

```
