def fun(num: int) -> int:
    """判断num是否是回文

    Args:
        num (int): 传入的数字num

    Returns:
        int: 1: num是回文数字, 0: num不是回文数字
    """
    str_num = str(num)
    return str_num == str_num[::-1]


cnt = 0
for i in range(100, 301):
    if fun(i):
        cnt += 1
        print(i, end=' ')
        if not cnt % 5:
            print()
