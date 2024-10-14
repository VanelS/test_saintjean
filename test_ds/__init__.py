import sys
import os

# Obtenir le chemin du dossier parent
parent_dir = os.path.dirname(os.getcwd())

# Ajouter le chemin du dossier parent au PYTHONPATH
sys.path.append(parent_dir)