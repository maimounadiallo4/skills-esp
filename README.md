# skills-esp

Une petite collection de skills GitHub Copilot et de scripts de productivité conçus pour aider à la rédaction académique, à la prise de notes, à l'organisation du contenu et aux flux de transcription automatisée.

## Vue d'ensemble

Ce dépôt regroupe un ensemble de compétences personnalisées et d'utilitaires pour des flux de travail courants tels que :

- la mise en forme de documents académiques
- la génération de bannières visuelles pour les pages Notion
- la capture et la structuration de notes pour Notion
- l'enregistrement et l'organisation des notes de session
- la transcription de fichiers audio ou vidéo avec Whisper

## Contenu du dépôt

- `dgi-academic-formatter.skill` — une skill pour formater un contenu académique de manière plus claire et plus structurée.
- `notion-banner-creator.skill` — une skill pour générer du contenu de bannière thématique pour les pages Notion.
- `notion-note-taker.skill` — une skill pour collecter et organiser des notes dans Notion.
- `obs-note-taker.skill` — une skill pour capturer des notes dans le cadre de workflows liés à OBS.
- `transcription.py` — un script Python qui transcrit des fichiers média à l'aide de Whisper d'OpenAI.

## Premiers pas

### 1. Cloner le dépôt

```bash
git clone https://github.com/maimounadiallo4/skills-esp.git
cd skills-esp
```

### 2. Utiliser les skills

Les fichiers `.skill` sont destinés à être utilisés avec les skills GitHub Copilot ou des workflows d'agent personnalisés. Copiez-les dans votre dossier de skills configuré ou utilisez-les dans un environnement GitHub Copilot prenant en charge les skills.

### 3. Exécuter le script de transcription

Installez la dépendance requise :

```bash
pip install git+https://github.com/openai/whisper.git
```

Ensuite, modifiez le chemin du fichier dans `transcription.py` puis exécutez :

```bash
python transcription.py
```

Si vous utilisez Google Colab, le script inclut également un exemple de montage de Drive pour charger des fichiers depuis Google Drive.

## Exemple de workflow

1. Enregistrez un cours ou une réunion.
2. Transcrivez l'audio ou la vidéo avec Whisper.
3. Vérifiez ou nettoyez la transcription générée.
4. Utilisez une skill pour organiser le contenu dans Notion ou créer une version académique mise en forme.
5. Publiez ou partagez le matériel final dans le format de votre choix.

## Notes

- Ce projet est orienté vers les workflows de productivité et d'automatisation.
- Certains fichiers sont adaptés à des cas d'usage académiques et de prise de notes en français.
- Le script de transcription est particulièrement utile pour la capture de cours et les tâches de documentation.

## Licence

Ce projet ne déclare pas actuellement de licence. Si vous envisagez de le partager ou de le réutiliser publiquement, pensez à ajouter un fichier de licence approprié tel que MIT ou Apache 2.0.

## Améliorations futures

Des ajouts potentiels incluent :

- un `requirements.txt` dédié pour les dépendances Python
- des exemples d'utilisation pour chaque skill
- des captures d'écran ou des exemples de résultats
- une section de dépannage
- la localisation de la documentation en anglais/français
