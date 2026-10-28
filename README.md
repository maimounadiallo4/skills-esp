# Utilitaires

Une petite collection de skills et de scripts de productivité conçus pour aider à la rédaction académique, à la prise de notes, à l'organisation du contenu et aux flux de transcription automatisée.
Part of "Kit de survie au DGI" !

## Vue d'ensemble

Ce dépôt regroupe un ensemble de compétences personnalisées et d'utilitaires pour des flux de travail courants tels que :

- la mise en forme de documents académiques
- la génération de bannières visuelles pour les pages Notion
- la capture et la structuration de notes pour Notion
- l'enregistrement et l'organisation des notes de cours
- la transcription de fichiers audio ou vidéo avec Whisper

## Contenu du dépôt

- `dgi-academic-formatter.skill` : skill pour rendre un document word généré avec une IA (like Claude) plus professionnel.
- `notion-banner-creator.skill` : skill pour générer des bannières thématiques pour les pages Notion.
- `notion-note-taker.skill` : skill pour transformer la transcription d'un cours en notes structurées intégrées directement dans Notion.
- `obs-note-taker.skill` : skill pour transformer la transcription d'un cours en notes markdown structurées à mettre dans Obsidian.
- `transcription.py` : script Python à exécuter sur Google colab, qui transcrit les enregistrements importés dans google drive à l'aide de Whisper d'OpenAI.

## Premiers pas

### 1. Cloner le dépôt

```bash
git clone https://github.com/maimounadiallo4/skills-esp.git
cd skills-esp
```

### 2. Utiliser les skills

Téléversez les fichiers `.skill` sur claude.ai par exemple afin qu'il les utilise au besoin, au lieu de devoir tout le temps copier coller un prompt.

### 3. Exécuter le script de transcription

Si vous utilisez Google Colab, il faudra juste autoriser le montage de Drive pour charger des fichiers depuis Google Drive. 

## LE workflow à suivre

1. Enregistrer un cours.
2. Mettre la vidéo sur Google Drive.
3. Ajouter un raccourci du dossier contenant les enregistrements dans "Mon Drive".
4. Uploader le script de transcription dans colab.
5. Activer GPU T4.
6. Autoriser le montage de google drive.
7. Cliquer sur l'icône dossier de la barre latérale gauche, attendre que ça se charge pour que le dossier `drive` apparaisse.
8. Chercher la vidéo que vous voulez transcrire en navigant tranquillement vers son emplacement.
9. Cliquer sur le menu trois points du fichier de la vidéo.
10. Copier le chemin d'accès.
11. Le mettre au niveau du champ de saisie qui apparaît à côté du script.
12. Exécuter.
13. Copier le résultat de la cellule.
14. Allez sur claude.ai pour y coller la transcription.
15. Utilisez une skill pour mettre au propre le contenu dans Notion ou Obsidian.

## Licence

MIT.
