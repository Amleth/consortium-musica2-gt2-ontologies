# Indexation d'un lieu

## a. Besoins musicologiques

## b. Problématisation 

## c. Contextualisation technique

Quels sont les critères d'indexation nécessaires pour identifier un lieu ? Utiliser le E53 ou le E74 comme critère d'indexation

## d. Proposition Cidoc-CRM

```mermaid
graph TD;

A(crm:E53_place<br>Bibliothèque_Nationale_de_France) --> |crm:P168_is_defined_by| B(crm:E94_space_primitive<br>48.82978, 2.37708)
C(crm:E74_group<br>Institution<br>aat:300026004) --> |crm:P74_has_current_or_former_residence| A(crm:E53_place<br>Bibliothèque_Nationale_de_France)
A(crm:E53_place<br>Bibliothèque_Nationale_de_France) --> |crm:P1_is_identified_by| D(crm:P190_has_symbolic_content<br>Quai François Mauriac, 75706 Paris)


```

Faire un E74 connecté à un E53 avec un P74 et pas besoin de E13 / représenter le fait qu'une institution a plusieurs lieux
E44 et E45 n'existent plus, l'adresse P1 --> E41 adresse postale

E74 BNF / E53 le site Tolbiac P1 --> E41 --> P190 ("3 rue blablabla")
                                         --> P2 --> E55 --> P1 ("adresse")
