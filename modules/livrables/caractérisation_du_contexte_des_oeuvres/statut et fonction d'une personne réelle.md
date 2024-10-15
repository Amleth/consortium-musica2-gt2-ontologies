# Statut et fonction d'une personne réelle

## a. Besoins musicologiques

Les rôles endossés par des personnes varient dans leurs appellations et significations au fil du temps. Il est donc important de pouvoir typer les responsabilités à l'aide d'un thésaurus, mais aussi de pouvoir exprimer un niveau de détail élevé vis-à-vis des informations à disposition, en faisant preuve de plus ou moins de précision.

## b. Problématisation

Comment exprime-t'on le statut et/ou la fonction d'une personne vis-à-vis de l'institution dont elle dépend ?

## c. Contextualisation technique

Nous présentons ici le protocole permettant de préciser le statut et/ou la fonction d'une personne au sein d'une institution. Nous avons fait le choix d'exprimer la fonction d'une personne par l'usage de deux 'E74_group' ; le premier d'entre eux correspond à la structure qui accueille la personne et le second, inclus dans le premier, détaille la fonction occupée. Il est possible de raffiner encore plus le processus par l'usage de 'E74_group' supplémentaires, jusqu'à arriver au niveau de précision attendu. Les concepts adjacents aux 'E74_group' sont typés à l'aide du Getty AAT pour assurer une interopérabilité maximale.

## d. Proposition CIDOC CRM

```mermaid
graph TD;

M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| S(crm:E74_group)
S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction)
U[crm:E85_joining] -->|crm:P143_joined| A(crm:E21_person<br>John Doe)
U[crm:E85_joining] --> |crm:P144_joined_with| M(crm:E74_group)

```

