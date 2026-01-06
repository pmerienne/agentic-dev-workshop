En tant que développeur TaskFlow, je souhaite utiliser un agent Copilot personnalisé pour documenter mes décisions architecturales, afin de produire des ADR de qualité professionnelle rapidement.
==

## WHY

Le Product Owner vient d'annoncer une feature majeure : le support multi-tenant. Il s'agit de permettre à plusieurs organisations d'utiliser la même application tout en isolant leurs données. Côté technique, plusieurs options s'offrent à nous : base par tenant, schéma par tenant, ou colonne discriminante ? Cette décision structurante impactera la scalabilité, la sécurité et les coûts d'infrastructure pour les 3 prochaines années. Le tech lead demande un ADR formel avant de trancher. Le product owner nous a informé de certaines contraintes importantes : besoins de scalabilité (1000+ tenants), d'isolation des données et de prévisibilité des coûts. 

## WHAT

Un ADR (Architecture Decision Record) qui compare les trois stratégies principales de multi-tenancy :
- Database-per-tenant
- Schema-per-tenant  
- Row-level isolation

## HOW

1. **Test avec Edit Mode**
   - Crée un fichier vide `docs/adr/adr-001-multi-tenant-strategy.md`
   - Ouvre **Edit Mode** (`Ctrl+I`)
   - Demande à copilot de générer un ADR pour le choix de la stratégie multi-tenancy

2. **Utilisation d'un agent ADR**
   - Télécharge [adr-generator.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/adr-generator.agent.md)
   - Place-le dans `.github/agents/`
   - Ouvre le chat Copilot (`Ctrl+Alt+I`)
   - Selectionne l'agent `adr-generator` (en bas à gauche) et demande lui de générer un ADR pour le choix de la stratégie multi-tenancy

4. **Analyse comparative**
   - Compare la qualité et la structure de l'ADR généré
   - Note les différences : profondeur d'analyse, format, sections, alternatives
   - Identifie les avantages de l'agent spécialisé

## RESSOURCES

- [Custom Agents Documentation](https://docs.github.com/en/copilot/customizing-copilot/custom-agents)
- [ADR Generator Agent](https://github.com/github/awesome-copilot/blob/main/agents/adr-generator.agent.md)
- [Awesome Copilot - Community Agents](https://github.com/github/awesome-copilot/blob/main/docs/README.agents.md)

## VALIDATION CRITERIA

- ✅ L'agent `adr-generator` est installé dans `.github/agents/`
- ✅ Un ADR complet sur le multi-tenancy a été généré via l'agent `adr-generator`
- ✅ Tu comprends quand utiliser un agent personnalisé vs un mode standard
