import time


def factorize(*args):
    solution_list = []
    start_time = time.time()
    
    for final_number in args:
        current_number_list = []
        
        for number in range(1, final_number + 1):
            if final_number % number == 0:
                current_number_list.append(number)
        
        solution_list.append(current_number_list)
    
    end_time = time.time()
    print(f"Час виконання {end_time - start_time}")
    
    return solution_list


                
            
    
        
    
    
