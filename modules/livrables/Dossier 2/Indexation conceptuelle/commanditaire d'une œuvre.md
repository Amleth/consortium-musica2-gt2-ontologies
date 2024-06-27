# Commanditaire d'une œuvre

## a. Besoins musicologiques

Nous avons besoin de modéliser la relation liant le commanditaire d'une œuvre au compositeur, ainsi que la pièce résultant de cette collaboration. Le commanditaire est souvent une personne morale (institution) plus qu'une personne physique.

## b. Problématisation 

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:F27_work_creation) --> |lrm:R16_created| B(crm:F1_work)
C(crm:F27_work_creation) -->|crm:P9_consists_of| A(crm:F27_work_creation)
C(crm:F27_work_creation) --> |crm:P2_has_type| D(crm:E55_type<br>Commande<br>aat:300400904)
C(crm:F27_work_creation) --> |crm:P14_carried_out_by| E(crm:E74_group)
E(crm:E74_group) -->|crm:P2_has_type| F(crm:E55_type<br>institution<br>aat:300026004)
E(crm:E74_group) -->|crm:P74_has_current_or_former_residence| G(crm:E53_place<br>geonames)
C(crm:F27_work_creation) --> |crm:P14_carried_out_by| H(crm:E21_person<John Doe)


```

