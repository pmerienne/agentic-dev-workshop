En tant que utilisateur, je souhaite connaître la date de création d'une tâche, afin de suivre l'ancienneté et l'historique de mes tâches
==

## WHY

L'équipe support remonte un problème récurrent : impossible de distinguer les tâches créées récemment de celles qui traînent depuis des semaines. Le nouveau dashboard d'analytics nécessite ces données pour calculer les métriques de vélocité. Sans horodatage de création, on navigue à l'aveugle. Il est temps d'ajouter cette information essentielle.

## WHAT

Ajouter une date de création au Task pour tracer la date et l'heure de création.
Ce champ doit être automatiquement renseigné à la création et ne doit pas être modifiable par l'utilisateur.

## HOW

- Ouvre le ficher qui définit les `Task` et utilise l'**Edit Mode** pour ajouter le nouveau champ
- Passe en mode **Agent** et demande lui de vérifier le fonctionnement de l'API
- Si l'agent ne parvient pas à démarrer/utiliser l'API :
    - Consulte la "chat debug view" pour voir quelles informations sont à sa disposition
    - Fournis-lui la documentation nécessaire en utilisant le glisser-déposer ou avec un `#`


## RESSOURCES
- https://github.blog/ai-and-ml/github-copilot/copilot-ask-edit-and-agent-modes-what-they-do-and-when-to-use-them/
- https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- https://code.visualstudio.com/docs/copilot/chat/chat-debug-view

## VALIDATION CRITERIA

- Les API sont toujours fonctionnelles et supportent cette nouvelle date
- ex: GET /task/{task_id} renvoie le champ, PUT et POST créé et mette à jour le champ
