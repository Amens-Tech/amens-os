STATUS: COMPLETED

Équipe,

Je lance officiellement le projet **windows-evtx-parser**.

## Objectif du projet

Construire un parseur fiable pour les fichiers **Windows Event Log `.evtx`**, afin d’extraire, structurer et exploiter les événements Windows pour des usages de **cybersécurité**, **forensic**, **audit** et **supervision système**.

Le premier objectif est d’obtenir une version utilisable en ligne de commande capable de lire un fichier `.evtx` et d’exporter les événements dans un format exploitable, idéalement **JSON/JSONL**.

## Premiers jalons

### Jalon 1 — Cadrage technique
- Étudier la structure du format `.evtx`
- Identifier les bibliothèques existantes ou specs pertinentes
- Définir l’architecture du parser
- Valider le langage, les dépendances et le format de sortie

### Jalon 2 — Prototype minimal
- Lire un fichier `.evtx`
- Extraire les événements principaux
- Récupérer les champs clés : timestamp, Event ID, provider, level, record ID, XML brut
- Produire une sortie JSON simple

### Jalon 3 — CLI utilisable
- Créer une commande du type :
  - entrée : chemin vers un fichier `.evtx`
  - sortie : JSON ou JSONL
- Ajouter la gestion des erreurs courantes
- Prévoir une option de sortie vers fichier

### Jalon 4 — Tests et documentation
- Ajouter des tests sur plusieurs fichiers `.evtx`
- Documenter l’installation et l’usage
- Fournir des exemples d’entrée/sortie
- Lister clairement les limitations connues

## Assignation

**Ibrahim**, tu prends le lead opérationnel sur cette première phase.

Tes premières missions :

1. Préparer une courte note technique sur le format `.evtx`
2. Proposer l’architecture initiale du projet
3. Identifier les dépendances nécessaires
4. Mettre en place le squelette du repository
5. Développer un premier prototype capable de lire un fichier `.evtx` et d’exporter les événements en JSON

Priorité : avancer vite vers un prototype simple, testable et propre. On privilégie une approche incrémentale : **lecture fiable d’abord, normalisation ensuite, enrichissements après validation**.