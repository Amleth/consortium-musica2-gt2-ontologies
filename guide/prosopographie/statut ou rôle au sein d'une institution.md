## Statut ou rôle au sein d'une institution

### a. Besoins musicologiques

Les rôles endossés par des personnes varient dans leurs appelations et significations au fil du temps. Il est donc important de pouvoir typer les responsabilités à l'aide d'un thésaurus, mais aussi de pouvoir exprimer un niveau de détail élevé vis-à-vis des informations à disposition, en faisant preuve de plus ou moins de précision.

### b. Problématisation

Comment exprime-t'on le statut et/ou la fonction d'une personne vis-à-vis de l'institution dont elle dépend ?

### c. Contextualisation technique

Nous présentons ici le protocole permettant de préciser le statut et/ou la fonction d'une personne au sein d'une institution. Nousavons fait le choix d'exprimer la fonction d'une personne par l'usage de deux 'E74_group' ; le premier d'entre eux correspond à la structure qui accueille la personne et le second, inclus dans le premier, détaille la fonction occupée. Il est posssible de raffiner encore plus le processus par l'usage de 'E74_group' supplémentaires, jusqu'à arriver au niveau de précision attendu. Les concepts adjacents aux 'E74_group' sont typés à l'aide du Getty AAT pour assurer une interopérabilité maximale.

```mermaid
graph TD;

P(crm:E66_formation) -->|crm:P4_has_time_span| Q(crm:E52_time_span)
P(crm:E66_formation) -->|crm:P95_has_formed| M(crm:E74_group)
Q(crm:E52_time_span) -->|crm:P82a_begin_of_begin| R(Date_ISO_8601)
Q(crm:E52_time_span) -->|crm:P82b_end_of_the_end| R(Date_ISO_8601)
M(crm:E74_group) -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)

M(crm:E74_group) -->|crm:P74_has_current_or_former_residence| O(crm:E53_place)
O(crm:E53_place) --> |crm:P1_is_identified_by| A(crm:E42_identifier)
A(crm:E42_identifier) --> |crm:P2_has_type| B(crm:E55_type<br>adresse<br>aat:300386983)
A(crm:E42_identifier) --> |crm:P190_has_sympbolic_value| C(Quai François Mauriac, 75706 Paris)
O(crm:E53_place) --> |crm:P1_is_identified_by| X(crm:E42_identifier)

X(crm:E42_identifier) --> |crm:P168_is_defined_by| Y(crm:E94_space_primitive<br>48.8339111,2.3750405,17)
X(crm:E42_identifier) --> |crm:P2_has_type| Z(crm:E55_type<br>coordonnées géographiques<br>aat:300387569)

M(crm:E74_group) ---> |crm:P107_has_current_or_former_member| S(crm:E74_group)
L[crm:E85_joining] --> |crm:P144_joined_with| M(crm:E74_group)
L[crm:E85_joining] --->|crm:P143_joined| K(crm:E21_person<br>John Doe)
U[crm:E85_joining] -->|crm:P143_joined| K(crm:E21_person<br>John Doe)

S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction)
M(crm:E74_group) --> |crm:P107_has_current_or_former_member| K(crm:E21_person<br>John Doe)
U[crm:E85_joining] ---> |crm:P144_joined_with| S(crm:E74_group)



```



