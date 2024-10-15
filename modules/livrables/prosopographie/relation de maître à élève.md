# Relation de maître à élève

**_Faire une autre fiche cf situation pédago avec une classe_**

## a. Besoins musicologiques

Nous avons besoin de représenter la situation pédagogique d'apprentissage de deux points de vue ; autant de l'apprenant que de l'enseignant. Il peut également être nécessaire de situer cette situation dans un espace-temps donné, afin de la relier à des événements, ou bien à une institution si celle-ci s'est déroulée dans ce cadre précis. 

## b. Problématisation

De quelle manière peut-on exprimer une relation de maître à élève des deux points de vue, ainsi que son inscription dans différents contextes ?

## c. Contextualisation technique

Cet exemple fait usage d'un certain nombre de 'E7_activity' permettant de définir de manière précise les différentes étapes d'une situation pédagogique : l'apprentissage, l'enseignement, et la situation pédagogique en elle-même. Ces activités sont typées à l'aide du thésaurus Getty AAT afin de permettre une meilleure interopérabilité.

## d. Proposition CIDOC CRM

```mermaid
graph TD;

F[crm:E7_activity] --> |crm:P2_has_type| H[crm:E55_type<br>Situation pédagogique<br>aat:300266104]
F[crm:E7_activity] --> |crm:P9_consists_of| D[crm:E7_activity]
F[crm:E7_activity] --> |crm:P9_consists_of| A[crm:E7_activity]
A[crm:E7_activity] --> |crm:P2_has_type| C[crm:E55_type<br>Enseignement<br>aat:300069743]
A[crm:E7_Activity] --> |crm:P14_carried_out_by| B[crm:E21_person<br>John Doe]


D[crm:E7_Activity] --> |crm:P14_carried_out_by| E[crm:E21_person<br>Jane Doe]
D[crm:E7_activity] --> |crm:P2_has_type| G[crm:E55_type<br>Apprentissage<br>aat:300449145]

I(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| B[crm:E21_person<br>John Doe]
I(crm:E13_attribute_assignement) --> |crm:P141_assigned| A[crm:E7_Activity]
I(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| J(crm:P9_consists_of)

```



