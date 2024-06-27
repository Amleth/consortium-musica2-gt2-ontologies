# Indexation d'une personne

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E21_person) --> |crm:P98_brought_into_life| B(crm:E67_birth)
B(crm:E67_birth) --> |crm:P4_has_time_span| C(crm:E52_time_span<br>Date ISO 8601)

A(crm:E21_person) --> |crm:P100_was_death_of| D(crm:E69_death)
D(crm:E69_death) --> |crm:P4_has_time_span| E(crm:E52_time_span<br>Date ISO 8601)

M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| S(crm:E74_group)
S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction)
U[crm:E85_joining] -->|crm:P143_joined| A(crm:E21_person<br>John Doe)
U[crm:E85_joining] --> |crm:P144_joined_with| M(crm:E74_group)

```
