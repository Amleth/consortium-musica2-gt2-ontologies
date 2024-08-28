# Propriétaire d'un objet

## a. Besoins musicologiques



## b. Problématisation


## c. Contextualisation technique


## d. Proposition Cidoc-CRM

```mermaid
graph TD;

E(crm:E13_attribute_assignement) --> |crm:P140_assigned_attribute_to| B(crm:E19_Physical_Object)
E(crm:E13_attribute_assignement) --> |crm:P141_assigned| A(crm:E21_person)
E(crm:E13_attribute_assignement) --> |crm:P177_assigned| F(crm:E55_type<br>acquisition<br>aat:300157782)

C(crm:E7_activity) -->|crm:P2_has_type| F(crm:E55_type<br>acquisition<br>aat:300157782)


```
