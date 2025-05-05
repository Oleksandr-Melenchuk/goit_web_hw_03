import logging
from func import *

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


if __name__ == '__main__':
    
    with ThreadPoolExecutor() as executor:
        for extention in extensions:    
            executor.submit(copy_past, extention)