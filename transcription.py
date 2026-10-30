#@title Script Complet : Installation et Transcription Whisper

# 1. Installer Whisper
!pip install git+https://github.com/openai/whisper.git

# 2. Connecter Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 3. Paramètre du fichier et Transcription
# Collez ci-dessous le chemin d'accès de votre fichier audio/vidéo copié depuis Google Drive
# Astuce : dans Colab, naviguez dans le dossier drive à gauche, clic droit sur votre fichier -> "Copier le chemin d'accès"
chemin_fichier = "/content/drive/MyDrive/Enregistrements/MonCours.mp4" #@param {type:"string"}

!whisper "{chemin_fichier}" --model medium --language French

