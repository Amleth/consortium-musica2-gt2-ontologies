# Transcription d'une œuvre

## a. Besoins musicologiques

L'acte de transcription musicale implique un certain nombre d'entités qu'il convient d'identifier avec précision dans le cadre de l'indexation conceptuelle : œuvre originelle, œuvre transcrite, compositeur et transcripteur, dans l'éventualité où les deux tâches seraient accomplies par des personnes différentes.

## b. Problématisation

De quelle manière peut-on exprimer l'action de transcription d'une œuvre existante ? 

## c. Contextualisation technique

Le compositeur et le transcripteur doivent être clairement nommés et identifiés, si possible à l'aide d'une URI, et les activités de transcription et de composition sont typées à l'aide du Thésaurus Getty AAT. Nous datons également l'action de transcription. 

## d. Proposition Cidoc-CRM


```mermaid
graph TD;

H[crm:F27_work_creation] --> |crm:P9_consists_of| A[crm:E7_activity]
H[crm:F27_work_creation] --> |crm:P9_consists_of| D[crm:F27_work_creation]

A[crm:E7_activity] --> |crm:p2_has_type| B[crm:E55_type<br>Transcription<br>aat:300404333]
A[crm:E7_activity] --> |crm:p14_carried_out_by| C[crm:E21_person<br>John Doe<br>URI]
A[crm:E7_activity] --> |crm:p16_used_specific_object| D[crm:F27_work_creation]
A[crm:E7_activity] --> |crm:p4_has_time_span| G(crm:E52_time_span<br>Date ISO 8601)

E[crm:E7_activity] --> |crm:p14_carried_out_by| F[crm:E21_person<br>Jane Doe<br>URI]
E[crm:E7_activity] --> |crm:p2_has_type| G[crm:E55_type<br>Composition<br>aat:300417577]
D[crm:F27_work_creation]  --> |crm:P9_consists_of| E[crm:E7_activity]

```

