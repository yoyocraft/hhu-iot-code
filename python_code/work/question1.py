# 小夏和小迪按到一个调研任务，需要按省份统计班级同学的籍贯分布
# 情况。他们决定两人分头统计男生和女生的籍贯分布，最后再汇总结果。
# 己知小夏统计的女生籍贯分别是：江苏3人，浙江12人，吉林4人，甘肃
# 12人；小迪统计的男生籍贯分布是：江苏8人、浙江15人，山东11人、安
# 徽14人、福建21人。请编写程序将两人的调研结果合并并输出，要求用
# 字典实现，字典中的元素示例："江苏"：{"男"：3人, "女"：8人}


def merge_dict(girls: dict, boys: dict) -> dict:
    res = {}

    for p, c in girls.items():
        if p in res:
            res[p]['女'] = c
        else:
            res[p] = {'女': c}

    for p, c in boys.items():
        if p in res:
            res[p]['男'] = c
        else:
            res[p] = {'男': c}

    return res


def output(d: dict) -> None:
    for p, data in d.items():
        print("{:<5s}: {:<10s}".format(p, str(data)))


# data
xiaoxia_girls = {"江苏": 3, "浙江": 12, "吉林": 4, "甘肃": 12}
xiaodi_boys = {"江苏": 8, "浙江": 15, "山东": 11, "安徽": 14, "福建": 21}

res = merge_dict(xiaodi_boys, xiaoxia_girls)
output(res)
