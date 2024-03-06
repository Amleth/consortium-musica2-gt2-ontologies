# Commanditaire d'une œuvre

## a. Besoins musicologiques

Nous avons besoin de modéliser la relation liant le commanditaire d'une œuvre et le compositeur, ainsi que la modélisation de l'œuvre elle-même pour modéliser l'influence du commanditaire sur celle-ci. 

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E28_conceptual_object<br>Œuvre) --> |crmdig:l35_has_commissioner| B(crm:E40_legal_body<br>Commanditaire)
B(crm:E40_legal_body<br>Commanditaire) --> |crm:p2_has_type| C[crm:E55_type<br>Orchestre]
B(crm:E40_legal_body<br>Commanditaire) --> |crm:P107_has_current_or_former_member| D[crm:E22_person]

```
