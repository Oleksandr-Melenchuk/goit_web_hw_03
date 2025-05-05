from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import shutil
from main import logging

def user_request():
    
    path_from = Path(input("Введіть папку для копіювання: ").strip())
    if not Path.exists(path_from):
        raise ValueError(f"{path_from} --> Невірно вказаний шлях")

    path_to_raw = input("Введіть шлях куди копіювати (або залиште порожнім для 'dist'): ").strip()
    path_to = Path(path_to_raw) if path_to_raw else Path("dist")
    logging.info(f"{path_to} Введений шлях")
    
    path_to.mkdir(parents=True, exist_ok=True)
    
     
    
    return path_from, path_to

path_from, path_to = user_request()

def found_extensions():
    extensions = set(file.suffix for file in path_from.rglob('*') if file.is_file() )
    return [name.lstrip('.') for name in extensions]

extensions = found_extensions()


def copy_past(extension):
        logging.info(f'Початок копіювання. {extension}')
        for file in path_from.rglob(f'*.{extension}'):
            target_dir = path_to  /  extension
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, target_dir)
        
        logging.info(f'Копіювання завершено. {extension}')
