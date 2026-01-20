Guide formateur
==

Ce guide permet au formateur de comprendre l’intention pédagogique, structurer la séance de travaux dirigé et faciliter l’apprentissage actif.

# Cadre général

Cette formation se déroule sous forme de mini-projet dans lequel les apprenants réalisent une suite d’exercices fortement guidés pour développer leurs usages de l’IA en situation de développement.

**Guidelines** :
- **Installation en amont** : les prérequis techniques sont clairs et réalisables avant la session.
- **Fortement guidé** : chaque exercice fournit un cadre, des consignes et des attentes explicites.
- **Exercices indépendants** : chaque étape peut être réalisée sans bloquer l’ensemble du TP.
- **Alignement pédagogique** : chaque exercice sert un objectif d’apprentissage identifié.
- **Mini-projet proche du réel** : contexte, contraintes et livrables reflètent des situations professionnelles.

# Déroulement 

## En amont

Les apprenants installent et initialisent le projet (environnement, dépendances, repo) à partir des consignes fournies.

## Pendant la session

Le formateur :

- introduit le contexte et le déroulé global du TP
- reste disponible pour débloquer les apprenants,
- assure le **cadencement** de la session.
- le contexte narratif est là pour rapprocher du réel et sa compréhensio ne doit en aucun cas ralentir les apprenants

## Cadence par exercice

Pour chaque exercice, le formateur :

- laisse du temps à l’exploration et à la tentative autonome,
- restitue et explique la solution par une démonstration en **live coding**
- transmet les élements théoriques et concepts mentaux à l'oral

## Pédagogie

Fortement guidé par le formateur, cette formation verticale est **100 % orientée pratique**. La théorie est transmise à l’oral, au fil de l’exécution et des questions, jamais comme un prérequis formel.


# Pré-requis et préparation formateur
- Installation et initialisation du projet (environnement, dépendances, repo) à partir des consignes fournies.
- Vérification de la connection de l'IDE à Github Copilot
- Vérification de l'adéquation des exercices avec la version actuelle de Github Copilot


# Objectifs pédagogiques

| Objectif principaux                                          | Objectifs Secondaires                                                                                                                                              | Savoirs et compétences                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01 : Compréhension des modes de GitHub Copilot               | 011 : J’utilise Copilot Chat et l’inline chat pour obtenir des réponses ciblées dans mon code                                                                      | Utilisation de Copilot Chat dans l’éditeur, déclenchement de l’inline chat, formulation de questions contextuelles sur du code sélectionné, navigation dans l’historique de conversation, suppression des échanges non pertinents pour clarifier le contexte                            |
|                                                              | 012 : Je choisis le mode de Copilot le plus adapté à une tâche donnée                                                                                              | Rôle et fonctionnement des modes ask/edit/agent, impact de chaque mode sur le code (lecture seule, édition ciblée, modifications étendues), cas d’usage typiques, limites et risques associés                                                                                           |
|                                                              | 013 : J’analyse et j’interprète les interactions avec Copilot grâce au Chat Debug view (VsCode) pour optimiser mes prompts et comprendre le comportement du modèle | Fonctionnement du Chat Debug view, lecture du system prompt, analyse du user prompt envoyé, inspection du contexte transmis au modèle, compréhension du déroulé des réponses de l’IA, identification des outils déclenchés, amélioration des prompts grâce aux informations de débogage |
| 02: Intégration de Copilot dans le workflow de développement | 021 : J’organise mon environnement IDE pour fournir à Copilot le bon contexte                                                                                      | Notion de contexte pour un LLM, impact des fichiers ouverts sur les suggestions, sélection et fermeture de fichiers selon la tâche, usage des références (#file, #editor, @workspace), gestion de plusieurs fils de discussion (threads)                                                |
|                                                              | 022 : Je configure des instructions personnalisées pour guider le comportement de Copilot dans un projet                                                           | Principes des custom instructions, définition de règles de style et de standards d’équipe, prise en compte de la structure du dépôt (types de fichiers, architectures), limitation du contexte et adaptation des instructions aux modes edit et agent                                   |
|                                                              | 023 : J’utilise des prompt files et custom agents réutilisables pour standardiser et accélérer mes tâches de développement                                         | Création et usage de prompts réutilisables, Context Engineering, Structuration de workflows standards, Enchaînement guidé via handoffs                                                                                                                                                  |
| 03: Maîtrise de la rédaction de prompts pour GitHub Copilot  | 031 : Je structure un prompt clair pour générer du code à partir d’un besoin métier/technique                                                                      | Distinction entre besoin métier et traduction technique, Structure Goal/Context/Expectations, identification des contraintes (langage, framework, performance, style), Reflection Pattern for validation                                                                               |
|                                                              | 032 : Je réalise des tâches de développement complexes en maintenant des prompts simples, spécifiques et découpés en étapes                                        | Découpage d’un problème complexe en sous-tâches, rédaction d’instructions courtes et ciblées, définition d’entrées et sorties attendues, réduction de la taille des réponses, usage d’un enchaînement de requêtes plutôt qu’une demande monolithique                                    |
|                                                              | 033 : J’identifie et corrige les prompts ambigus pour obtenir des résultats plus pertinents                                                                        | Repérage des termes vagues ou ambivalents, clarification de la portée (fichier, fonction, projet), précision des bibliothèques ou versions à utiliser, reformulation progressive d’un prompt en plusieurs itérations, suppression ou nettoyage de l’historique non pertinent            |

# Détails des exercices

## US - 1
Développer le réflexe d'utiliser Copilot pour l'onboarding plutôt que la lecture exhaustive de code. Faire comprendre l'impact du contexte fourni sur la qualité des réponses.

**Concepts théoriques** :
- **Importance** : Accélérer la compréhension d'une codebase inconnue en utilisant l'IA plutôt que la lecture linéaire.
- **Contexte pour LLM** : fichiers ouverts, sélection de code, références (#file, @workspace)
- **Modes Copilot** : Ask (lecture seule), Edit (modifications ciblées), Agent (modifications étendues)
- **Slash command** : accélération des use-cases communs avec `/explain` sur du code sélectionné
- S'assurer de la formulation de questions précises et contextuelles

**Erreurs fréquentes** :
- Prompts trop vagues ("explique le projet", "/explain")
- Ne pas sélectionner le code avant d'utiliser l'inline chat
- Oublier de préciser la portée (fichier, fonction, projet)

## US - 2
Développer avec Github Copilot. Développer le réflexe d'utiliser le **Chat Debug View** pour ouvrir le capot et comprendre les échecs de l'agent.

**Concepts théoriques** :
- **Agentic Coding** : modification locale d'un fichier ouvert, exécution autonome
- **Prompt vs. Context** : ce que l'utilisateur écrit ≠ ce que le modèle reçoit (fichiers ouverts, sélections, références #file)
- **Chat Debug View** : inspection du contexte transmis au modèle, identification des outils utilisés, diagnostic des échecs
- **Erreurs fréquentes** : Ne pas interrompre un Agent dont le raisonnement s'égare

## US - 3
Utiliser les outils packagés avec Copilot pour adopter une approche qualité de code. Découvrir un flux de résolution de bug avec Github Copilot.

**Concepts théoriques** :
- **Slash commands spécialisés** : `/setupTests` , `/tests`, `/fix` 
- **Tools IDE** : `#testFailure` , `#runTests`
- **Quick Fix IDE** : exploitation des suggestions contextuelles pour corriger rapidement
- **TDD is a must** : Les tests servent de garde-fous et permettent a un agent d'auto-valider son code => itérer en autonomie

**Erreurs fréquentes** :
- Laisser Copilot générer des tests sans spécifications fonctionnelles
- Générer les tests après l'implémentation

## US - 4
Initiation au Spec-Driven-Development avec l'utilisation du **Plan Mode** puis **Agent Mode** pour implémenter une fonctionnalité complexe.

**Concepts théoriques** :
- **SDD** : Pour guider un agent sans micro-manager avec plus d'autonomie et éviter les itérations inutiles
- **Context Window** : Limite de tokens que le modèle peut traiter, nécessite de fournir uniquement le contexte pertinent pour éviter la surcharge et maintenir la cohérence des réponses
- **Compression** : Réduction de la quantité d'informations transmises en synthétisant les échanges précédents, en nettoyant l'historique non pertinent, et en structurant les prompts de manière concise
- **Plan Mode vs. Agent Mode** : À chaque agent un rôle limité pour améliorer ses performances : le Plan Mode réduit les risques de dérive et permet d'ajuster la direction avant l'implémentation.

**Erreurs fréquentes** :
- Passer directement en Agent sans demander de plan
- Utiliser du SDD pour de petites tâches
- Ne pas valider les étapes intermédiaires avant de continuer
- Spécifications trop détaillées ou verbeuses

## US - 5
Spec-Driven-Development à l'échelle, découpage en sous-tâches et utilisation de fichiers de spécifications comme artefacts intermédiaires pour maintenir la cohérence sans surcharger le contexte.

**Concepts théoriques** :
- **Découpage en sous-tâches** : Diviser un problème complexe pour éviter la dérive d'agent et améliorer la qualité
- **Memory bank** : Utilisation de fichiers intermédiaires (specs, plans, notes) comme mémoire persistante entre sessions pour maintenir la cohérence et réduire la charge contextuelle
- **Spec files** : Fichiers de spécifications comme contrat entre sessions, réduisent le besoin de contexte répété
- **Spec-first . Spec-Anchored vs. Spec-as-source** : Spec-first = écrire une spec réfléchie avant de développer avec l'IA ; Spec-anchored = conserver la spec après implémentation pour l'évolution/maintenance ; Spec-as-source = la spec devient le fichier principal édité par l'humain, le code n'est plus touché directement

**Erreurs fréquentes** :
- Tenter d'implémenter toute la fonctionnalité en une seule session d'agent
- Spécifications trop génériques ou trop détaillées
- Ne pas valider le plan avant de générer les specs

## US - 6
Standardiser les suggestions de Copilot à l'échelle d'une équipe via des instructions personnalisées. Développer la capacité à adapter le comportement de l'IA aux conventions projet.

**Concepts théoriques** :
- **Custom Instructions** : Configuration hiérarchique (globales + contextuelles) pour guider Copilot selon les standards d'équipe
- **ApplyTo** : Ciblage précis des instructions par pattern de fichiers (controllers, services, repositories, tests)
- **Context Engineering** : Réduction du besoin de répéter les conventions dans chaque prompt
- **Chat Debug View** : Vérification des instructions effectivement appliquées selon le fichier ouvert

**Erreurs fréquentes** :
- Instructions trop verbeuses ou trop génériques
- Ne pas valider l'application effective via le debug view
- Mélanger instructions générales et spécifiques dans un même fichier

## US - 7
Industrialiser l'usage de Copilot en créant une bibliothèque de prompts réutilisables. Développer la capacité à standardiser les tâches récurrentes et partager des workflows d'équipe.

**Concepts théoriques** :
- **Prompt Files** : Bibliothèque de commandes slash personnalisées (`.prompt.md`) dans `.github/prompts/`
- **Réutilisabilité** : Encapsuler logique complexe, éviter répétition, garantir cohérence entre devs
- **Variables d'entrée** : `argument-hint` pour guider utilisateur, interpolation dans le prompt
- **Context Engineering** : Référencer custom instructions, fichiers, workspaces pour contexte riche

**Erreurs fréquentes** :
- Prompts trop génériques ou non testés sur cas réels
- Ne pas utiliser `argument-hint` pour guider l'utilisateur

## US - 8
Développer la capacité à identifier les cas d'usage d'agents spécialisés et comprendre leur apport versus les modes standards. Adopter une approche task-specific agents pour les workflows complexes récurrents.

**Concepts théoriques** :
- **Custom Agents** : Agents spécialisés (`.agent.md`) dans `.github/agents/` pour workflows experts (ADR, migration code, revue sécu)
- **Task-specific vs. Generic** : Agents spécialisés = instructions + context + handoffs pré-configurés pour un domaine
- **Community Agents** : Réutilisation d'agents éprouvés ([awesome-copilot](https://github.com/github/awesome-copilot/blob/main/docs/README.agents.md))
- **Comparaison Edit/Agent** : Edit = modification locale simple ; Agent spécialisé = workflow complet avec validation, alternatives, format standardisé

**Erreurs fréquentes** :
- Utiliser un agent spécialisé pour des tâches simples (surcharge inutile)
- Installer un agent sans le tester sur cas réel du projet