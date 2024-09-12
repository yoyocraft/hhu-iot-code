import random

NO_POOL = set()
MOD = 5
BOUND = 100

def test():
    while True:
        if len(NO_POOL) == 5: 
            break
        no = random.randint(1, 100) % MOD
        if no not in NO_POOL:
            NO_POOL.add(no)
            print(no)
            print(NO_POOL)



for _ in range(10):
    test()