import time
from concurrent.futures import ThreadPoolExecutor

def gcd(pair):
    '''
    max gcd
    '''
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

    assert False, "Not reachable"


# data
NUMBERS = [
    (1963309, 2265973), (5948475, 2734765),
    (1876435, 4765849), (7654637, 3458496),
    (1823712, 1924928), (2387454, 5873948),
    (1239876, 2987473), (3487248, 2098437),
    (1963309, 2265973), (5948475, 2734765),
    (1876435, 4765849), (7654637, 3458496),
    (1823712, 1924928), (2387454, 5873948),
    (1239876, 2987473), (3487248, 2098437),
    (3498747, 4563758), (1298737, 2129874)
]

##
start = time.time()
results = list(map(gcd, NUMBERS))
end = time.time()
delta = end - start
print(f'serial: {delta:.3f} s')

##
start = time.time()
pool = ThreadPoolExecutor(max_workers=9)
results = list(pool.map(gcd, NUMBERS))
end = time.time()
delta = end - start
print(f'multi thered: {delta:.3f} s')