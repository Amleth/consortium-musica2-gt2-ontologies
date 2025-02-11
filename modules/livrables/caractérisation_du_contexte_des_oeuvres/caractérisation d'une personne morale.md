## Caractérisation d'une personne morale

### a. Besoins musicologiques

Une personne morale est, par définition, une entité regroupant divers individus regroupés sous un statut juridique, œuvrant de manière commune. Afin de caractériser une personne morale, il convient de signaler plusieurs éléments majeurs : les différentes personnes le composant, le statut juridique, la date de création de l'entité, le lieu éventuel où son bureau est établi, _etc._

### b. Problématisation

De quelle manière peut-on indiquer les caractéristiques principales d'une personne morale et les modéliser ?

### c. Contextualisation technique

Nous faisons ici usage de l'entité 'E66_formation', qui permet de témoigner de la création d'un 'E74_group'. Nous utilisons à nouveau notre protocole de datation ainsi que des entrées du thésaurus Getty AAT afin de typer les concepts d'_institution_, d'_adresse_ ou encore de _coordonnées géographiques_.

### d. Proposition CIDOC CRM

```mermaid
graph TD;

A(crm:E39_actor) --> |crm:P2_has_type| B(crm:E55_type<br>Personne morale<br>aat:300025969)
C(crm:E66_formation) --> |crm:P95_has_formed| A(crm:E74_group)
A(crm:E74_group) --> |crm:P1_is_identified_by| I(Société Française de Musicologie)
A(crm:E74_group) -->|crm:P74_has_current_or_former_residence| D(crm:E53_place<br>Bibliothèque Nationale de France)

D(crm:E53_place<br>Société Française de Musicologie) --> |crm:P1_is_identified_by| F(crm:E42_Identifier)
F(crm:E42_Identifier) --> |crm:P190_has_symbolic_content| G(58 rue de Richelieu, 75002, Paris)
F(crm:E42_Identifier) --> |crm:P2_has_type| H(crm:E55_has_type<br>adresse<br>aat:300386983)

D(crm:E53_place<br>Société Française de Musicologie) --> |crm:P1_is_identified_by| M(crm:E42_Identifier)
M(crm:E42_Identifier) --> |crm:P168_is_defined_by| E(crm:E94_space_primitive<br>48.8680388, 2.3356072)
M(crm:E42_Identifier) --> |crm:P2_has_type| N(crm:E55_type<br>coordonnées géographiques<br>aat:300387569)


```
