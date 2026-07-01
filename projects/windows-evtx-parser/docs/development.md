STATUS: COMPLETED

**Ce que j’ai fait :**
- Ajout d’un module `binxml.py` avec résumé défensif et lossless des payloads Binary XML.
- Ajout des options CLI :
  - `--include-data` pour inclure le payload brut en hexadécimal.
  - `--binxml-summary` pour exposer taille, premier token et données hex.
- Ajout de tests unitaires pour `binxml.py` et de tests CLI associés.
- Mise à jour du README et des notes de format.
- Validation : `16 passed`.
- Commit Git : `8b8f17b` (`Add Binary XML payload summaries`).

**Ce qu’il reste :**
- Décoder réellement les tokens Binary XML EVTX.
- Construire une dataclass événement structurée (`EvtxEvent`).
- Ajouter les filtres métier : `--event-id`, `--provider`, dates.

**Prochaine étape :**
- Implémenter le premier vrai parseur Binary XML incrémental, en commençant par les tokens de fragments/templates et chaînes.