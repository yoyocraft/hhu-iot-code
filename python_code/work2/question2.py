from math import sqrt

def gen_factors(n: int) -> list:
    factors = [1]
    sqrt_n = int(sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if not n % i:
            factors.append(i)
            j = n // i
            if i != j:
                factors.append(j)
    factors.append(n)
    factors.sort()
    return factors

factors_map = {}
for i in range(10, 101):
    factors_map[i] = gen_factors(i)

# 输出到屏幕
for k, v in factors_map.items():
    print("{}的因子：{}".format(k, ', '.join(map(str, v))))
    
# 输出到文件
with open('1.txt', 'wb') as f:
    for k, v in factors_map.items():
        f.write("{}的因子：{}\n".format(k, ', '.join(map(str, v))).encode("UTF-8"))