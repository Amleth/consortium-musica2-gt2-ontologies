# Dédicataire d'une œuvre

## a. Besoins musicologiques

La dédicace d'une œuvre musicale diffère de la commande dans la mesure où n'elle n'induit aucun soutien financier, à moins que le commanditaire et le dédicataire soient la même personne. Le dédicataire peut-être un proche du compositeur, mais aussi une figure publique ; il peut s'agir d'un témoignage d'affection mais aussi d'admiration, sans nécessairement signaler un lien de proximité dans la vie réelle.

## b. Problématisation

Comment exprimer la dédicace, mention textuelle présente au sein de la partition ? Il s'agira également de distinguer clairement cette notion de la commande en marquant la différence entre l'aspect institutionnel de la commande et l'aspect plus personnel de la dédicace, mais aussi de distinguer l'étape de l'œuvre où la dédicace est fixée. 

## c. Contextualisation technique

Le thesaurus Getty AAT est à nouveau utilisé afin de typer les différentes activités mais aussi statuts du graphe Cidoc-CRM. Dans le cadre d'un cas concret, nous pourrons également ajouter des URI pour un niveau de précision accru. Nous faisons également appel au modèle FRBR en mettant en exergue la manifestation sur laquelle apparait la dédicace.

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

M(crm:F27_work_creation) --> |crm:P9_consists_of| C(crm:E7_activity)
M(crm:F27_work_creation) --> |crm:P9_consists_of| A(crm:F27_work_creation)
M(crm:F27_work_creation) --> |crm:P9_consists_of| G(crm:F27_work_creation)

C(crm:E7_activity) --> |crm:P2_has_type| O(crm:E55_type<br>Dedication<br>aat:300026114)
C(crm:E7_activity) --> |crm:P14_carried_out_by| L(crm:E21_person<br>Compositeur<br>aat:300025671<br>URI)

A(crm:F27_work_creation) --> |crm:P14_carried_out_by| L(crm:E21_person<br>Compositeur<br>aat:300025671)
A(crm:F27_work_creation) --> |lrm:R16_created| B(crm:F1_work)
A(crm:F27_work_creation) --> |crm:P2_has_type| N(E55_type<br>Composition musicale<br>aat:300417577)
A(crm:F27_work_creation) --> |crm:P4_has_time_span| J(crm:E52_time_span<br>Date ISO 8601)

G(crm:F27_work_creation) --> |lrm:R16_created| E(crm:F3_manifestation) 
E(crm:F3_manifestation) --> |crm:P3_has_note| H(crm:E34_inscription)
H(crm:E34_inscription) --> |crm:p2_has_type| F(crm:E55_type<br>Dedicatee<br>aat:300121765)

```

