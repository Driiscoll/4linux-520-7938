import random
import time

cadeiras = 9
pessoas = [
    'fernando',
    'carlos',
    'ricardo', 
    'fabricio', 
    'lucas', 
    'Italo',
    'roberto',
    'fabio',
    'diego',
    'saulo'
]

#print(f"{random.choice(pessoas)}")


while cadeiras > 0:
    pessoas.remove(random.choice(pessoas))
    print(pessoas)
    time.sleep(1)
    cadeiras -= 1