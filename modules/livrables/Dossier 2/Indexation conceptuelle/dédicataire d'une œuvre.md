# Dédicataire d'une œuvre

## a. Besoins musicologiques

La dédicace d'une œuvre musicale diffère de la commande dans la mesure où n'elle n'induit aucun soutien financier, à moins que commanditaire et dédicataire soient la même personne. Le dédicataire peut-être un proche du compositeur, mais aussi une figure publique ; il peut s'agir d'un témoignage d'affection mais aussi d'admiration.

## b. Problématisation

## c. Contextualisation technique

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E22_person<br>John Doe) --> |crm:p2_has_type| B(crm:E7_type<br>Composer)
A(crm:E22_person<br>John Doe) --> |crm:p94_has_created| C(crm:E28_conceptual_object<br>Œuvre)
D(crm:E37_mark<br>To_Jane_Doe) ---> |crm:p67_refers_to| C(crm:E28_conceptual_object<br>Œuvre)
C(crm:E28_conceptual_object<br>Œuvre) --> |xxx| F(frbroo:F28_expression_creation)
D(crm:E37_mark<br>To_Jane_Doe) ---> |crm:p2_has_type| E(crm:E7_type<br>Dedication)

```

