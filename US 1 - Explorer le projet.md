En tant que développeur nouvellement onboardé, je souhaite comprendre la structure et les responsabilités de chaque couche, afin de pouvoir contribuer efficacement à l'API.
==

## WHY

C'est ton premier jour chez TaskFlow. Le tech lead t'a donné accès au repo et t'attend demain matin pour ta première PR. Pas de panique : l'équipe utilise GitHub Copilot pour accélérer l'onboarding. Tu dois comprendre rapidement l'architecture actuelle pour être autonome sur les prochaines évolutions.

## WHAT

Explorer la structure de l'API TaskFlow et comprendre le rôle de chaque composant :

- **Architecture** : identifier les couches (API, Service, Repository, DB)
- **Responsabilités** : comprendre la structure du code et le rôle de chaque fichier
- **Flux de données** : analyser le parcours complet d'une requête `POST /tasks` de l'entrée à la base de données

## HOW

- Utilise **Ask Mode** pour demander :
    - "Explique-moi la responsabilité de TaskService"
    - "Analyse le flux complet d'un POST /tasks"
    - Utilise les symlinks pour faciliter le travail de Copilot
- Utilise `/explain` dans les fichiers pour comprendre les méthodes clés
- Pose des questions sur les cas limites et la gestion d'erreurs

## RESSOURCES

- [Explorer une codebase avec Copilot](https://docs.github.com/en/copilot/tutorials/explore-a-codebase#example-prompts)
- [Modes Ask, Edit et Agent](https://github.blog/ai-and-ml/github-copilot/copilot-ask-edit-and-agent-modes-what-they-do-and-when-to-use-them/)

## VALIDATION CRITERIA

- Tu peux expliquer le rôle de chaque fichier
- Tu comprends le flux complet d'une requête HTTP jusqu'à la base de données