# Appartenance à un groupe social

## a. Besoins musicologiques

L'appartenance à un groupe - qu'il soit publiquement identifié (société savante) - ou bien lié à l'association de diverses personnalités (par exemple, le "Groupe des six". 

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E21_person<br>John_Doe) -->|crm:P143_joined| B(crm:E85_joining<br>Groupe)
B(crm:E85_joining) --> |P144_joined_with| G(crm:E74_group)
G(crm:E74_group) -->|crm:P2_has_type| C(crm:E55_type<br>Société Savante)
G(crm:E74_group) --> |crm:P107_has_current_or_former_member| A(crm:E21_person<br>John_Doe)


B(crm:E85_joining) --> |crmP4:has_time_span| D(crm:E52_time_span)
D(crm:E52_time_span) --> |crmP82a:begin_of_the_begin| E(Date ISO 8601)
D(crm:E52_time_span) --> |crmP82b:end_of_the_end| E(Date ISO 8601)
D(crm:E52_time_span) --->|crm:P2_has_type| F(crm:E55_type<br>Date d'entrée)

```
