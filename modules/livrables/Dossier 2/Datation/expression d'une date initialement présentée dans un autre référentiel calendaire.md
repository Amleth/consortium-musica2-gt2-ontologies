# Expression d'une date initialement présentée dans un autre référentiel calendaire

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM 

```mermaid
graph TD;

A(crm:E2_temporal_entity) --> |crm:p128_is_carried_by| G[crm:E73_information_object<br>dating_system<br>aat:300404573]
G[crm:E73_information_object<br>dating_system<br>aat:300404573] --> |crm:p2_has_type| H[crm:E55_Type<br>style_vénitien]
A(crm:E2_temporal_entity) --> |crm:p4_has_time_span| B(crm:E52_time_span)
B(crm:E52_time_span) --> |crm:p82a_begin_of_the_begin| C("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p81a_end_of_the_begin| D("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p81b_begin_of_the_end| E("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p82b_end_of_the_end| F("Date ISO 8601")
```
