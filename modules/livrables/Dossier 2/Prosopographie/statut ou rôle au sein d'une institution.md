# Statut ou rôle au sein d'une institution

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique 

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

L[crm:E85_joining] -->|crm:P143_joined| K(crm:E21_person<br>John Doe)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| K(crm:E21_person<br>John Doe)
L[crm:E85_joining] --> |crm:P144_joined_with| M(crm:E74_group)
U[crm:E85_joining] -->|crm:P143_joined| K(crm:E21_person<br>John Doe)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| S(crm:E74_group)
S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction)
U[crm:E85_joining] --> |crm:P144_joined_with| S(crm:E74_group)

M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
M(crm:E74_group) -->|crm:P74_has_current_or_former_residence| O(crm:E53_place<br>geonames)
P(crm:E66_formation)  -->|crm:P95_has_formed| M(crm:E74_group)
P(crm:E66_formation) -->|crm:P4_has_time_span| Q(crm:E52_time_span)
Q(crm:E52_time_span) -->|crm:P82a_begin_of_begin| R(Date_ISO_8601)
Q(crm:E52_time_span) -->|crm:P82b_end_of_the_end| R(Date_ISO_8601)



```

Aussi possible avec des E74 : sous-groupes 

