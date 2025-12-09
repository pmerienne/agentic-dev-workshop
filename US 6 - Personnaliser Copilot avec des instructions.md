En tant que développeur, je souhaite bénéficier de suggestions Copilot adaptées aux standards de mon équipe.
==

## WHY

L'équipe s'agrandit rapidement et chaque développeur a sa propre façon de coder. Les code reviews révèlent des incohérences : certains utilisent des exceptions customs, d'autres des codes HTTP génériques ; certains documentent en français, d'autres en anglais ; les conventions de nommage varient ... Bref, notre lead a décidé : il faut standardiser l'aide de Copilot pour que les suggestions respectent automatiquement les conventions TaskFlow. Résultat attendu : moins de friction en review et un code plus homogène => plus de vélocité.

## WHAT

Mettre en place un système d'instructions personnalisées pour GitHub Copilot à trois niveaux :

1. **Instructions globales du projet** (`.github/copilot-instructions.md`)
   - Standards généraux applicables dans les projets (à mettre dans`/java` ou `/python`)
   - Règles métier transverses de TaskFlow
   - Structure du projet

2. **Instructions spécifiques par contexte** (`.github/instructions/*.instructions.md`)
   - Instructions ciblées selon la couche en cours d'édition (controller, service et repository)
   - Utilisation du champ `applyTo` pour définir le périmètre d'application

## RÈGLES MÉTIER & STANDARDS TASKFLOW

### Standards généraux

**Architecture & Design**
- Architecture en couches : Controller → Service → Repository → DB
- Principe de responsabilité unique : chaque classe a un rôle clair
- Pas de logique métier dans les contrôleurs
- Validation des entrées au niveau Controller
- Gestion d'erreur cohérente avec des exceptions métier

**Documentation**
- Code et commentaires en **anglais uniquement**
- Docstrings/Javadoc pour toutes les méthodes publiques
- Format : description brève, params, returns, throws/raises
- Exemples d'usage pour les méthodes complexes

**Naming conventions**
- Variables et méthodes : `camelCase` en Java, `snake_case` en Python
- Classes : `PascalCase` dans les deux langages
- Constantes : `UPPER_SNAKE_CASE`
- Préfixes significatifs : `is/has` pour booléens, `get/set` pour accesseurs

### Standards spécifiques par contexte

**Pour les contrôleurs**
- Codes HTTP précis : 200 OK, 201 Created, 204 No Content, 400 Bad Request, 404 Not Found
- Pas de logique métier : déléguer au Service

**Pour les services**
- Toute la logique métier doit être ici
- Lever des exceptions métier personnalisées (ex: `TaskNotFoundException`, `InvalidTaskStateException`)
- Transactions gérées au niveau Service
- Méthodes testables unitairement sans dépendances externes

**Pour les repositories**
- Pas de logique métier, uniquement de l'accès données
- Nommage des méthodes selon conventions (`findBy...`, `existsBy...`)

**Pour les tests**
- Pattern AAA : Arrange, Act, Assert
- Un test = un scénario = une assertion principale
- Nommage descriptif : `shouldReturnErrorWhenTitleIsTooShort`
- Utiliser des builders/factories/fixture pour les données de test
- Mocker les dépendances externes

## HOW

### Étape 1 : Créer les instructions globales

1. **Créer le fichier `.github/copilot-instructions.md`**
   - Utilise le mode **Edit** pour créer ce fichier
   - Demande à Copilot : "Crée un fichier d'instructions globales pour Copilot avec les standards généraux du projet et la structure du projet"

2. **Instructions pour les contrôleurs**
   - Créer `.github/instructions/controller.instructions.md`
   - Ajouter le champ `applyTo` pour cibler uniquement les fichiers de contrôleurs
   - Exemple de `applyTo` :
     ```yaml
     ---
     applyTo:
       - "**/*Controller.java"
       - "**/controller.py"
     ---
     ```
   - Ajouter les standards de la section "Pour les contrôleurs"

3. **Instructions pour les services**
   - Créer `.github/instructions/service.instructions.md`
   - Utiliser `applyTo` pour cibler `**/*Service.java` et `**/service.py`
   - Ajouter les standards de la section "Pour les services"

4. **Instructions pour les repositories**
   - Créer `.github/instructions/repository.instructions.md`
   - Cibler avec `applyTo` : `**/*Repository.java` et `**/repository.py`
   - Ajouter les standards de la section "Pour les repositories"

5. **Instructions pour les tests**
   - Créer `.github/instructions/test.instructions.md`
   - Cibler avec `applyTo` : `**/test/**/*.java` et `**/test_*.py`
   - Ajouter les standards de la section "Pour les tests"

6. **Vérifier l'application des instructions**
   - Ouvre un fichier existant (ex: `TaskService`) 
   - Demande à Copilot en mode **Ask** : "Comment devrais-je documenter une nouvelle méthode publique ?"
   - Vérifie que la réponse mentionne l'anglais et le format docstring/javadoc
   - Ouvre le chat debug view pour vérifier les instructions prises en compte


## RESSOURCES

- [GitHub Copilot Custom Instructions](https://docs.github.com/fr/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
- [Get the best results with Coding Agent](https://docs.github.com/fr/copilot/tutorials/coding-agent/get-the-best-results)
- [Best practices for custom instructions](https://docs.github.com/en/copilot/customizing-copilot/best-practices-for-custom-instructions)

## VALIDATION CRITERIA

### Fichiers créés
- ✅ `.github/copilot-instructions.md` existe et contient les standards généraux
- ✅ `.github/instructions/controller.instructions.md` existe avec `applyTo` configuré
- ✅ `.github/instructions/service.instructions.md` existe avec `applyTo` configuré
- ✅ `.github/instructions/repository.instructions.md` existe avec `applyTo` configuré
- ✅ `.github/instructions/test.instructions.md` existe avec `applyTo` configuré


### Efficacité validée
- ✅ Copilot génère des suggestions conformes aux standards dans les contrôleurs
- ✅ Copilot place correctement la logique métier dans les services
- ✅ Copilot génère des tests suivant le pattern AAA
- ✅ Documentation générée en anglais avec le bon format
- ✅ Conventions de nommage respectées automatiquement
