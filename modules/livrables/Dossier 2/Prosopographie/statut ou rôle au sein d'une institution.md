# Statut ou rôle au sein d'une institution

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique 

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

H(crm:E7_activity) --> |crm:P2_has_type| I(crm:E55_type<br>Direction)
H(crm:E7_activity) --> |crm:P14_carried_out_by| K(crm:E21_person<br>John Doe)

L[crm:E85_joining] -->|crm:P143_joined| K(crm:E21_person<br>John Doe)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| K(crm:E21_person<br>John Doe)
L[crm:E85_joining] --> |P144_joined_with| M(crm:E74_group)

M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
M(crm:E74_group) -->|crm:P55_has_current_location| O(crm:E53_place)
O(crm:E53_place) -->|crm:P140_assigned_attribute_to| P(crm:E13_attribute_assignement<br>geonames)
M(crm:E74_group) -->|crm:P4_has_time_span| R(crm:E52_time_span)
R(crm:E52_time_span) -->|crm:P2_has_type| T(crm:E55_type<br>création)
R(crm:E52_time_span) -->|crm:P82a_begin_of_begin| S(Date_ISO_8601)
R(crm:E52_time_span) -->|crm:P82b_end_of_the_end| S(Date_ISO_8601)

```

