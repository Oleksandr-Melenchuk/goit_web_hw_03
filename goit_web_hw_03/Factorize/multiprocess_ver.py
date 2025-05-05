import os
from multiprocessing import Pool
import time


def factorize(n):
    solution_list = []
    for number in range(1, n + 1):
        if n % number == 0:
            solution_list.append(number)
    
    return solution_list



if __name__ == '__main__':
    args = (128, 255, 99999, 10651060)
    core_count = os.cpu_count()
    
    start = time.time()
    
    with Pool(processes=core_count) as pool:
        result = pool.map(factorize, args)
        
    end = time.time()
        
    print(result)
    print(f"Час виконання {end - start}")
        
        