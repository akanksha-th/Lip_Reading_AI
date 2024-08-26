import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "lipreader-project"

list_of_files = [
    ".github/workflows/.gitkeep",
    "app/modelutils.py",
    "app/utils.py",
    "data/datasets/",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "research/trials.ipynb",
    "README.md",
    "models/model_checkpoints"
]

for filepath in list_of_files:
    filepath = Path(filepath) # convert string to Path object
    filedir, filename = os.path.split(filepath) # split the path into directory and filename
    
    if filedir:
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created directory: {filedir}")
        
    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass # create the file with a placeholder content
        logging.info(f"Created file: {filepath}")
    else :
        logging.info(f"File {filepath} already exists and is not empty.")