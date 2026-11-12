# Utilitaires — Kit de survie au DGI 🎓

Une collection d'outils, de compétences IA (**skills / plugins**) et de scripts de productivité conçus pour accompagner les étudiants dans la rédaction académique, la prise de notes automatique, la transcription et l'organisation de leurs cours.

Ce dépôt fait partie intégrante du [**Kit de survie au DGI**](https://minalab.app/ebooks/kit-de-survie-au-dgi-1801) !

---

## 📦 Organisation du dépôt

Le dépôt est organisé en trois dossiers thématiques :

```text
skills-esp/
├── skills-zip/     # Formats .zip prêts pour Claude.ai (Upload Skill)
├── skills-skill/   # Formats .skill natifs
├── notebooks/      # Notebooks interactifs Google Colab
├── PROMPTS.md      # Bibliothèque texte universelle (ChatGPT, Gemini, DeepSeek...)
└── README.md
```

### 1. Compétences IA (`skills-zip/` & `skills-skill/`)

| Compétence | Description |
| :--- | :--- |
| **`active-learning-tutor`** | Tuteur pédagogique et coach d'apprentissage actif : découpe le cours pas à pas, pose des questions socratiques ciblées, évalue et note rigoureusement (sur 20) sans jamais avancer sans votre validation. |
| **`dgi-academic-formatter`** | Met en conformité les rapports de TP, mémoires, CDC et documents académiques selon les normes officielles du **DGI / ESP Dakar**. |
| **`notion-banner-creator`** | Génère des bannières panoramiques esthétiques (ratio 7:1) adaptées au recadrage et aux icônes des pages Notion. |
| **`notion-note-taker`** | Transforme une transcription brute de cours en fiche structurée pour **Notion**. Optimisé pour les templates Notion (DIC1 & DIC2 Informatique) avec intégration de la base de devoirs ou to-do list native. |
| **`obs-note-taker`** | Alternative pour les adeptes d'**Obsidian** : convertit une transcription en fiche Markdown complète (callouts, LaTeX, diagrammes Mermaid). |

> **Formats disponibles :**
> - **Dossier [`skills-zip/`](skills-zip/)** : fichiers `.zip` prêts à être importés dans [Claude.ai](https://claude.ai) (**Paramètres / Settings > Capabilities > Skills > Upload Skill**).
> - **Dossier [`skills-skill/`](skills-skill/)** : fichiers `.skill` pour les environnements supportant ce format.
> - **Fichier [`PROMPTS.md`](PROMPTS.md)** : texte brut complet des prompts pour les utilisateurs de **ChatGPT**, **Google Gemini**, **DeepSeek** ou Claude gratuit.

---

### 2. Notebooks Google Colab (`notebooks/`)

| Notebook | Description |
| :--- | :--- |
| [**`transcription.ipynb`**](notebooks/transcription.ipynb) | Notebook interactif prêt à l'emploi pour **Google Colab**, permettant de transcrire n'importe quel cours audio ou vidéo depuis Google Drive avec Whisper d'OpenAI (sur GPU T4 gratuit). |
| [**`youtube_playlist_to_notebooklm.ipynb`**](notebooks/youtube_playlist_to_notebooklm.ipynb) | Extrait instantanément tous les liens vidéo d'une playlist YouTube pour les importer en un seul copier-coller comme sources dans **Google NotebookLM**. |

---

## 🎯 Pourquoi utiliser `youtube_playlist_to_notebooklm.ipynb` ?

Lorsque vous suivez une playlist YouTube de cours, de TP ou de vulgarisation technique, il arrive souvent de bloquer sur un concept ou une ligne de code :
- **Le créateur n'est pas joignable** pour répondre à vos questions en direct.
- **Les IA généralistes répondent souvent à côté** car elles n'ont pas le contexte exact, la terminologie ou la progression choisie par l'enseignant.

**La solution NotebookLM :** En injectant la playlist complète comme sources dans **Google NotebookLM**, l'IA s'ancre strictement (*grounding*) sur le contenu de vos vidéos. Vous disposez ainsi d'un tuteur personnalisé capable de clarifier n'importe quel point **avec les explications et exemples précis de votre cours**.

Ce script extrait l'ensemble des URLs de la playlist en quelques secondes, prêt à être copié-collé d'un coup dans NotebookLM !

---

## 💡 Quel outil de prise de notes choisir ?

- **Vous utilisez Notion ?**
  👉 Utilisez **`notion-note-taker`** (disponible dans [`skills-zip/`](skills-zip/) ou [`skills-skill/`](skills-skill/)). Si vous utilisez le template Notion du Kit (DIC1 ou DIC2 Informatique), il crée et relie automatiquement les devoirs dans votre base *« Travail (cours · TD · TP) »*. Si vous avez un autre espace Notion, il insère automatiquement une to-do list interactive dans la page du cours sans blocage.
- **Vous n'utilisez pas Notion ou préférez Obsidian ?**
  👉 Utilisez **`obs-note-taker`**. Il génère un document Markdown autonome prêt à glisser dans votre coffre Obsidian, complet avec métadonnées, callouts et formules.

---

## 🔄 Le Workflow complet (De l'amphi à la fiche de révision)

1. **Enregistrer le cours** (audio ou vidéo sur votre smartphone ou PC).
2. **Déposer le fichier sur Google Drive**.
3. **Ouvrir Google Colab** et importer [`notebooks/transcription.ipynb`](notebooks/transcription.ipynb).
4. **Configurer l'environnement Colab** :
   - Menu *Exécution* > *Modifier le type d'exécution* > Sélectionner **GPU T4** (quota gratuit et rapide).
   - Exécuter la cellule pour installer Whisper et autoriser l'accès à Google Drive.
5. **Indiquer votre fichier** :
   - Dans le volet latéral gauche de Colab, ouvrez l'onglet *Fichiers* (`drive/MyDrive/...`).
   - Clic droit sur votre enregistrement > **Copier le chemin d'accès**.
   - Collez ce chemin dans la variable `chemin_fichier` et lancez la transcription.
6. **Structurer les notes avec Claude** :
   - Copiez le texte transcrit généré par Whisper.
   - Sur Claude, activez **`notion-note-taker`** (ou **`obs-note-taker`**) et collez la transcription.
   - Claude génère la fiche de cours complète et structurée en une seule passe !

> 📖 **Envie d'aller plus loin ?** La méthode complète (stratégies de révision, création d'examens d'entraînement avec NotebookLM, optimisation du travail académique et avantages étudiants) est détaillée dans le [**Guide du Kit de survie au DGI**](https://minalab.app/ebooks/kit-de-survie-au-dgi-1801).

---

## 📄 Licence

Distribué sous licence **MIT**. Libre d'utilisation et d'adaptation.
