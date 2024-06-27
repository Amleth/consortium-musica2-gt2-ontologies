# Commanditaire d'une œuvre

## a. Besoins musicologiques

Nous avons besoin de modéliser la relation liant le commanditaire d'une œuvre au compositeur, ainsi que la pièce résultant de cette collaboration. Le commanditaire est souvent une personne morale (institution) plus qu'une personne physique ; nous nous attacherons néanmoins à expliciter ces deux possibilités distinctes. 

## b. Problématisation 

De quelle manière peut-on révéler l'aspect conséquentiel de l'œuvre suite à l'action de la commande ? Comment modéliser les différents types de commanditaires : institutionnels ou bien plus informels, commande d'une personne à une autre ?

## c. Contextualisation technique

Le thesaurus Getty AAT nous permet de typer l'action de commande, tandis que l'institution est inscrite dans un champ spatio-temporel. La date de commande de l'œuvre est ainsi, ainsi que sa date de finalisation. 

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E7_activity) --> |lrm:R16_created| B(crm:F1_work)
A(crm:E7_activity) --> |crm:P4_has_time_span| J(crm:E52_time_span<br>Date ISO 8601)

C(crm:F27_work_creation) -->|crm:P9_consists_of| A(crm:E7_activity)
C(crm:F27_work_creation) --> |crm:P2_has_type| D(crm:E55_type<br>Commande<br>aat:300400904)
C(crm:F27_work_creation) --> |crm:P14_carried_out_by| E(crm:E74_group)
C(crm:F27_work_creation) --> |crm:P4_has_time_span| K(crm:E52_time_span<br>Date ISO 8601)
E(crm:E74_group) -->|crm:P2_has_type| F(crm:E55_type<br>institution<br>aat:300026004)
E(crm:E74_group) --> |crm:P74_has_current_or_former_residence| I(crm:E53_place<br>Opéra de Paris)
I(crm:E53_place<br>Opéra de Paris) --> |crm:P168_is_defined_by| G(crm:E94_space_primitive
48.866667, 2.333333)
C(crm:F27_work_creation) --> |crm:P14_carried_out_by| H(crm:E21_person<John Doe)


```

