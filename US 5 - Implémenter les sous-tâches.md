En tant que utilisateur méthodique, je souhaite créer des sous-tâches associées à une tâche principale, afin de mieux structurer mon travail complexe.
==

## WHY

Le board vient d'annoncer TaskFlow Premium lors de la keynote annuelle. Les investisseurs sont enthousiastes : les sous-tâches permettront de structurer des projets complexes et de justifier l'abonnement premium. La date de livraison est déjà annoncé et l'équipe produit compte sur nous pour livrer rapidement cette fonctionnalité stratégique qui différenciera TaskFlow de la concurrence.

## WHAT

- Ajouter une entité `Subtask`
    1. **Propriétés minimales**
        - `id` (unique, généré par le système)
        - `title` (obligatoire)
        - `status`
        - `parentTaskId` (référence obligatoire vers une `Task` existante)
        - Optionnel : `description`, `dueDate`, `position` (pour l’ordre), `createdAt`, `updatedAt`.
    2. **Validation du titre**
        - Le titre est **obligatoire** (non nul, non vide après trim).
        - Longueur : par exemple `3 <= length(title) <= 100`.
        - Pas uniquement des espaces ou caractères de contrôle.
        - Normalisation : trim des espaces en début/fin, réduction des espaces multiples internes.
    3. **Statut initial**
        - À la création, si aucun statut n’est fourni → statut par défaut `TODO`.
    4. **Suppression**
        - Supprimer une `Subtask` ne doit **jamais** supprimer sa `Task` parente.
        - Une `Subtask` supprimée ne doit plus être renvoyée par les endpoints publics (soft delete possible côté infra, mais métier = “indisponible”).
- Relation OneToMany Task → Subtask
    1. **Existence du parent**
        - Toute `Subtask` doit être rattachée à une `Task` existante.
        - Si la Task n’existe pas ou n’est pas accessible à l’utilisateur → erreur (404 ou 403 selon le cas).
    2. **Immutabilité du parent**
        - Une fois créée, la `Subtask` ne peut pas changer de `parentTaskId` (pas de “déplacement” vers une autre tâche par simple update).
        - Un changement de parent, si nécessaire, doit passer par un cas d’usage dédié (ex : “déplacer la sous-tâche”), avec règles spécifiques.
    3. **Cascades**
        - Suppression d’une `Task` :
            - règle stricte : toutes les `Subtasks` associées sont également supprimées ou archivées (à définir, mais le comportement doit être **cohérent et documenté**).
        - Archivage d’une `Task` :
            - toutes les `Subtasks` doivent être considérées comme archivées également (non modifiables).
    4. **Limite du nombre de sous-tâches**
        - Optionnel : limiter le nombre de `Subtasks` par `Task` (ex. 50), surtout en contexte premium & performance.
        - Si la limite est atteinte → erreur métier claire : `MAX_SUBTASKS_REACHED`.
    5. **Cohérence de statut avec la Task**
        - Une `Task` marquée `DONE` ne peut plus recevoir de nouvelles `Subtasks` (ou alors les nouvelles sous-tâches sont automatiquement `DONE`, selon la politique choisie).
        - Si la `Task` repasse de `DONE` à `TODO` ou `IN_PROGRESS`, ses `Subtasks` conservent leur statut, mais on peut définir une règle métier explicite :
            - soit on ne touche pas aux `Subtasks`,
            - soit on remet en TODO les sous-tâches non DONE, etc.
- API associée
    
    **`POST /tasks/{id}/subtasks`**
    
    - Crée une nouvelle `Subtask` rattachée à la `Task` `{id}`.
    - Règles :
        - Vérifier l’existence et l’accessibilité de la Task.
        - Vérifier que la Task n’est pas archivée/supprimée.
        - Vérifier la limite max de sous-tâches.
        - Appliquer la validation du titre.
        - Status par défaut à `TODO` si non fourni.
    - Erreurs typiques :
        - `404` si Task introuvable.
        - `403` si l’utilisateur n’a pas les droits sur la Task.
        - `400` si validation échoue (titre invalide, limite max atteinte, etc.).
    
    **`GET /subtasks/{id}`**
    
    - Ne renvoie la sous-tâche que si l’utilisateur a accès à la `Task` parente.
    
    **`PUT/PATCH /subtasks/{id}`**
    
    - Modifiables : `title`, `status`, `description`, `dueDate`, éventuellement `position`.
    - Non modifiable : `parentTaskId`, `id`, dates de création.
    - Re-valider le titre à chaque update si modifié.
    - Appliquer les règles de cohérence (ex. statut vs statut de la Task parente, dueDate).
    
    **`DELETE /subtasks/{id}`**
    
    - Suppression logique/fonctionnelle :
        - Interdite si la Task parente est verrouillée, archivée ou si l’utilisateur n’a pas les droits de modification.
    - La suppression ne doit pas casser le calcul du statut de la Task (recalculer sur les sous-tâches restantes).
    
    **`GET /tasks/{id}/subtasks`**
    
    - Liste paginée et ordonnée des sous-tâches associées.
    - Respect de l’ordre (par `position` ou par `createdAt` si aucun ordre explicite).
    - Filtrage optionnel : par `status` (ex. `?status=TODO`).
- Règles métier “parent vs sous-tâches”
    
    **Task complétée vs sous-tâches**
    
    - Règle recommandée :
        - Une `Task` ne peut passer à `DONE` que si **toutes** ses `Subtasks` sont `DONE`.
        - Exception possible : permettre un “forçage” (par ex. via une action explicite “Marquer comme terminée malgré les sous-tâches incomplètes”), qui met alors toutes les sous-tâches en `DONE` ou `CANCELLED`.
    - Si on ne veut pas de forçage :
        - tentative de passage de la Task en `DONE` alors qu’il reste des sous-tâches non `DONE` → erreur métier.
    
    **Propagation descendante**
    
    - Si une `Task` passe en `DONE` :
        - soit toutes ses `Subtasks` passent automatiquement en `DONE`,
        - soit l’opération est refusée tant que ce n’est pas le cas (cf. règle précédente).
    - Si une `Task` passe en `CANCELLED` (si état existant) :
        - les `Subtasks` passent en `CANCELLED` aussi.
    
    **Dates d’échéance**
    
    - Si la `Task` a une `dueDate`, alors chaque `Subtask` :
        - ne doit pas avoir de `dueDate` **postérieure** à celle de la `Task` (ou au minimum, c’est validé côté métier).
    - Si on modifie la `dueDate` de la Task parente à une date antérieure :
        - soit on refuse si des sous-tâches ont une `dueDate` plus tardive,
        - soit on ajuste automatiquement les `dueDate` des sous-tâches.

## HOW

- Avant de coder : utiliser Copilot pour générer **une spécification détaillée** qui découpe cette US en plusieurs sous-tâches à développer (écrite dans des fichiers markdown)
- Utiliser Copilot pour développer les sous-tâches 1 à 1

## VALIDATION CRITERIA

- API fonctionnelle end-to-end.
- Code lisible et cohérent.
- Tests générés ou complétés avec Copilot.
- Les sous-tâches sont enregistrés et justifiés.