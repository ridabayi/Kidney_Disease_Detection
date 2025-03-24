"""ce code configure un système de logging pour une application, permettant d'enregistrer des messages d'information et d'erreur
 dans un fichier tout en les affichant également dans la console. Cela aide à suivre l'exécution de l'application et à diagnostiquer 
 d'éventuels problèmes."""

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath),
              logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("cnnClassifierLogger")

