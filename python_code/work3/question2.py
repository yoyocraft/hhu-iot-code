def PrintDic(data: dict) -> None:
    """输出传入的字典的内容

    Args:
        data (dict): 传入的字典
    """
    for k, v in data.items():
        print('{}: {}'.format(k, v))


def PrintList(data: list) -> None:
    """输出传入的列表的内容

    Args:
        data (list): 传入的列表
    """
    for item in data:
        print(item)


def Sort(data: list) -> list:
    """对传入的data排序, 按照每个列表元素的第二个元素中的元音字母的个数升序排序

    Args:
        data (list): 由字典的键值对构成的列表

    Returns:
        list: 排序后的列表元素
    """
    def CountVowels(s: str) -> int:
        """返回字符串s中元音字母的个数

        Args:
            s (str): 传入的字符串

        Returns:
            int: s中元音字母的个数
        """
        return len([char for char in s if char.lower() in 'aeiou'])
    sorted_list = sorted(data, key=lambda x: CountVowels(x[1]))
    return sorted_list


def WriteToFile(file_path: str, data: list) -> None:
    """将data写入file_path指定的文件

    Args:
        file_path (str): 文件路径
        data (list): 文件内容
    """
    with open(file_path, 'w') as f:
        for item in data:
            f.write(str(item) + '\n')


def count(data: dict) -> (int, int):
    """统计字典中所有的单词个数和不重复的单词个数

    Args:
        data (dict): 传入的字典

    Returns:
        tuple: (int, int) 第一个值为所有的单词个数，第二个值为不重复的单词个数
    """
    words_count = 0
    unique_words = set()
    for movie in data.values():
        words = movie.split()
        words_count += len(words)
        unique_words.update(words)
    return words_count, len(unique_words)


OscarDic = {
    81: 'Slumdog Millioaire',
    2: 'The Broadway Melody',
    21: 'Hamlet',
    4: 'Cimarron',
    7: 'It Happend One Night',
    5: 'Grand Hotel',
    13: 'Rebecca',
    38: 'The Sound of Music',
    60: 'The Lase Emperor',
    32: 'Ben Hur',
    79: 'The Departed',
    49: 'Rocky'
}

PrintDic(OscarDic)
PrintList(OscarDic.values())
WriteToFile('./Oscar.txt', Sort([k, v] for k, v in OscarDic.items()))
words_count, unique_words_count = count(OscarDic)
print('total words count = {} \nunique words count = {}'.format(
    words_count, unique_words_count))
