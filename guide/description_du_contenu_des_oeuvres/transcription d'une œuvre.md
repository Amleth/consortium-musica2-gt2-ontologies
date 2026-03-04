## Transcription d'une œuvre

### a. Besoins musicologiques

L'acte de transcription musicale implique un certain nombre d'entités qu'il convient d'identifier avec précision dans le cadre de l'indexation conceptuelle : œuvre originelle, œuvre transcrite, compositeur et transcripteur, dans l'éventualité où les deux tâches seraient accomplies par des personnes différentes.

### b. Problématisation

De quelle manière peut-on exprimer l'action de transcription d'une œuvre existante ? 

### c. Contextualisation technique

Nous nous appuyons sur le modèle FRBR pour caractériser l'œuvre ; dans le cadre d'une transcription, le niveau auquel nous nous intéressons est celui de l'expression et est intégré dans le graphe par l'usage de 'F2_expression', portées par des personnes 'E21_person' - clairement nommées et identifiées, si possible à l'aide d'une URI- , tandis que les actions de transcription et de composition sont typées à l'aide du Thésaurus Getty AAT. Celles-ci résultent en des 'F28_Expression_Creation'.

### d. Proposition CIDOC CRM

```mermaid
graph TD;

E[crm:F28_Expression_Creation] --> |crm:p2_has_type| G[crm:E55_type<br>Composition<br>aat:300417577]
E[crm:F28_Expression_Creation] --> |crm:p14_carried_out_by| F[crm:E21_person<br>Jane Doe<br>URI]
E[crm:F28_Expression_Creation] --> |crm:R17_created| M(F2_expression)

N(F2_expression) --> |lrm:R76_is_derivative_of| M(F2_expression)
A[crm:F28_Expression_Creation] --> |crm:R17_created| N(F2_expression)

A[crm:F28_Expression_Creation] --> |crm:p2_has_type| B[crm:E55_type<br>Transcription<br>aat:300404333]
A[crm:F28_Expression_Creation] --> |crm:p14_carried_out_by| C[crm:E21_person<br>John Doe<br>URI]
A[crm:F28_Expression_Creation] --> |crm:p4_has_time_span| I(crm:E52_time_span<br>Date ISO 8601)





```

