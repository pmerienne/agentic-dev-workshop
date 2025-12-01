En tant que utilisateur, je souhaite pouvoir assigner un ou plusieurs tags à mes tâches, afin de les organiser par catégorie (personnel, travail, urgent, etc.)

---

## WHY

Les utilisateurs power de TaskFlow gèrent des dizaines de tâches simultanément et demandent depuis des mois un système de catégorisation flexible. Contrairement aux projets fixes, les tags permettraient d'organiser dynamiquement leurs tâches ("urgent", "client-X", "perso"). C'est une des fonctionnalités les plus votées sur le feedback board. Time to ship!

## WHAT

Implémenter un système complet de tags avec relation many-to-many :

- **Modèle `Tag`** : créer une entité avec `id`, `name` unique
- **Relation** : table d'association pour relier `Task` et `Tag` (many-to-many)
- **Endpoints de gestion** :
  - `POST /tasks/{id}/tags` : assigner un ou plusieurs tags à une tâche
  - `DELETE /tasks/{id}/tags/{tag_id}` : retirer un tag d'une tâche
  - `GET /tags` : lister tous les tags existants
- **Filtrage** : `GET /tasks?tags=urgent,travail` pour récupérer les tâches ayant ces tags
- **Règles métier** :
  - Maximum 5 tags par tâche
  - Nom de tag unique, non vide, longueur entre 3 et 30 caractères
  - Caractères autorisés : lettres, chiffres, espaces, tirets, underscores
  - Réutilisation automatique des tags existants (pas de doublons)

## HOW

- Commence par utiliser **Plan Mode** pour demander un **plan d'implémentation détaillé** de cette fonctionnalité en copiant/collant les spécifications de cette user-story
- Clique sur "start implementation" pour passer en mode **Agent** et implémenter cette nouvelle fonctionnalité
- Prend un café et regardes copilot travailler, n'hésites pas à le guider si il commence à se perdre

## RESSOURCES
- https://code.visualstudio.com/docs/copilot/chat/chat-planning


## VALIDATION CRITERIA

- Entité `Tag` créée avec relation many-to-many vers `Task`
- Endpoints `POST /tasks/{id}/tags`, `DELETE /tasks/{id}/tags/{tag_id}`, `GET /tags` fonctionnels
- Endpoint `GET /tasks?tags=...` filtre correctement les tâches
- Validation des règles métier (max 5 tags, contraintes sur le nom)
- Tests unitaires couvrent les cas nominaux et limites
- Pas de tags dupliqués en base (réutilisation automatique)