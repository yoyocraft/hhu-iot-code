def check_code(code: str) -> bool:
    """校验卡号是否合法"""
    valid_code = int(code[-1])
    pre_code = code[:-1]
    n = len(pre_code)
    s = 0
    for i in range(0, n, 2):
        mul = int(pre_code[i]) << 1
        while mul:
            s += mul % 10
            mul //= 10
        if i + 1 < n:
            s += int(pre_code[i + 1])

    return 10 - (s % 10) == valid_code


code = '6259650871772098'
print('卡号：{} {}'.format(code, '合法' if check_code(code) else '不合法'))
