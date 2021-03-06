'''
在使用 for 循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少,
例如：有列表 numbers = [10, 29, 30, 41]，要求输出 (0, 10)，(1, 29)，(2, 30)，(3, 41)
'''


def enumerator(seq):
    for index, num in enumerate(seq):
        yield (index, num)


numbers = [10, 29, 30, 41]
for each in enumerator(numbers):
    print(each)
