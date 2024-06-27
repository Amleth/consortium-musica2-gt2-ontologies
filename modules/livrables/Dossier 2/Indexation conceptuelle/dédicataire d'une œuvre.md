# Dédicataire d'une œuvre

## a. Besoins musicologiques

La dédicace d'une œuvre musicale diffère de la commande dans la mesure où n'elle n'induit aucun soutien financier, à moins que commanditaire et dédicataire soient la même personne. Le dédicataire peut-être un proche du compositeur, mais aussi une figure publique ; il peut s'agir d'un témoignage d'affection mais aussi d'admiration.

## b. Problématisation

Comment exprimer la dédicace, mention textuelle présente au sein de la partition ? Il s'agira également de distinguer clairement cette notion de la commande en marquant la différence entre l'aspect institutionnel de la commande et l'aspect plus personnel de la dédicace.

## c. Contextualisation technique

Nous ferons de nouveau appel au thesauras Getty Aat afin de typer les différents éléments du graphe Cidoc-CRM.

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E22_person<br>John Doe) --> |crm:p2_has_type| B(crm:E55_type<br>Composer<br>aat:300025671) 
A(crm:E22_person<br>John Doe) --> |crm:p94_has_created| C(crm:E28_conceptual_object<br>Œuvre)
D(crm:E37_mark<br>To_Jane_Doe) ---> |crm:p67_refers_to| C(crm:E28_conceptual_object<br>Œuvre)

G(crm:F27_work_creation) --> |lrm:R16_created| E(crm:F3_manifestation) 
E(crm:F3_manifestation) --> |crm:P3_has_note| H(crm:E34_inscription)
H(crm:E34_inscription) --> |crm:p2_has_type| E(crm:E55_type<br>Dedicatee<br>aat:300121765)



```

