En tant que utilisateur, je souhaite définir une date limite pour une tâche, afin de mieux planifier mon travail
==

## WHY

Le PM vient de présenter la nouvelle roadmap : un calendrier des deadlines en vue Kanban. Le frontend est prêt, mais l'API ne stocke aucune date d'échéance. Les utilisateurs réclament cette fonctionnalité depuis des mois pour prioriser leurs tâches urgentes. C'est le moment d'implémenter ce champ critique.

## WHAT

Ajouter une due date au Task.
Pas de règle métier spécifique, juste assurer le CRUD complet (création, lecture, mise à jour, suppression) de ce champ.

**HOW** :

- Utilise **Agent Mode** pour générer toutes les modifications nécessaires.
- Valide le code généré pour assurer la qualité de l'API

**RESSOURCES :**
- https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

**VALIDATION CRITERIA** :

- Les API sont toujours fonctionnelles et supportent la due date
- ex: GET renvoie le champ.
