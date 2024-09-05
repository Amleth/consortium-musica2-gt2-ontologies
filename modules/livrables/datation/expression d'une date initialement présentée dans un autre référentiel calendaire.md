# Expression d'une date initialement présentée dans un autre référentiel calendaire

## a. Besoins musicologiques

Les chercheurs spécialisés en musicologie historique naviguent entre un grand nombre de référentiels calendaires. Il convient de proposer une convention de notation offrant une compréhension immédiate à travers la modélisation de dates en Cidoc-CRM, tout en permettant aux chercheurs de témoigner d'incertitudes mais aussi d'éclairer la méthodologie derrière la conversion des dates et justifier leur choix.

## b. Problématisation

De quelle manière exprimer de manière compréhensible une date originellement exprimée dans un référentiel calendaire ancien, ou peu commun ?

## c. Contextualisation technique

Les ateliers menés auprès de musicologues nous ont permis d'orienter les résultats vers une nécessaire uniformisation des dates au format ISO 8601. Le chercheur peut, s'il le souhaite, faire part d'un commentaire précis par l'usage d'un 'E13_Attribute_Assignement' ; dans cet exemple, le commentaire signale une attention particulière à accorder à la date de fin la plus tardive, signée de la main de son auteur par l'emploi d'un 'E21_person'.

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

I(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| A(crm:E2_temporal_entity)
I(crm:E13_attribute_assignement) --> |crm:P141_assigned| F("Date ISO 8601")
I(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| K(crm:P82b_end_of_the_end)
I(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| L(crm:E21_person<br>John Doe)

```
