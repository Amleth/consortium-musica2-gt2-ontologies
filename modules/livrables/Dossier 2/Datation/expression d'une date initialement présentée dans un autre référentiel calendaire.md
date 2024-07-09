# Expression d'une date initialement présentée dans un autre référentiel calendaire

## a. Besoins musicologiques

Les chercheurs spécialisés en musicologie historique naviguent entre un grand nombre de référentiels calendaires. Il convient de proposer une convention qui permette leur compréhension immédiate à travers leur modélisation en Cidoc-CRM, tout en permettant aux chercheurs de témoigner d'incertitudes mais aussi d'éclairer la méthodologie derrière la conversion des dates.

## b. Problématisation

De quelle manière exprimer de manière compréhensible une date originellement exprimée dans un référentiel calendaire ancien, ou peu commun ?

## c. Contextualisation technique

Les ateliers menés auprès de musicologues nous ont permis d'orienter les résultats vers une nécessaire uniformisation des dates au format ISO 8601. Le chercheur est responsable de la transposition d'un référentiel à l'autre, et peut, s'il le souhaite, faire part d'une incertitude par l'usage d'un E13 Attribute Assignement.

## d. Proposition CIDOC CRM 

```mermaid
graph TD;

A(crm:E2_temporal_entity) --> |crm:P128_is_carried_by| G[crm:E73_information_object<br>dating_system<br>aat:300404573]
G[crm:E73_information_object<br>dating_system<br>aat:300404573] --> |crm:P2_has_type| H[crm:E55_Type<br>style_vénitien]
A(crm:E2_temporal_entity) --> |crm:P4_has_time_span| B(crm:E52_time_span)
B(crm:E52_time_span) --> |crm:P82a_begin_of_the_begin| C("Date ISO 8601")
B(crm:E52_time_span) --> |crm:P81a_end_of_the_begin| D("Date ISO 8601")
B(crm:E52_time_span) --> |crm:P81b_begin_of_the_end| E("Date ISO 8601")
B(crm:E52_time_span) --> |crm:P82b_end_of_the_end| F("Date ISO 8601")
B(crm:E52_time_span) --> |crm:P140_assigned_attribute_to| I(crm:E13_attribute_assignement)
```
