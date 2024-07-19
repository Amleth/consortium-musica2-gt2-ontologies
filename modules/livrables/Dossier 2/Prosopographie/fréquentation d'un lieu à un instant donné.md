# Fréquentation d'un lieu à un instant donné

## a. Besoins musicologiques

Les chercheurs ont besoin de témoigner de manière normée de la présence d'une ou plusieurs personnes au sein d'un espace-temps normé, avec une date précise exprimée dans un format référence.

## b. Problématisation

Comment peut-on exprimer la présence d'une personne physique dans un lieu donné, au sein d'une période de temps définie par le chercheur ? Nous ne nous posons pas encore la question des outils de modélisation pour la définition de la personne dans le cadre de cet exemple, mais son rôle et son statut peuvent être précisés.

## c. Contextualisation technique

L'utilisation de deux intervalles est primordiale pour exprimer une incertitude sur la temporalité de la présence dans un lieu donné. Celle-ci peut être enrichie d'une annotation, tout comme des commentaires liés à l'attribution de l'endroit fréquenté.

## d. Proposition Cidoc-CRM

```mermaid
graph TD;



B(E7_activity) -->|crm:P7_took_place_at| I(E53_place<br>Cathédrale Notre Dame de Paris)
I(E53_place<br>Cathédrale Notre Dame de Paris) --> |crm:P1_is_identified_by| M(crm:E42_identifier)
M(crm:E42_identifier) --> |crm:P2_has_type| K(crm:E55_type<br>adresse<br>aat:300386983)
M(crm:E42_identifier) --> |crm:P190_has_symbolic_content| N(6 Parvis Notre-Dame - Place Jean-Paul II, 75004 Paris<br>geonames:6269274)
I(E53_place<br>Cathédrale Notre Dame de Paris) --> |crm:P1_is_identified_by| X(crm:E42_identifier)
X(crm:E42_identifier) --> |crm:P168_is_defined_by| L(crm:E94_space_primitive<br>48.8471097, 2.3590381)
X(crm:E42_identifier) --> |crm:P2_has_type| Y(crm:E55_type<br>coordonnées géographiques<br>aat:300387569)

B(E7_activity) --> |crm:P4_has_time_span| D(crm:E52_time_span<br>Date ISO 8601)
B(E7_activity) -->|crm:P2_has_type| C(E55_type<br>Fréquentation)

U(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| A(crm:E21_Person<br>John Doe)
U(crm:E13_attribute_assignement) --> |crm:P141_assigned| D(crm:E52_time_span)
U(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| S(crm:P164_is_temporally_specified_by)
U(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| V(crm:E21_Person<br>Jane Doe)

R(crm:E93_presence) --> |crm:P195_was_a_presence_of| A(crm:E21_Person<br>John Doe)
R(crm:E93_presence) --> |crm:P167_was_within| I(E53_place<br>Cathédrale Notre Dame de Paris)

```


