'''
data:

| 性别 | 书本 | 服饰 | 零食 | 日用品 |
| ---- | ---- | ---- | ---- | ------ |
| 男   | 15   | 500  | 110  | 80     |
| 男   | 200  | 100  | 130  | 30     |
| 女   | 50   | 700  | 200  | 400    |
| 男   | 80   | 150  | 52   | 200    |
| 男   | 120  | 180  | 60   | 150    |
| 女   | 100  | 250  | 90   | 320    |
| 女   | 24   | 810  | 100  | 88     |
'''

data = [
    {"性别": "男", "书本": 15, "服饰": 500, "零食": 110, "日用品": 80},
    {"性别": "男", "书本": 200, "服饰": 100, "零食": 130, "日用品": 30},
    {"性别": "女", "书本": 50, "服饰": 700, "零食": 200, "日用品": 400},
    {"性别": "男", "书本": 80, "服饰": 150, "零食": 52, "日用品": 200},
    {"性别": "男", "书本": 120, "服饰": 180, "零食": 60, "日用品": 150},
    {"性别": "女", "书本": 100, "服饰": 250, "零食": 90, "日用品": 320},
    {"性别": "女", "书本": 24, "服饰": 810, "零食": 100, "日用品": 88},
]


############################
#          第一题           #
############################
def output(d: dict) -> None:
    for p, data in d:
        print(f"{p}: ￥%.2f" % data)


def cal_category_avg_val() -> dict:
    '''
    绕计每一类消费项目的平均消费金额，并按从大到小排序后输出
    '''
    category_avg = {}
    for d in data:
        for category, val in d.items():
            if category == '性别':
                continue
            if category in category_avg:
                category_avg[category] += val
            else:
                category_avg[category] = val

    for c, v in category_avg.items():
        category_avg[c] = v / len(data)
    return sorted(category_avg.items(), key=lambda x: x[1], reverse=True)


res = cal_category_avg_val()
output(res)


############################
#          第二题           #
############################

def cal_sex_avg_val() -> tuple:
    '''
    分别统计男女生“双十一”的消费总金额的平均值
    '''
    gender_val_dic = {}
    male_count = 0
    for item in data:
        s = 0
        for k in item:
            if k != '性别':
                s += item[k]

        sex = item['性别']
        if sex == '男':
            male_count += 1

        gender_val_dic[sex] = gender_val_dic.get(sex, 0) + s

    male_avg = gender_val_dic['男'] / male_count
    female_avg = gender_val_dic['女'] / (len(data) - male_count)
    return male_avg, female_avg


male_avg, female_avg = cal_sex_avg_val()
print("男生双十一消费总金额平均值: ￥{:<10.2f}".format(male_avg))
print("女生双十一消费总金额平均值: ￥{:<10.2f}".format(female_avg))
