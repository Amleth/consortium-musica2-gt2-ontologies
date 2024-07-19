# Statut et fonction d'une personne fictive

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

Nous avons fait le choix d'exprimer la fonction d'une personne par l'usage de deux 'E74_group' ; le premier d'entre eux correspond à la structure qui accueille la personne et le second, inclus dans le premier, détaille la fonction occupée. Il est posssible de raffiner encore plus le processus par l'usage de 'E74_group' supplémentaires, jusqu'à arriver au niveau de précision attendu.

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
U[crm:E85_joining] --> |crm:P144_joined_with| M(crm:E74_group)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| S(crm:E74_group)
S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction<br>aat:300404157)
U[crm:E85_joining] -->|crm:P143_joined| K(crm:E28_propositionnal_object<br>«Mercure»)

R(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| K(crm:E89_propositionnal_object<br>«Mercure»)
R(crm:E13_attribute_assignement) --> |crm:P141_assigned| C(crm:E55_type<br>protagonist<br>aat:300410266)
R(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| V(crm:P2_has_type)
R(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| W(crm:E21_person<br>John Doe)

```
