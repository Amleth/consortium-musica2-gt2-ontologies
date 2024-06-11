# Modélisation d'une institution

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E1_entity) -->|crm:P2_has_type| B(crm:E55_type<br>institution<br>aat:300026004)
A(crm:E1_entity) -->|crm:P55_has_current_location| C(crm:E53_place)
C(crm:E53_place) --> |crm:P140_assigned_attribute_to| D(crm:E13_attribute_assignement<br>geonames)

```

