# -*- Encoding: utf-8 -*-
"""数理统计"""


def count_comb(total, chose):
    """C_total^chose 的组合数

    组合太大时,
    - 使用 itertools.combinations 计数, 卡死.
    - reduce 计算分子 / 分母时, 存在溢出风险.
    """
    # 分子分母对应位置相除, 商
    quotient = map(lambda x, y: 1.0*x/y,
                   range(total, total-chose, -1),
                   range(chose, 0, -1))
    # 商连乘
    cnt = reduce(lambda x, y: x*y, quotient, 1.0)
    return int(round(cnt, 0))  # float 转最近的 int:w


if __name__ == '__main__':
    for i in range(8+1):
        print count_comb(8, i)
