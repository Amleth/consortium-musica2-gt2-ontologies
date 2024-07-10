# Description d'une personne

## a. Besoins musicologiques

**_éléments pour la description d'une personne_**

Afin d'indexer une personne, nous avons dans un premier temps besoin d'informations biographiques basiques liées aux dates de naissance et de mort de l'individu. Nous pourrons, le cas échéant, exprimer de manière idoine aux exemples présents au sein du module _datation_ diverses incertitudes où des inscriptions dans des référentiels calendaires plus rares. La fonction et/ou le statut occupé par la personne sont également des éléments nous permettant d'indexer. 

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E21_person<br>John Doe) --> |crm:P98_brought_into_life| B(crm:E67_birth)
B(crm:E67_birth) --> |crm:P4_has_time_span| C(crm:E52_time_span<br>Date ISO 8601)

U[crm:E85_joining] --> |crm:P144_joined_with| S(crm:E74_group)

M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| S(crm:E74_group)

U[crm:E85_joining] -->|crm:P143_joined| A(crm:E21_person<br>John Doe)

A(crm:E21_person) --> |crm:P100_was_death_of| D(crm:E69_death)
S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction)
D(crm:E69_death) --> |crm:P4_has_time_span| E(crm:E52_time_span<br>Date ISO 8601)

```


```mermaid
graph TD;

A(crm:E21_person<br>John Doe) --> |crm:P98_brought_into_life| B(crm:E67_birth)
B(crm:E67_birth) --> |crm:P4_has_time_span| C(crm:E52_time_span<br>Date ISO 8601)

U[crm:E85_joining] --> |crm:P144_joined_with| S(crm:E74_group)

M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| S(crm:E74_group)

U[crm:E85_joining] -->|crm:P143_joined| A(crm:E21_person<br>John Doe)

A(crm:E21_person) --> |crm:P100_was_death_of| D(crm:E69_death)
S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction)
D(crm:E69_death) --> |crm:P4_has_time_span| E(crm:E52_time_span<br>Date ISO 8601)

T(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| A(crm:E21_person<br>John Doe)
T(crm:E13_attribute_assignement) --> |crm:P141_assigned| C(crm:E52_time_span<br>Date ISO 8601)
T(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| U(crm:P4_has_time_span)

```
