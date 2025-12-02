En tant que développeur nouvellement onboardé, je souhaite comprendre la structure et les responsabilités de chaque couche, afin de pouvoir contribuer efficacement à l'API.
==

## WHY

C'est ton premier jour chez TaskFlow. Le tech lead t'a donné accès au repo et t'attend demain matin pour tes premiers développements. Pas de panique : l'équipe utilise GitHub Copilot pour accélérer l'onboarding. Tu dois comprendre rapidement l'architecture actuelle pour être autonome sur les prochaines évolutions. Prends le temps de bien comprendre la validation des tâches, elle est assez complexe.

## WHAT

Explorer la structure de l'API TaskFlow et comprendre le rôle de chaque composant :

- **Architecture** : identifier les couches (API, Service, Repository, DB)
- **Responsabilités** : comprendre la structure du code et le rôle de chaque fichier
- **Flux de données** : analyser le parcours complet d'une requête `POST /tasks` de l'entrée à la base de données

## HOW
- Ouvre le chat de copilot avec `Ctrl` + `Alt` + `I` (ou `Cmd` + `Shift` + `I`)
- Utilise **Ask Mode** pour demander :
    - "Explique-moi la responsabilité du service de gestion des tâches"
    - "Analyse le flux complet d'un POST /tasks"
- Surligne du code, ouvre l'inline chat (`Ctrl` + `I` ou `Cmd` + `I`)) et utilise `/explain` pour comprendre la fonction de validation des Task
- Pose des questions sur les cas limites et la gestion d'erreurs

## RESSOURCES

- [Best practices for using GitHub Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot#using-github-copilot-chat)
- [Modes Ask, Edit et Agent](https://github.blog/ai-and-ml/github-copilot/copilot-ask-edit-and-agent-modes-what-they-do-and-when-to-use-them/)

## VALIDATION CRITERIA

- Tu peux expliquer le rôle de chaque fichier
- Tu comprends le flux complet d'une requête HTTP jusqu'à la base de données
- Tu connais le fonctionnement de la validation des tâches
