STATUS: COMPLETED

**Ce que j’ai fait :**
- Développé le module `binxml.py` pour classifier les bytes de tokens Binary XML EVTX.
- Ajout d’une structure `BinXmlToken` avec offset, valeur, type reconnu et flag `has_more`.
- Enrichi `summarize_binxml()` avec liste de tokens et indication de troncature.
- Ajout de l’option CLI `--binxml-token-limit`.
- Mise à jour du README et des notes de format.
- Ajout/ajustement des tests unitaires et CLI.
- Validation : `19 passed`.
- Commit Git : `528290b` (`Classify Binary XML token bytes`).

**Ce qu’il reste :**
- Décoder le contenu des tokens Binary XML, pas seulement les classifier.
- Reconstruire une structure XML/événement exploitable.
- Ajouter les filtres métier après extraction des champs événementiels.

**Prochaine étape :**
- Implémenter le décodage des premiers tokens avec payload structuré, en commençant par fragment header, template instance et substitutions.
⚠️ 🛠️ `run python3 (agent)` failed