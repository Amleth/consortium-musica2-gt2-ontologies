# Indexation d'une source avec un mot-clé

## a. Besoins musicologiques

Les sources historiques musicologiques sont souvent identifiés à l'aide de critères spécialisés liés à des notions théoriques ou esthétiques, en plus des informations de temps et d'espace. Des mots-clés sont alors définis par la personne en charge de l'indexation et appliqués à différentes sources afin de les typer. Il est donc nécessaire de pouvoir modéliser l'indexation d'une source à l'aide d'un mot clé issu d'un thésaurus.

## b. Problématisation

De quelle manière peut-on indexer une source à l'aide d'un mot-clé ?

## c. Contextualisation technique

Nous utilisons ici le 'E13_attribute_assignement' afin d'attribuer un mot clé à une source. Le concept de "mot-clé" porté par un 'E62_string' est lui-même typé à l'aide du Getty AAT, tandis que les mots-clés eux-mêmes sont également piochés au sein de ce thésaurus.

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E73_information_object) --> |crm:P3_has_note| B(crm:E62_string<br>Symphonie)
B(crm:E62_string<br>Symphonie) --> |crm:P2_has_type| C(crm:E55_type<br>keyword<br>aat:300311841)

D(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| A(crm:E73_information_object)
D(crm:E13_attribute_assignement) --> |crm:P141_assigned| B(crm:E62_string<br>Symphonie)
D(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| C(crm:E55_type<br>keyword<br>aat:300311841)
D(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| F(crm:E21_person<br>John Doe)

```
