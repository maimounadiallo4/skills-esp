#@title Script Complet : Installation et Transcription Whisper

# 1. Installer Whisper
!pip install git+https://github.com/openai/whisper.git

# 2. Connecter Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 3. Paramètre du fichier et Transcription
chemin_fichier = "/content/drive/MyDrive/Enregistrement cours DIC2 Génie Informatique/POO avancée/Poo-Cours1.mp4" #@param {type:"string"}

!whisper "{chemin_fichier}" --model medium --language French
