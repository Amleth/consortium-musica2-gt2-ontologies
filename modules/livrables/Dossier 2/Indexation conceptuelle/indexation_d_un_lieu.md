# Indexation d'un lieu

## a. Besoins musicologiques



## b. Problématisation 

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E28_conceptual_object<br>Œuvre) --> |crmdig:l35_has_commissioner| B(crm:E40_legal_body<br>Commanditaire)
B(crm:E40_legal_body<br>Commanditaire) --> |crm:p2_has_type| C[crm:E55_type<br>Orchestre]
B(crm:E40_legal_body<br>Commanditaire) --> |crm:P107_has_current_or_former_member| D[crm:E22_person<br>John Doe]

```

