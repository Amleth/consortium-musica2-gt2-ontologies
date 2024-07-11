# Fréquentation d'une institution

## a. Besoins musicologiques

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

P(crm:E7_activity) --> |crm:socP11_has_role| Q(crm:socE15_role)
Q(crm:socE15_role) -->|crm:P2_has_type| R(crm:E55_type<br>Direction)
P(crm:E7_activity) --> |crm:P14_carried_out_by| A("crm:E21_Person<br>John Doe")

B(E7_activity) -->|crm:P14_carried_out_by| A("crm:E21_Person<br>John Doe")
B(E7_activity) -->|crm:P2_has_type| C(E55_type<br>Fréquentation)

B(E7_activity) --->|crm:P7_took_place_at| K(E53_place<br>Philharmonie de Paris)
I(crm:E74_group) -->|crm:P2_has_type| J(crm:E55_type<br>institution<br>aat:300026004)
I(crm:E74_group) -->|crm:P55_has_current_location| K(crm:E53_place)
K(crm:E53_place<br>Philharmonie de Paris) --> |crm:P1_is_identified_by| S(crm:E42_identifier)
S(crm:E42_identifier) --> |crm:P2_has_type| T(crm:E55_type<br>adresse<br>aat:300386983)
S(crm:E42_identifier) --> |crm:P190_has_sympbolic_value| U(221 Av. Jean Jaurès, 75019 Paris)
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

