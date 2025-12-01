En tant que développeur backend, je souhaite corriger une erreur empêchant la mise à jour du statut d'une tâche, afin de restaurer les fonctionnalités du front.
==

## WHY

Le frontend a signalé un bug critique en production : quand un utilisateur coche une tâche comme "completed", l'API retourne un 200 OK mais l'état ne persiste pas en base. Les utilisateurs rechargent la page et voient leurs tâches redevenir "non complétées". Le support client est submergé de tickets. Il faut corriger ça rapidement avec une approche test-driven.

## WHAT

Mettre en place un framework de tests et identifier puis corriger le bug de mise à jour du statut `completed` :

- **Tests** : installer et configurer  un framework de tests pour le projet
- **Reproduction** : créer un test qui reproduit le bug (mise à jour de `completed` qui ne persiste pas)
- **Diagnostic** : identifier la cause racine (problème de commit DB, validation incorrecte, etc.)
- **Correction** : implémenter le fix et s'assurer que le test passe
- **Non-régression** : ajouter des tests pour les autres champs modifiables

## DESCRIPTION DU BUG

Le champ `completed` ne persiste pas lors d'un `PUT /tasks/{id}` avec `status: "ARCHIVED"`:
- **Comportement actuel** : L'API retourne 200 OK mais `completed` reste `false` après rechargement.
- **Comportement attendu** : `status: "ARCHIVED"` doit automatiquement passer `completed: true` et persister en base.


## HOW

- En mode **Agent**, met en place un framework de test avec **`/setupTests`**
- Utilise **`/tests`** pour créer un test unitaire qui reproduit le bug
- Corrige le bug dans l'IDE avec un Quick Fix ou manuellement avec **`/fix the #testFailure`**
- Tu peux demander à l'agent de lancer automatiquement les tests avec `#runTests`

## RESSOURCES

- [Écrire des tests avec Copilot](https://docs.github.com/en/copilot/tutorials/write-tests)

## VALIDATION CRITERIA

- Un frameowork de test est configuré et fonctionnel sur le projet
- Un test reproduit le bug (doit échouer initialement)
- Le bug est corrigé et le test passe au vert
- Le champ `completed` se met à jour correctement via `PUT /tasks/{id}`
- Couverture de tests pour les cas nominaux de mise à jour de tâches
