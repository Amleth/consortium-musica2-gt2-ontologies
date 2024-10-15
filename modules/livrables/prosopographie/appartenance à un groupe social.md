## Appartenance à un groupe social

### a. Besoins musicologiques

L'appartenance à un groupe - qu'il soit publiquement identifié (par exemple une association, une société savante, etc...) - ou bien lié à l'association plus ou moins informelle de diverses personnalités (par exemple, le "Groupe des six") permet de reconstituer des liens inter-personnels dans l'optique d'un travail de recherche musicologique. Nous pouvons ainsi témoigner d'une certaine influence esthétique chez une personne liée à la fréquentation d'un cercle promeuvant une certaine idéologie, _etc_.

### b. Problématisation

De quelle manière peut-on matérialiser l'appartenance à un groupe afin de témoigner d'une rencontre au sein d'un même cercle ?

### c. Contextualisation technique

Nous utilisons un 'E74_group' lié à la personne concernée par un 'E85_joining'. Le 'E74_group' doit nécessairement être typé, ici à l'aide du thésaurus Getty AAT, afin de représenter la fonction / valeur du groupe. La date d'entrée au sein du groupe est également indiquée ; à noter que si celle-ci est incertaine, il convient d'utiliser un 'E13_attribute_assignement' pour préciser le raisonnement derrière l'attribution de cette date.

**P107 est plus pauvre qu'utiliser un E85 voir la notion de shortcut en CIDOC CRM** 

### d. Proposition CIDOC CRM

```mermaid
graph TD;

A(crm:E21_person<br>John_Doe) -->|crm:P143_joined| B(crm:E85_joining<br>Groupe)
B(crm:E85_joining) --> |P144_joined_with| G(crm:E74_group)
G(crm:E74_group) -->|crm:P2_has_type| C(crm:E55_type<br>Société Savante<br>aat:300026019)
G(crm:E74_group) --> |crm:P107_has_current_or_former_member| A(crm:E21_person<br>John_Doe)


B(crm:E85_joining) --> |crmP4:has_time_span| D(crm:E52_time_span)
D(crm:E52_time_span) --> |crmP82a:begin_of_the_begin| E(Date 1 ISO 8601)
D(crm:E52_time_span) --> |crmP81a:end_of_the_begin| I(Date 2 ISO 8601)
D(crm:E52_time_span) --> |crmP81b:begin_of_the_end| J(Date 3 ISO 8601)
D(crm:E52_time_span) --> |crmP82b:end_of_the_end| H(Date 4 ISO 8601)

```
