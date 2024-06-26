# Statut et fonction d'une personne réelle

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
U[crm:E85_joining] --> |crm:P144_joined_with| M(crm:E74_group)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| S(crm:E74_group)
S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction)
U[crm:E85_joining] -->|crm:P143_joined| K(crm:E28_conceptual_object<br>John Doe)
U[crm:E85_joining] -->|crm:P143_joined| A(crm:E21_person<br>John Doe)
U[crm:E85_joining] --> |crm:P144_joined_with| M(crm:E74_group)

K(crm:E28_conceptual_object<br>John Doe) --> |crm:P2_has_type| C(crm:E55_type<br>protagonist<br>aat:300410266)
A(crm:E21_person<br>John Doe) --> |crm:P2_has_type| C(crm:E55_type<br>protagonist<br>aat:300410266)

```

