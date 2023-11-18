import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name ='TextSummerizer'
list_of_file=[
    ".github/workflows/.gitkeep",
    'src/{}/__init__.py'.format(project_name),
    'src/{}/components/__init__.py'.format(project_name),
    'src/{}/utils/__init__.py'.format(project_name),
    'src/{}/utils/common.py'.format(project_name),
    'src/{}/logging/__init__.py'.format(project_name),
    'src/{}/config/__init__.py'.format(project_name),
    'src/{}/config/configuration.py'.format(project_name),
    'src/{}/pipeline/__init__.py'.format(project_name),
    'src/{}/entity/__init__.py'.format(project_name),
    'src/{}/constants/__init__.py'.format(project_name),
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'

]
for file_path in list_of_file:
    filepath= Path(file_path)
    filedir,filename=os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info('creating directory:{}'.format(filedir))

    if( not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")