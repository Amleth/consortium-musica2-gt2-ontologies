## Fréquentation d'une institution

### a. Besoins musicologiques

Il est souvent nécessaire de témoigner de la présence d'une personne au sein d'une institution, en détaillant s'il s'agit d'un simple passage ou bien d'une inscription réelle au sein de celle-ci. Nous avons donc besoin d'informations spatio-temporelles, mais aussi de typer les statuts et/ou fonctions des personnes concernées, tout en se référant à des ressources existantes telles que des thésaurus.

### b. Problématisation

Comment modéliser la présence d'une personne au sein d'une institution ? Quels sont les outils nous permettant de typer la nature de la fréquentation ?

### c. Contextualisation technique

Nous croisons ici l'usage de trois de nos protocoles ; sur les dates, les lieux et les statuts et fonctions. La mise en relation de ces derniers avec un 'E21_Person' permet de tisser des liens complémentaires entre l'individu et l'institution.

### d. Proposition CIDOC CRM

```mermaid
graph TD;

P(crm:E85_joining) --> |crm:P144_joined_with| Q(crm:E74:group)
P(crm:E85_joining) --> |crm:P143_joined| A("crm:E21_Person<br>John Doe")
Q(crm:E74:group) --> |crm:P107_has_current_or_former_member| X(crm:E74:group)
X(crm:E74:group) --> |crm:P2_has_type| Y(crm:E55_type<br>Direction<br>aat:300404157)
Q(crm:E74:group) -->|crm:P2_has_type| R(crm:E55_type<br>institution<br>aat:300026004)

B(E7_activity) -->|crm:P14_carried_out_by| A("crm:E21_Person<br>John Doe")
B(E7_activity) -->|crm:P2_has_type| C(E55_type<br>Fréquentation)

B(E7_activity) --->|crm:P7_took_place_at| K(E53_place<br>Philharmonie de Paris)
I(crm:E74_group) -->|crm:P2_has_type| J(crm:E55_type<br>institution<br>aat:300026004)
I(crm:E74_group) -->|crm:P55_has_current_location| K(crm:E53_place)
K(crm:E53_place<br>Philharmonie de Paris) --> |crm:P1_is_identified_by| S(crm:E42_identifier)

S(crm:E42_identifier) --> |crm:P2_has_type| T(crm:E55_type<br>adresse<br>aat:300386983)
S(crm:E42_identifier) --> |crm:P190_has_sympbolic_value| U(221 Av. Jean Jaurès, 75019 Paris)
K(crm:E53_place<br>Philharmonie de Paris) --> |crm:P1_is_identified_by| V(crm:E42_identifier)
V(crm:E42_identifier) --> |crm:P168_is_defined_by| Z(crm:E94_space_primitive<br>48.8912963,2.3917211)
V(crm:E42_identifier) --> |crm:P2_has_type| W(crm:E55_type<br>coordonnées géographiques<br>aat:300387569)


I(crm:E74_group) -->|crm:P4_has_time_span| M(crm:E52_time_span)
M(crm:E52_time_span) -->|crm:P2_has_type| N(crm:E55_type<br>création)
M(crm:E52_time_span) -->|crm:P82a_begin_of_begin| O(Date_ISO_8601)
M(crm:E52_time_span) -->|crm:P82b_end_of_the_end| O(Date_ISO_8601)

B(E7_activity) --> |crm:P4_has_time_span| D(crm:E52_time_span)
D(crm:E52_time_span) --> |crm:P82a_begin_of_the_begin| E("Date ISO 8601")
D(crm:E52_time_span) --> |crm:P81a_end_of_the_begin| F("Date ISO 8601")
D(crm:E52_time_span) --> |crm:P81b_begin_of_the_end|G("Date ISO 8601")
D(crm:E52_time_span) --> |crm:P82b_end_of_the_end| H("Date ISO 8601")

```

