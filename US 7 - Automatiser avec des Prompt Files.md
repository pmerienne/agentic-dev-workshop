En tant que développeur TaskFlow, je souhaite automatiser des tâches récurrentes avec des prompt files, afin de gagner du temps et garantir la cohérence du code.
==

## WHY

L'équipe TaskFlow grandit vite et les tâches se répètent : créer de nouveaux endpoints CRUD, générer des tests, faire des code reviews, documenter les API... Chaque dev reformule les mêmes demandes à Copilot, avec des résultats variables selon le prompt. Le lead tech a constaté que certains passent 10 minutes à écrire un prompt détaillé que d'autres devront réécrire demain. Les prompt files permettent de créer une bibliothèque réutilisable de commandes standardisées : un gain de temps immédiat et une qualité homogène. C'est le moment d'industrialiser notre usage de Copilot !

## WHAT

Créer une bibliothèque de prompt files pour automatiser les tâches récurrentes du projet TaskFlow :

### 1. Prompt `/code-review` - Révision de code automatisée
- **Objectif** : Analyser du code sélectionné selon les standards TaskFlow
- **Comportement** :
  - Vérifie le respect des conventions (nommage, architecture, documentation)
  - Détecte les problèmes de sécurité ou performance
  - Suggère des améliorations concrètes
  - Format de sortie structuré (✅ OK / ⚠️ À améliorer / ❌ À corriger)

### 2. Prompt `/api-doc` - Générer la documentation OpenAPI/Swagger
- **Objectif** : Créer automatiquement la doc d'un endpoint
- **Comportement** :
  - Analyse les méthodes du controller
  - Documente les codes de retour, paramètres, body
  - Inclut des exemples de requête/réponse

### 3. Prompt `/new-endpoint` - Générer un nouveau endpoint CRUD
- **Objectif** : Créer un endpoint complet (Controller + Service + Repository) en respectant l'architecture TaskFlow
- **Input variables** :
  - Nom de l'entité (ex: "Comment", "Attachment")
  - Type d'opération (GET, POST, PUT, DELETE)
- **Comportement** :
  - Génère le code dans les bonnes couches
  - Applique les conventions de nommage
  - Inclut la validation et la gestion d'erreurs
  - Respecte les custom instructions du projet

### 4. Prompt `/adr` - Créer un Architectural Decision Record
- **Objectif** : Générer un ADR structuré pour une décision architecturale
- **Input variables** :
  - Context (problème, contraintes, exigences)
  - Decision (solution choisie avec justification)
  - Alternatives (autres options considérées)
  - Stakeholders (parties prenantes)
- **Comportement** :
  - Suit le format standardisé ADR avec front matter
  - Documente les conséquences positives et négatives
  - Inclut les alternatives avec justification du rejet
  - Sauvegarde dans `/docs/adr/` avec convention `adr-NNNN-[title-slug].md`

## HOW

0. **Créer le dossier de prompts** `.github/prompts` à la racine du projet (`/java` ou `./python`), c'est ici que vivront tous les prompt files du workspace
1. Créer le prompt `.github/prompts/code-review.prompt.md`
2. Créer le prompt `.github/prompts/api-doc.prompt.md`
3. Créer le prompt `.github/prompts/new-endpoint.prompt.md`
4. Créer le prompt `.github/prompts/adr.prompt.md` en utilisant le template de [awesome-copilot](https://github.com/github/awesome-copilot/blob/main/prompts/create-architectural-decision-record.prompt.md)
5. **Tester les prompt**
   - Ouvre le chat Copilot (`Ctrl+Alt+I`)
   - Tape `/new-endpoint`, `/api-doc`, `/code-review` ou `/adr`
   - Fournis les inputs demandés (ex: "POST" et "Comment" pour `/new-endpoint`)
   - Observe Copilot générer tout le code ou la documentation nécessaire
   - Si les résultats ne sont pas satisfaisants, modifie le prompt
   - Teste de nouveau jusqu'à obtenir un résultat de qualité consistant


## RESSOURCES

- [Prompt Files Tutorial - GitHub Docs](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file)
- [Prompt Files in VS Code](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Awesome GitHub Copilot - Community Prompts](https://github.com/github/awesome-copilot/blob/main/docs/README.prompts.md)

## VALIDATION CRITERIA

- ✅ Le dossier `.github/prompts/` contient au moins 4 prompt files
- ✅ `/new-endpoint` génère du code cohérent dans les 3 couches (Controller/Service/Repository)
- ✅ `/code-review` produit une analyse structurée avec recommandations concrètes
- ✅ `/api-doc` crée une documentation OpenAPI complète et réaliste
- ✅ Les prompts référencent les custom instructions existantes
- ✅ Les descriptions sont claires et guident l'utilisateur
- ✅ Les `argument-hint` aident à comprendre les inputs attendus
