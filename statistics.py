#!/usr/bin/python
# -*- encoding:utf-8 -*-
import math


def median(vals):
    # 中央値
    return sorted(vals)[len(vals) / 2]


def average(vals):
    # 平均
    return float(sum(vals)) / len(vals)


def starges(vals):
    # スタージェスの公式
    return int(math.floor(1 + math.log(len(vals)) / math.log(2)))


def class_range(vals):
    # 範囲
    return max(vals) - min(vals)


def classes(vals, N=None, MIN=None):
    # 階級リストを返す
    if not N:
        N = starges(vals)
    if not MIN:
        MIN = min(vals)
    R = class_range(vals)
    width = math.floor(R / N)
    return [MIN + width * i for i in xrange(N + 2)]


def frequency(vals, _classes=None):
    # 度数
    if not _classes:
        _classes = classes(vals)
    # 度数
    n = len(_classes)
    ranges = [(x, y) for x, y in zip(_classes[0:n], _classes[1:])]
    return [len(filter(lambda x: a <= x < b, vals)) for a, b in ranges]


def relative_frequency(frequencies):
    num = sum(frequencies)
    return [x * 100 / num for x in frequencies]


def dispersion(vals):
    # 分散
    avg = average(vals)
    N = len(vals)
    return sum([(x - avg) ** 2 for x in vals]) / N


def standard(vals):
    # 標準偏差
    return math.sqrt(dispersion(vals))


def relative_avg(vals):
    avg = average(vals)
    return [v - avg for v in vals]


def norm(vec):
    return math.sqrt(sum([x * x for x in vec]))


def correlation(v1, v2):
    # 相関係数
    # ベクトル列を与える
    v1 = map(float, v1)
    v2 = map(float, v2)
    v1 = relative_avg(v1)
    v2 = relative_avg(v2)
    nv1 = norm(v1)
    nv2 = norm(v2)
    if nv1 * nv2 == 0:
        return 0
    return sum([x * y for x, y in zip(v1, v2)]) / (nv1 * nv2)


def eval_correlation(r):
    if r <= 0:
        return u"相関なし"
    elif 0 <= r <= 0.2:
        return u"ほとんど相関がない"
    elif 0.2 <= r <= 0.4:
        return u"やや相関がある"
    elif 0.4 <= r <= 0.7:
        return u"かなり相関がある"
    elif 0.7 <= r <= 1.0:
        return u"強い相関がある"
    else:
        return u"異常な値です"


if __name__ == "__main__":
    print "median:", median(range(10))
    print "avg:", average(range(10))
    print "starges:", starges(range(10))
    print "range:", class_range(range(10))
    print "classes", [x for x in classes(range(10))]
    print "frequency:", frequency(range(10))
    print "relative frequency:", relative_frequency(frequency(range(10)))
    print "dispersion:", dispersion(range(10))
    print "standard:", standard(range(10))
    print "correlation:", correlation(range(10), range(10))
    print "eval correlation:", eval_correlation(correlation(range(10), range(10)))
