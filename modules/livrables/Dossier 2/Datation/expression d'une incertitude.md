# Expression d'une incertitude

## a. Besoins musicologiques

Le chercheur en sciences humaines doit pouvoir exprimer une incertitude avec souplesse, afin de transmettre avec justesse l'information scientifique, tout en étant conscient de la nécessité informatique d'une date précise exprimée dans un format référence. Il faut ainsi fournir une méthode permettant l'expression de divers doutes, besoins, _etc_. Par exemple, dans les répertoires les plus anciens, l'exactitude des dates est souvent difficile à établir, voire contestée. Les propositions de datation doivent donc être argumentées et justifiées.

## b. Problématisation

Quels sont les outils permettant l'expression de l'incertitude entourant une datation en Cidoc-CRM ? On constate par exemple que le terme _circa_ est régulièrement employé, malgré son manque de précision ; il convient donc de trouver une solution pour exprimer le doute et les propositions de divers chercheurs. 

## c. Contextualisation technique

Plusieurs instances de `crm:E13_Attribute_Assignment` viennent justifier les choix de datation, car toute attribution de date repose sur une interprétation, aussi minime soit-elle. Il convient ensuite au chercheur de se référer aux thésaurus et sources nécessaires afin de compléter sa proposition. **reprendre tout ce que Thomas a dit** Un vocabulaire contrôlé proposant des paliers d'expression de la certitude doit être proposé, et partagé au sein du Consortium Musica2.

## d. Proposition CIDOC CRM


```mermaid
graph TD;




I(crm:E67_birth) --> |crm:p98_brought_into_life| H(crm:E21_person<br>John Doe)
G(crm:E13_attribute_assignement) -->|crm:p141_assigned| B(crm:E52_time_span)
G(crm:E13_attribute_assignement) -->|crm:p177_assigned_property_of_type| K(crm:p4_has_time_span)
G(crm:E13_attribute_assignement)  --> |crm:p140_assigned_attribute_to| I(crm:E67_birth)

G(crm:E13_attribute_assignement) --> |crm:p14_carried_out_by| L(crm:E21_person<br>Chercheur)

B(crm:E52_time_span) --> |crm:p82a_begin_of_the_begin| C("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p81a_end_of_the_begin| D("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p81b_begin_of_the_end| E("Date ISO 8601")
B(crm:E52_time_span) --> |crm:p82b_end_of_the_end| F("Date ISO 8601")

```
