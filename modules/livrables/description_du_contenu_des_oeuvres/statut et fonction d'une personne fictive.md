## Statut et fonction d'une personne fictive

### a. Besoins musicologiques

Lorsque dans certains récits - notamment mythologiques - certaines personnes sont évoquées et que leur existence réelle ne peut être prouvée, il est nécessaire de leur attribuer des caractéristiques les différenciant de personnes réelles. Par exemple, le personnage (fictif) incarné par un chanteur (personne réelle) au sein d'un Opéra. Il convient ensuite de détailler différents attributs du rôle vis-à-vis de l'univers dans lequel il s'inscrit.

### b. Problématisation

De quelle manière peut-on préciser le caractère fictif d'une personne ? 

### c. Contextualisation technique

Afin de préciser le caractère fictif d'une personne, nous prenons le parti d'utiliser un 'E13_attribute_assignement' auquel est assigné - à l'aide de la propriété ```crm:P141_assigned``` - un ```crm:E55_type "protagonist"``` référencé au sein du thésaurus Getty AAT. 

Pour exprimer le statut et/ou la fonction d'une personne au sein d'une institution, nous reprenons notre protocole détaillé dans la fiche _Statut ou fonction d'une personne réelle_. Nous exprimons la fonction d'une personne par l'usage de deux ```crm:E74_group``` ; le premier d'entre eux correspond à la structure qui accueille la personne et le second, inclus dans le premier, détaille la fonction occupée. Il est posssible de raffiner encore plus le processus par l'usage de ```crm:E74_group``` supplémentaires, jusqu'à arriver au niveau de précision attendu. Les concepts adjacents aux ```crm:E74_group``` sont typés à l'aide du Getty AAT pour assurer une interopérabilité maximale.

### d. Proposition CIDOC CRM

```mermaid
graph TD;

M(crm:E74_group<br>«Daily Bugle») -->|crm:P2_has_type| N(crm:E55_type<br>institution<br>aat:300026004)
U[crm:E85_joining] --> |crm:P144_joined_with| M(crm:E74_group<br>«Daily Bugle»)
M(crm:E74_group<br>«Daily Bugle») --> |crm:P107_has_current_or_former_member| S(crm:E74_group)
S(crm:E74_group) --> |crm:P2_has_type| T(crm:E55_type<br>Direction<br>aat:300404157)
U[crm:E85_joining] -->|crm:P143_joined| K(crm:E89_propositionnal_object<br>crm:E21_person<br>«J. Jonah Jameson»)

R(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| K(crm:E89_propositionnal_object<br>crm:E21_person<br>«J. Jonah Jameson»)
R(crm:E13_attribute_assignement) --> |crm:P141_assigned| C(crm:E55_type<br>protagonist<br>aat:300410266)
R(crm:E13_attribute_assignement) --> |crm:P177_assigned_property_of_type| V(crm:P2_has_type)
R(crm:E13_attribute_assignement) --> |crm:P14_carried_out_by| W(crm:E21_person<br>John Doe)

```
